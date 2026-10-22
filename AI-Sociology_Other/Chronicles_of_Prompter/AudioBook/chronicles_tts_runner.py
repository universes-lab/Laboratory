#!/usr/bin/env python
from __future__ import annotations

import argparse
import hashlib
import re
from dataclasses import dataclass
from pathlib import Path

import soundfile as sf
import torch

from omnivoice import OmniVoice, VoiceClonePrompt


VOICE_IDS = {
    "PROMPTER_OLD",
    "PROMPTER_YOUNG",
    "INTEGRATOR",
    "MISS_DUSHNILA",
    "KEEPER",
    "ARCHIVE",
}
PROCESS_IDS = {"NONE", "ARCHIVE_RADIO"}
MUSIC_IDS = {"NONE", "PART_BOUNDARY"}
LANG_MAP = {"RU": "Russian", "EN": "English", "AUTO": None}

DEFAULT_MODEL = Path(
    r"E:\Gemini\Unseen_University_Workshops\OmniVoice.git\models\OmniVoice"
)
DEFAULT_EDITORIAL = Path("editorial/CHRONICLES_TTS_PILOT_FM_PRO.txt")
DEFAULT_STRESS = Path("editorial/CHRONICLES_TTS_RU_STRESS_OVERRIDES.txt")
DEFAULT_OUTPUT = Path("renders_pilot")


@dataclass(frozen=True)
class VoiceSpec:
    voice_id: str
    ref_audio: Path
    ref_text_file: Path


@dataclass(frozen=True)
class StressOverride:
    word: str
    tts: str
    scope: str


@dataclass(frozen=True)
class Take:
    take_id: str
    text: str


@dataclass(frozen=True)
class Block:
    block_id: str
    voice: str
    rate: float
    lang: str
    pause_before_ms: int
    pause_after_ms: int
    delivery: str
    process: str
    music: str
    takes: tuple[Take, ...]


def die(message: str) -> None:
    raise SystemExit(f"ERROR: {message}")


def read_text_fallback(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8-sig")
    except UnicodeDecodeError:
        return path.read_text(encoding="cp1251")


def clean_body_lines(lines: list[str]) -> str:
    lines = list(lines)
    while lines and not lines[0].strip():
        lines.pop(0)
    while lines and not lines[-1].strip():
        lines.pop()

    out: list[str] = []
    blank = False
    for raw in lines:
        line = raw.rstrip()
        if not line.strip():
            if not blank:
                out.append("")
            blank = True
        else:
            out.append(line.strip())
            blank = False

    text = "\n".join(out).strip()
    text = text.replace("[[EN]]", "").replace("[[/EN]]", "")

    if "[[" in text or "]]" in text:
        die("Unknown [[...]] service marker remains in spoken text")
    return text


def parse_casting(path: Path, book_root: Path) -> dict[str, VoiceSpec]:
    if not path.is_file():
        die(f"CASTING.md not found: {path}")

    result: dict[str, VoiceSpec] = {}
    current = None
    audio = None
    text = None

    def flush():
        nonlocal current, audio, text
        if current is None:
            return
        if current not in VOICE_IDS:
            die(f"Unknown VOICE_ID in CASTING.md: {current}")
        if not audio or not text:
            die(f"Incomplete CASTING.md entry for {current}")

        result[current] = VoiceSpec(
            voice_id=current,
            ref_audio=(book_root / audio).resolve(),
            ref_text_file=(book_root / text).resolve(),
        )
        current = audio = text = None

    for raw in read_text_fallback(path).splitlines():
        line = raw.strip()
        if not line:
            flush()
            continue
        if line in VOICE_IDS:
            flush()
            current = line
        elif line.startswith("ref_audio:"):
            audio = line.split(":", 1)[1].strip()
        elif line.startswith("ref_text:"):
            text = line.split(":", 1)[1].strip()
        else:
            die(f"Unexpected CASTING.md line: {raw}")

    flush()
    return result


def parse_stress_overrides(path: Path) -> list[StressOverride]:
    if not path.is_file():
        return []

    result: list[StressOverride] = []
    current: dict[str, str] = {}

    def flush():
        nonlocal current
        if current.get("@WORD") and current.get("@TTS"):
            result.append(
                StressOverride(
                    word=current["@WORD"],
                    tts=current["@TTS"],
                    scope=current.get("@SCOPE", "ALL"),
                )
            )
        current = {}

    for raw in read_text_fallback(path).splitlines():
        line = raw.strip()

        if not line:
            flush()
            continue
        if line.startswith("#"):
            continue
        if line.startswith("@"):
            key, _, value = line.partition(" ")
            current[key] = value.strip()

    flush()
    return result


def apply_stress_overrides(
    text: str,
    block_id: str,
    overrides: list[StressOverride],
) -> str:
    result = text

    for item in overrides:
        if item.scope != "ALL" and item.scope != block_id:
            continue

        pattern = re.compile(
            rf"(?<![\wА-Яа-яЁё]){re.escape(item.word)}(?![\wА-Яа-яЁё])",
            re.IGNORECASE,
        )

        def repl(match):
            source = match.group(0)
            if source[:1].isupper():
                return item.tts[:1].upper() + item.tts[1:]
            return item.tts

        result = pattern.sub(repl, result)

    return result


def parse_blocks(path: Path) -> list[Block]:
    if not path.is_file():
        die(f"Editorial file not found: {path}")

    lines = read_text_fallback(path).splitlines()
    blocks: list[Block] = []
    seen_blocks: set[str] = set()
    seen_takes: set[str] = set()
    i = 0

    while i < len(lines):
        if not lines[i].strip():
            i += 1
            continue

        m = re.fullmatch(r"@SEG\s+(\S+)", lines[i].strip())
        if not m:
            die(f"Expected @SEG at line {i + 1}: {lines[i]}")

        block_id = m.group(1)
        if block_id in seen_blocks:
            die(f"Duplicate block ID: {block_id}")
        seen_blocks.add(block_id)
        i += 1

        meta: dict[str, str] = {}

        while i < len(lines):
            stripped = lines[i].strip()
            if not stripped:
                i += 1
                break
            if not stripped.startswith("@"):
                die(f"{block_id}: expected metadata before body at line {i + 1}")

            key, _, value = stripped.partition(" ")
            meta[key] = value.strip()
            i += 1

        required = {
            "@VOICE",
            "@RATE",
            "@PAUSE_BEFORE",
            "@PAUSE_AFTER",
            "@DELIVERY",
            "@PROCESS",
            "@MUSIC",
            "@LANG",
        }
        missing = required - meta.keys()
        if missing:
            die(f"{block_id}: missing metadata: {', '.join(sorted(missing))}")

        voice = meta["@VOICE"]
        process = meta["@PROCESS"]
        music = meta["@MUSIC"]
        lang = meta["@LANG"].upper()

        if voice not in VOICE_IDS:
            die(f"{block_id}: unknown voice {voice}")
        if process not in PROCESS_IDS:
            die(f"{block_id}: unsupported PROCESS {process}")
        if music not in MUSIC_IDS:
            die(f"{block_id}: unsupported MUSIC {music}")
        if lang not in LANG_MAP:
            die(f"{block_id}: unsupported LANG {lang}")

        declared_takes = int(meta.get("@TAKES", "1"))
        takes: list[Take] = []

        if declared_takes == 1:
            body_lines: list[str] = []

            while i < len(lines) and lines[i].strip() != "@END":
                if lines[i].strip().startswith("@TAKE"):
                    die(
                        f"{block_id}: @TAKES 1 but explicit @TAKE found "
                        f"at line {i + 1}"
                    )
                body_lines.append(lines[i])
                i += 1

            if i >= len(lines):
                die(f"{block_id}: missing @END")
            i += 1

            text = clean_body_lines(body_lines)
            if not text:
                die(f"{block_id}: empty spoken text")

            takes.append(Take(take_id=block_id, text=text))

        else:
            while i < len(lines):
                stripped = lines[i].strip()

                if not stripped:
                    i += 1
                    continue

                if stripped == "@END":
                    i += 1
                    break

                m_take = re.fullmatch(r"@TAKE\s+(\S+)(?:\s+#.*)?", stripped)
                if not m_take:
                    die(
                        f"{block_id}: expected @TAKE or @END at line {i + 1}: "
                        f"{lines[i]}"
                    )

                take_id = m_take.group(1)
                if take_id in seen_takes:
                    die(f"Duplicate take ID: {take_id}")
                seen_takes.add(take_id)
                i += 1

                body_lines = []

                while i < len(lines) and lines[i].strip() != "@END_TAKE":
                    body_lines.append(lines[i])
                    i += 1

                if i >= len(lines):
                    die(f"{take_id}: missing @END_TAKE")
                i += 1

                text = clean_body_lines(body_lines)
                if not text:
                    die(f"{take_id}: empty spoken text")

                takes.append(Take(take_id=take_id, text=text))

            if len(takes) != declared_takes:
                die(
                    f"{block_id}: @TAKES says {declared_takes}, "
                    f"but parsed {len(takes)}"
                )

        blocks.append(
            Block(
                block_id=block_id,
                voice=voice,
                rate=float(meta["@RATE"]),
                lang=lang,
                pause_before_ms=int(meta["@PAUSE_BEFORE"]),
                pause_after_ms=int(meta["@PAUSE_AFTER"]),
                delivery=meta["@DELIVERY"],
                process=process,
                music=music,
                takes=tuple(takes),
            )
        )

    if not blocks:
        die("No voice blocks found")
    return blocks


def voice_fingerprint(spec: VoiceSpec) -> str:
    if not spec.ref_audio.is_file():
        die(f"Reference WAV not found: {spec.ref_audio}")
    if not spec.ref_text_file.is_file():
        die(f"Reference TXT not found: {spec.ref_text_file}")

    h = hashlib.sha256()
    with spec.ref_audio.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    h.update(b"\0")
    h.update(spec.ref_text_file.read_bytes())
    return h.hexdigest()[:16]


def build_voice_prompt(
    model: OmniVoice,
    spec: VoiceSpec,
    cache_dir: Path,
) -> VoiceClonePrompt:
    ref_text = read_text_fallback(spec.ref_text_file).strip()
    if not ref_text:
        die(f"Empty reference text: {spec.ref_text_file}")

    fingerprint = voice_fingerprint(spec)
    cache_file = cache_dir / f"{spec.voice_id}_{fingerprint}.pt"

    if cache_file.is_file():
        print(f"VOICE {spec.voice_id}: cached prompt")
        return VoiceClonePrompt.load(str(cache_file))

    print(f"VOICE {spec.voice_id}: encoding reference")
    prompt = model.create_voice_clone_prompt(
        ref_audio=str(spec.ref_audio),
        ref_text=ref_text,
        preprocess_prompt=True,
    )
    prompt.save(str(cache_file))
    return prompt


def parse_only(value: str | None) -> set[str] | None:
    if not value:
        return None
    ids = {x.strip() for x in value.split(",") if x.strip()}
    return ids or None


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Render Chronicles Pilot voice blocks/takes with OmniVoice."
    )
    parser.add_argument("--book-root", type=Path, default=Path.cwd())
    parser.add_argument("--editorial", type=Path, default=DEFAULT_EDITORIAL)
    parser.add_argument("--stress", type=Path, default=DEFAULT_STRESS)
    parser.add_argument("--model", type=Path, default=DEFAULT_MODEL)
    parser.add_argument("--output", type=Path, default=DEFAULT_OUTPUT)
    parser.add_argument(
        "--only",
        type=str,
        default=None,
        help="Comma-separated parent block IDs, e.g. FM_003,PRO_002,PRO_017.",
    )
    parser.add_argument("--force", action="store_true")
    args = parser.parse_args()

    book_root = args.book_root.resolve()

    editorial = (
        args.editorial.resolve()
        if args.editorial.is_absolute()
        else (book_root / args.editorial).resolve()
    )
    stress_file = (
        args.stress.resolve()
        if args.stress.is_absolute()
        else (book_root / args.stress).resolve()
    )
    output_dir = (
        args.output.resolve()
        if args.output.is_absolute()
        else (book_root / args.output).resolve()
    )

    casting_file = book_root / "CASTING.md"
    cache_dir = book_root / ".tts_cache" / "voice_prompts"

    output_dir.mkdir(parents=True, exist_ok=True)
    cache_dir.mkdir(parents=True, exist_ok=True)

    casting = parse_casting(casting_file, book_root)
    stress_overrides = parse_stress_overrides(stress_file)
    blocks = parse_blocks(editorial)

    only = parse_only(args.only)
    if only is not None:
        known = {block.block_id for block in blocks}
        unknown = sorted(only - known)
        if unknown:
            die(f"Unknown --only block ID(s): {', '.join(unknown)}")
        blocks = [block for block in blocks if block.block_id in only]

    used_voices = list(dict.fromkeys(block.voice for block in blocks))
    missing_voices = [v for v in used_voices if v not in casting]
    if missing_voices:
        die(f"Missing CASTING.md voices: {', '.join(missing_voices)}")

    total_takes = sum(len(block.takes) for block in blocks)

    print(f"Book root  : {book_root}")
    print(f"Editorial  : {editorial}")
    print(f"Stress     : {stress_file}")
    print(f"Blocks     : {len(blocks)}")
    print(f"Takes      : {total_takes}")
    print(f"Voices     : {', '.join(used_voices)}")
    print(f"Output     : {output_dir}")
    print(f"Model      : {args.model}")
    print()

    if not args.model.is_dir():
        die(f"Model directory not found: {args.model}")
    if not torch.cuda.is_available():
        die("CUDA is not available")

    print("Loading OmniVoice once...")
    model = OmniVoice.from_pretrained(
        str(args.model),
        device_map="cuda:0",
        dtype=torch.float16,
        load_asr=False,
    )
    print(f"Model ready: {torch.cuda.get_device_name(0)}")
    print()

    prompts: dict[str, VoiceClonePrompt] = {}
    for voice_id in used_voices:
        prompts[voice_id] = build_voice_prompt(
            model=model,
            spec=casting[voice_id],
            cache_dir=cache_dir,
        )

    print()
    index = 0

    for block in blocks:
        block_dir = output_dir / block.block_id
        block_dir.mkdir(parents=True, exist_ok=True)
        language = LANG_MAP[block.lang]

        for take in block.takes:
            index += 1
            wav_path = block_dir / f"{take.take_id}.wav"

            if wav_path.is_file() and not args.force:
                print(
                    f"[{index:03d}/{total_takes:03d}] {take.take_id} "
                    f"{block.voice} rate={block.rate:.2f} lang={block.lang} SKIP"
                )
                continue

            synthesis_text = apply_stress_overrides(
                take.text,
                block.block_id,
                stress_overrides,
            )

            print(
                f"[{index:03d}/{total_takes:03d}] {take.take_id} "
                f"{block.voice} rate={block.rate:.2f} lang={block.lang}"
            )

            audio = model.generate(
                text=synthesis_text,
                language=language,
                voice_clone_prompt=prompts[block.voice],
                speed=block.rate,
                normalize_text=False,
                postprocess_output=True,
            )[0]

            sf.write(
                wav_path,
                audio,
                model.sampling_rate,
                subtype="PCM_16",
            )

    print()
    print("DONE")
    print(f"Rendered takes: {total_takes}")
    print(f"Output: {output_dir}")


if __name__ == "__main__":
    main()
