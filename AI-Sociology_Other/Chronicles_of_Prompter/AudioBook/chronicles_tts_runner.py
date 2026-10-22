#!/usr/bin/env python
from __future__ import annotations

import argparse
import hashlib
import re
import shutil
import subprocess
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
MUSIC_IDS = {"NONE"}

DEFAULT_MODEL = Path(
    r"E:\Gemini\Unseen_University_Workshops\OmniVoice.git\models\OmniVoice"
)

ARCHIVE_FILTER = "highpass=f=300,lowpass=f=3400"


@dataclass(frozen=True)
class VoiceSpec:
    voice_id: str
    ref_audio: Path
    ref_text_file: Path


@dataclass(frozen=True)
class Segment:
    seg_id: str
    voice: str
    rate: float
    pause_before_ms: int
    pause_after_ms: int
    delivery: str
    process: str
    music: str
    text: str


def die(message: str) -> None:
    raise SystemExit(f"ERROR: {message}")


def run(cmd: list[str]) -> None:
    print("  >", " ".join(f'"{x}"' if " " in x else x for x in cmd))
    subprocess.run(cmd, check=True)


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

    for raw in path.read_text(encoding="utf-8-sig").splitlines():
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


def parse_segments(path: Path) -> list[Segment]:
    if not path.is_file():
        die(f"Editorial file not found: {path}")

    lines = path.read_text(encoding="utf-8-sig").splitlines()
    segments: list[Segment] = []
    seen: set[str] = set()
    i = 0

    while i < len(lines):
        if not lines[i].strip():
            i += 1
            continue

        m = re.fullmatch(r"@SEG\s+(\S+)", lines[i].strip())
        if not m:
            die(f"Expected @SEG at line {i + 1}: {lines[i]}")
        seg_id = m.group(1)
        if seg_id in seen:
            die(f"Duplicate segment ID: {seg_id}")
        seen.add(seg_id)
        i += 1

        meta: dict[str, str] = {}
        while i < len(lines) and lines[i].strip().startswith("@"):
            line = lines[i].strip()
            if line == "@END":
                die(f"{seg_id}: @END before text")
            key, _, value = line.partition(" ")
            meta[key] = value.strip()
            i += 1

        while i < len(lines) and not lines[i].strip():
            i += 1

        text_lines: list[str] = []
        while i < len(lines) and lines[i].strip() != "@END":
            if lines[i].strip():
                text_lines.append(lines[i].strip())
            i += 1

        if i >= len(lines):
            die(f"{seg_id}: missing @END")
        i += 1

        required = {
            "@VOICE",
            "@RATE",
            "@PAUSE_BEFORE",
            "@PAUSE_AFTER",
            "@DELIVERY",
            "@PROCESS",
            "@MUSIC",
        }
        missing = required - meta.keys()
        if missing:
            die(f"{seg_id}: missing metadata: {', '.join(sorted(missing))}")

        voice = meta["@VOICE"]
        process = meta["@PROCESS"]
        music = meta["@MUSIC"]

        if voice not in VOICE_IDS:
            die(f"{seg_id}: unknown voice {voice}")
        if process not in PROCESS_IDS:
            die(f"{seg_id}: unsupported PROCESS {process}")
        if music not in MUSIC_IDS:
            die(
                f"{seg_id}: MUSIC={music} is not supported by this pilot runner; "
                "mix music in a separate production stage"
            )

        # O-4: multi-line text inside one SEG is joined by one space.
        spoken_text = " ".join(text_lines).strip()
        if not spoken_text:
            die(f"{seg_id}: empty spoken text")

        segments.append(
            Segment(
                seg_id=seg_id,
                voice=voice,
                rate=float(meta["@RATE"]),
                pause_before_ms=int(meta["@PAUSE_BEFORE"]),
                pause_after_ms=int(meta["@PAUSE_AFTER"]),
                delivery=meta["@DELIVERY"],
                process=process,
                music=music,
                text=spoken_text,
            )
        )

    if not segments:
        die("No segments found")
    return segments


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
    try:
        ref_text = spec.ref_text_file.read_text(encoding="utf-8-sig").strip()
    except UnicodeDecodeError:
        ref_text = spec.ref_text_file.read_text(encoding="cp1251").strip()
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


def ffmpeg_path() -> str:
    found = shutil.which("ffmpeg")
    if found:
        return found

    fallback = Path(r"E:\Samurai_Software\ffmpeg\bin\ffmpeg.exe")
    if fallback.is_file():
        return str(fallback)

    die("ffmpeg not found in PATH or E:\\Samurai_Software\\ffmpeg\\bin")
    return ""


def make_silence(ffmpeg: str, path: Path, milliseconds: int) -> None:
    if milliseconds <= 0 or path.is_file():
        return

    seconds = milliseconds / 1000.0
    run(
        [
            ffmpeg,
            "-hide_banner",
            "-loglevel",
            "error",
            "-y",
            "-f",
            "lavfi",
            "-i",
            "anullsrc=r=24000:cl=mono",
            "-t",
            f"{seconds:.3f}",
            "-c:a",
            "pcm_s16le",
            str(path),
        ]
    )


def process_archive(ffmpeg: str, src: Path, dst: Path, force: bool) -> Path:
    if dst.is_file() and not force:
        return dst

    run(
        [
            ffmpeg,
            "-hide_banner",
            "-loglevel",
            "error",
            "-y",
            "-i",
            str(src),
            "-af",
            ARCHIVE_FILTER,
            "-ar",
            "24000",
            "-ac",
            "1",
            "-c:a",
            "pcm_s16le",
            str(dst),
        ]
    )
    return dst


def write_concat_file(
    segments: list[Segment],
    segment_audio: dict[str, Path],
    silence_dir: Path,
    concat_file: Path,
    ffmpeg: str,
) -> None:
    pause_values = {
        ms
        for seg in segments
        for ms in (seg.pause_before_ms, seg.pause_after_ms)
        if ms > 0
    }

    for ms in sorted(pause_values):
        make_silence(ffmpeg, silence_dir / f"silence_{ms:04d}ms.wav", ms)

    def q(path: Path) -> str:
        return str(path.resolve()).replace("\\", "/").replace("'", "'\\''")

    out: list[str] = []
    for seg in segments:
        if seg.pause_before_ms > 0:
            out.append(
                f"file '{q(silence_dir / f'silence_{seg.pause_before_ms:04d}ms.wav')}'"
            )

        out.append(f"file '{q(segment_audio[seg.seg_id])}'")

        if seg.pause_after_ms > 0:
            out.append(
                f"file '{q(silence_dir / f'silence_{seg.pause_after_ms:04d}ms.wav')}'"
            )

    concat_file.write_text("\n".join(out) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Render the Chronicles of the Prompter OmniVoice pilot."
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
        default=Path("editorial/CHRONICLES_TTS_PILOT_PRO_CH01.txt"),
    )
    parser.add_argument("--model", type=Path, default=DEFAULT_MODEL)
    parser.add_argument(
        "--force",
        action="store_true",
        help="Re-render existing segment WAV files.",
    )
    parser.add_argument(
        "--limit",
        type=int,
        default=7,
        help="Render only the first N segments. Default: 7. Use 0 for all segments.",
    )
    args = parser.parse_args()

    book_root = args.book_root.resolve()
    editorial = (
        args.editorial.resolve()
        if args.editorial.is_absolute()
        else (book_root / args.editorial).resolve()
    )
    casting_file = book_root / "CASTING.md"

    raw_dir = book_root / "renders_raw"
    processed_dir = book_root / "renders_processed"
    final_dir = book_root / "final"
    cache_dir = book_root / ".tts_cache" / "voice_prompts"
    silence_dir = book_root / ".tts_cache" / "silence"

    for d in (raw_dir, processed_dir, final_dir, cache_dir, silence_dir):
        d.mkdir(parents=True, exist_ok=True)

    casting = parse_casting(casting_file, book_root)
    segments = parse_segments(editorial)

    if args.limit < 0:
        die("--limit must be 0 or a positive integer")
    if args.limit > 0:
        segments = segments[: args.limit]

    used_voices = list(dict.fromkeys(seg.voice for seg in segments))
    missing_voices = [v for v in used_voices if v not in casting]
    if missing_voices:
        die(f"Missing CASTING.md voices: {', '.join(missing_voices)}")

    print(f"Book root : {book_root}")
    print(f"Editorial : {editorial}")
    print(f"Segments  : {len(segments)}")
    print(f"Voices    : {', '.join(used_voices)}")
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
    ffmpeg = ffmpeg_path()
    segment_audio: dict[str, Path] = {}

    for index, seg in enumerate(segments, start=1):
        raw_path = raw_dir / f"{seg.seg_id}.wav"

        force_render = args.force or args.limit > 0

        if raw_path.is_file() and not force_render:
            print(
                f"[{index:03d}/{len(segments):03d}] {seg.seg_id} "
                f"{seg.voice} rate={seg.rate:.2f} SKIP"
            )
        else:
            print(
                f"[{index:03d}/{len(segments):03d}] {seg.seg_id} "
                f"{seg.voice} rate={seg.rate:.2f}"
            )

            word_count = len(seg.text.split())
            base_words_per_second = 2.3
            target_duration = max(
                1.0,
                word_count / (base_words_per_second * seg.rate),
            )
            print(
                f"    words={word_count} target_duration={target_duration:.2f}s"
            )

            audio = model.generate(
                text=seg.text,
                language="Russian",
                voice_clone_prompt=prompts[seg.voice],
                duration=target_duration,
                normalize_text=False,
                postprocess_output=True,
            )[0]

            sf.write(raw_path, audio, model.sampling_rate, subtype="PCM_16")

        if seg.process == "ARCHIVE_RADIO":
            processed_path = processed_dir / f"{seg.seg_id}.wav"
            segment_audio[seg.seg_id] = process_archive(
                ffmpeg=ffmpeg,
                src=raw_path,
                dst=processed_path,
                force=force_render,
            )
        else:
            segment_audio[seg.seg_id] = raw_path

    if args.limit > 0:
        concat_name = f"test_first_{len(segments):03d}_concat.txt"
        final_name = f"CHRONICLES_TTS_TEST_FIRST_{len(segments):03d}.wav"
    else:
        concat_name = "pilot_concat.txt"
        final_name = "CHRONICLES_TTS_PILOT_PRO_CH01.wav"

    concat_file = book_root / ".tts_cache" / concat_name
    write_concat_file(
        segments=segments,
        segment_audio=segment_audio,
        silence_dir=silence_dir,
        concat_file=concat_file,
        ffmpeg=ffmpeg,
    )

    final_wav = final_dir / final_name
    run(
        [
            ffmpeg,
            "-hide_banner",
            "-loglevel",
            "error",
            "-y",
            "-f",
            "concat",
            "-safe",
            "0",
            "-i",
            str(concat_file),
            "-ar",
            "24000",
            "-ac",
            "1",
            "-c:a",
            "pcm_s16le",
            str(final_wav),
        ]
    )

    print()
    print("DONE")
    print(f"Final pilot: {final_wav}")


if __name__ == "__main__":
    main()
