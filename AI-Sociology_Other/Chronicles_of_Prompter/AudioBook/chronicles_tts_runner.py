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
DEFAULT_OUTPUT = Path("renders_pilot")


@dataclass(frozen=True)
class VoiceSpec:
    voice_id: str
    ref_audio: Path
    ref_text_file: Path


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
    text: str


def die(message: str) -> None:
    raise SystemExit(f"ERROR: {message}")


def read_text_fallback(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8-sig")
    except UnicodeDecodeError:
        return path.read_text(encoding="cp1251")


def parse_casting(path: Path, book_root: Path) -> dict[str, VoiceSpec]:
    if not path.is_file():
        die(f"CASTING.md not found: {path}")

    result: dict[str, VoiceSpec] = {}
    current: str | None = None
    audio: str | None = None
    text: str | None = None

    def flush() -> None:
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
        current = None
        audio = None
        text = None

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


def clean_body_lines(lines: list[str]) -> str:
    # Preserve paragraph structure; remove only outer blank lines and
    # collapse 3+ consecutive blank lines to a normal paragraph break.
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

    # [[EN]] is editorial metadata, not spoken text. We deliberately keep
    # the English words themselves inside the large block for this pilot.
    text = text.replace("[[EN]]", "").replace("[[/EN]]", "")

    if "[[" in text or "]]" in text:
        die("Unknown [[...]] service marker remains in spoken text")

    return text


def parse_blocks(path: Path) -> list[Block]:
    if not path.is_file():
        die(f"Editorial file not found: {path}")

    lines = read_text_fallback(path).splitlines()
    blocks: list[Block] = []
    seen: set[str] = set()
    i = 0

    while i < len(lines):
        if not lines[i].strip():
            i += 1
            continue

        m = re.fullmatch(r"@SEG\s+(\S+)", lines[i].strip())
        if not m:
            die(f"Expected @SEG at line {i + 1}: {lines[i]}")

        block_id = m.group(1)
        if block_id in seen:
            die(f"Duplicate block ID: {block_id}")
        seen.add(block_id)
        i += 1

        meta: dict[str, str] = {}
        while i < len(lines):
            stripped = lines[i].strip()
            if not stripped:
                i += 1
                break
            if not stripped.startswith("@"):
                die(f"{block_id}: expected metadata before text at line {i + 1}")
            if stripped == "@END":
                die(f"{block_id}: @END before text")
            key, _, value = stripped.partition(" ")
            meta[key] = value.strip()
            i += 1

        body_lines: list[str] = []
        while i < len(lines) and lines[i].strip() != "@END":
            body_lines.append(lines[i])
            i += 1

        if i >= len(lines):
            die(f"{block_id}: missing @END")
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

        spoken_text = clean_body_lines(body_lines)
        if not spoken_text:
            die(f"{block_id}: empty spoken text")

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
                text=spoken_text,
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
        description="Render large voice blocks for Chronicles of the Prompter with OmniVoice."
    )
    parser.add_argument(
        "--book-root",
        type=Path,
        default=Path.cwd(),
        help="AudioBook directory. Default: current directory.",
    )
    parser.add_argument(
        "--editorial",
        type=Path,
        default=DEFAULT_EDITORIAL,
        help="Pilot markup file relative to AudioBook.",
    )
    parser.add_argument("--model", type=Path, default=DEFAULT_MODEL)
    parser.add_argument(
        "--output",
        type=Path,
        default=DEFAULT_OUTPUT,
        help="Output directory relative to AudioBook.",
    )
    parser.add_argument(
        "--only",
        type=str,
        default=None,
        help="Comma-separated block IDs, e.g. FM_001,FM_003,PRO_002,PRO_017.",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Re-render WAV files that already exist.",
    )
    args = parser.parse_args()

    book_root = args.book_root.resolve()
    editorial = (
        args.editorial.resolve()
        if args.editorial.is_absolute()
        else (book_root / args.editorial).resolve()
    )
    output_dir = (
        args.output.resolve()
        if args.output.is_absolute()
        else (book_root / args.output).resolve()
    )
    cache_dir = book_root / ".tts_cache" / "voice_prompts"
    casting_file = book_root / "CASTING.md"

    output_dir.mkdir(parents=True, exist_ok=True)
    cache_dir.mkdir(parents=True, exist_ok=True)

    casting = parse_casting(casting_file, book_root)
    blocks = parse_blocks(editorial)

    requested = parse_only(args.only)
    if requested is not None:
        known = {b.block_id for b in blocks}
        missing = requested - known
        if missing:
            die(f"Unknown --only block IDs: {', '.join(sorted(missing))}")
        blocks = [b for b in blocks if b.block_id in requested]

    used_voices = list(dict.fromkeys(b.voice for b in blocks))
    missing_voices = [v for v in used_voices if v not in casting]
    if missing_voices:
        die(f"Missing CASTING.md voices: {', '.join(missing_voices)}")

    print(f"Book root : {book_root}")
    print(f"Editorial : {editorial}")
    print(f"Blocks    : {len(blocks)}")
    print(f"Voices    : {', '.join(used_voices)}")
    print(f"Output    : {output_dir}")
    print(f"Model     : {args.model}")
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
    for index, block in enumerate(blocks, start=1):
        wav_path = output_dir / f"{block.block_id}.wav"

        if wav_path.is_file() and not args.force:
            print(
                f"[{index:02d}/{len(blocks):02d}] {block.block_id} "
                f"{block.voice} lang={block.lang} rate={block.rate:.2f} SKIP"
            )
            continue

        print(
            f"[{index:02d}/{len(blocks):02d}] {block.block_id} "
            f"{block.voice} lang={block.lang} rate={block.rate:.2f} "
            f"delivery={block.delivery} process={block.process}"
        )

        audio = model.generate(
            text=block.text,
            language=LANG_MAP[block.lang],
            voice_clone_prompt=prompts[block.voice],
            speed=block.rate,
            normalize_text=False,
            postprocess_output=True,
        )[0]

        sf.write(wav_path, audio, model.sampling_rate, subtype="PCM_16")
        print(f"    -> {wav_path.name}")

    print()
    print("DONE")
    print(f"Rendered blocks: {output_dir}")
    print("NOTE: PAUSE / PROCESS / MUSIC metadata were NOT applied; montage stays separate.")


if __name__ == "__main__":
    main()
