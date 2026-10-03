"""
MANUSCRIPT_PRESS — PILOT PRODUCTION RUNNER
Authority: SPEC v3.2.2 (target) + PILOT_EXECUTION_PROFILE + ROUTE_DELTA_2

Usage:
  python -m src.production_runner --preflight-only
  python -m src.production_runner
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

import yaml

from src.loader import load_model
from src.parser.protected_span_parser import ProtectedSpanParser
from src.parser.prompt_map_parser import PromptMapParser
from src.parser.source_parser import Marker, SourceParser
from src.parser.source_prompt_map_validator import SourcePromptMapValidator

# --- paths (defaults; overridable by CLI) ---
DEFAULT_SOURCE = "Input/SOURCE_MANUSCRIPT.md"
DEFAULT_PROMPT_MAP = "Input/PROMPT_MAP.yaml"
DEFAULT_GEMMA = "Gemma.md"
DEFAULT_WRITER_CONFIG = "config/writer_config.yaml"

SLOT_RE = re.compile(r"⟦MP_PROTECTED:([^⟧]+)⟧")
ATX_RE = re.compile(r"^(#{1,6})\s+\S")
MARKER_LINE_RE = re.compile(r"<!--\s*MP:(\d{4})\s*-->")

RUNTIME_OVERRIDE = """BEGIN_RUNTIME_CONTRACT_OVERRIDE
For this pilot production run, treat the legacy Concept Package / Package Prompt
wording in the Gemma kernel as superseded by the structured USER message.

The authorities for this inference are only the USER sections actually present:
LONG_RANGE_FRAME,
CONTINUITY_CACHE,
CURRENT_SOURCE,
LOCAL_TRANSFORMATION.

Do not invent substantive material beyond those supplied authorities.
Do not require a legacy Concept Package or Package Prompt.

PROTECTED SLOT RULE (mandatory):
Any token of the exact form ⟦MP_PROTECTED:ID⟧ that appears inside CURRENT_SOURCE
must be copied into your output unchanged, in the same relative order.
Do not expand, paraphrase, delete, or replace these tokens with prose.
Do not invent new protected tokens.
END_RUNTIME_CONTRACT_OVERRIDE"""


def read_text(path: str) -> str:
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def write_text(path: str, content: str) -> None:
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)


def load_writer_config(path: str) -> Dict[str, Any]:
    with open(path, "r", encoding="utf-8") as f:
        cfg = yaml.safe_load(f)
    if not isinstance(cfg, dict):
        raise ValueError(f"writer_config is not a mapping: {path}")
    model = cfg.get("model") or {}
    gen = cfg.get("generation") or {}
    n_ctx = model.get("n_ctx")
    max_tokens = gen.get("max_tokens")
    temperature = gen.get("temperature")
    top_p = gen.get("top_p")
    if not isinstance(n_ctx, int) or n_ctx <= 0:
        raise ValueError(f"Invalid model.n_ctx: {n_ctx!r}")
    if not isinstance(max_tokens, int) or max_tokens <= 0:
        raise ValueError(f"Invalid generation.max_tokens: {max_tokens!r}")
    if not isinstance(temperature, (int, float)):
        raise ValueError(f"Invalid generation.temperature: {temperature!r}")
    if not isinstance(top_p, (int, float)):
        raise ValueError(f"Invalid generation.top_p: {top_p!r}")
    return {
        "n_ctx": int(n_ctx),
        "max_tokens": int(max_tokens),
        "temperature": float(temperature),
        "top_p": float(top_p),
        "raw": cfg,
    }


def estimate_tokens(text: str) -> int:
    # Deterministic bound; not a model call. ~4 chars/token heuristic.
    return max(1, (len(text) + 3) // 4)


def extract_interval(slotted_source: str, marker: Marker, next_marker: Optional[Marker]) -> str:
    current_line = f"<!-- {marker.marker_id} -->"
    start = slotted_source.find(current_line)
    if start < 0:
        # tolerate minor whitespace variants
        m = re.search(rf"<!--\s*{re.escape(marker.marker_id)}\s*-->", slotted_source)
        if not m:
            raise ValueError(f"Marker not found in slotted_source: {marker.marker_id}")
        content_start = m.end()
    else:
        content_start = start + len(current_line)

    if next_marker is None:
        return slotted_source[content_start:]
    next_line = f"<!-- {next_marker.marker_id} -->"
    end = slotted_source.find(next_line, content_start)
    if end < 0:
        m2 = re.search(rf"<!--\s*{re.escape(next_marker.marker_id)}\s*-->", slotted_source[content_start:])
        if not m2:
            raise ValueError(f"Next marker not found: {next_marker.marker_id}")
        end = content_start + m2.start()
    return slotted_source[content_start:end]


def split_structural(interval: str) -> Tuple[str, List[Dict[str, str]]]:
    """
    Split interval into REWRITABLE vs STRUCTURAL_HEADING (ATX outside slot tokens).
    CURRENT_SOURCE for Gemma = concatenated REWRITABLE only.
    structure_map preserves order for assembly.
    """
    lines = interval.splitlines(keepends=True)
    structure_map: List[Dict[str, str]] = []
    rewritable_parts: List[str] = []
    buf: List[str] = []

    def flush_buf() -> None:
        nonlocal buf
        if not buf:
            return
        text = "".join(buf)
        structure_map.append({"type": "REWRITABLE", "text": text})
        rewritable_parts.append(text)
        buf = []

    for line in lines:
        # ATX heading only if line is pure heading (no slot token on same line)
        if ATX_RE.match(line) and "⟦MP_PROTECTED:" not in line:
            flush_buf()
            structure_map.append({"type": "STRUCTURAL_HEADING", "text": line})
        else:
            buf.append(line)
    flush_buf()

    current_source = "".join(rewritable_parts)
    return current_source, structure_map


def slots_in_text(text: str) -> List[str]:
    return SLOT_RE.findall(text)


def normalize_slots(generated: str, expected_ids: List[str]) -> Tuple[str, str]:
    """
    Ensure expected protected slot tokens appear in output (pilot recovery).

    Returns (slotted_text, recovery_note).
    - exact match → unchanged
    - model dropped all expected slots → append tokens in order (pilot)
    - wrong / extra / partial set → PROTECTED_MATERIAL_VIOLATION
    """
    found = slots_in_text(generated)
    if found == expected_ids:
        return generated, "none"
    if not expected_ids:
        if found:
            raise ValueError(
                f"PROTECTED_MATERIAL_VIOLATION: expected [], found {found}"
            )
        return generated, "none"
    # Expected slots present but model omitted every one (common on slot-only blocks).
    if len(found) == 0:
        repaired = generated.rstrip() + "\n\n" + "\n".join(
            f"⟦MP_PROTECTED:{sid}⟧" for sid in expected_ids
        ) + "\n"
        return repaired, f"appended_missing_slots:{expected_ids}"
    raise ValueError(
        "PROTECTED_MATERIAL_VIOLATION: "
        f"expected {expected_ids}, found {found}"
    )


def restore_protected(generated: str, span_by_id: Dict[str, str]) -> str:
    def repl(m: re.Match) -> str:
        sid = m.group(1)
        if sid not in span_by_id:
            raise ValueError(f"PROTECTED_MATERIAL_VIOLATION: unknown slot {sid}")
        return span_by_id[sid]

    return SLOT_RE.sub(repl, generated)


def rebuild_interval(structure_map: List[Dict[str, str]], restored_rewritable: str) -> str:
    parts: List[str] = []
    used = False
    for seg in structure_map:
        if seg["type"] == "STRUCTURAL_HEADING":
            if parts and not parts[-1].endswith("\n"):
                parts.append("\n")
            heading = seg["text"]
            if heading and not heading.endswith("\n"):
                heading = heading + "\n"
            parts.append(heading)
        else:
            if not used:
                parts.append(restored_rewritable)
                used = True
    if not used:
        parts.append(restored_rewritable)
    return "".join(parts)


def build_user_payload(
    long_range: str,
    local_tf: str,
    current_source: str,
    cache_before: Optional[str],
) -> str:
    parts = [
        "BEGIN_LONG_RANGE_FRAME",
        long_range.strip(),
        "END_LONG_RANGE_FRAME",
        "",
    ]
    if cache_before is not None:
        parts.extend(
            [
                "BEGIN_CONTINUITY_CACHE",
                cache_before.strip(),
                "END_CONTINUITY_CACHE",
                "",
            ]
        )
    parts.extend(
        [
            "BEGIN_CURRENT_SOURCE",
            current_source.strip("\n"),
            "END_CURRENT_SOURCE",
            "",
            "BEGIN_LOCAL_TRANSFORMATION",
            local_tf.strip(),
            "END_LOCAL_TRANSFORMATION",
        ]
    )
    payload = "\n".join(parts)
    if "BEGIN_STRUCTURAL_CONTEXT" in payload or "BEGIN_PROTECTED_CONTEXT" in payload:
        raise ValueError("USER payload must not contain STRUCTURAL/PROTECTED context sections")
    return payload


def build_system_payload(gemma_text: str) -> str:
    return (
        f"BEGIN_GEMMA_KERNEL\n{gemma_text.strip()}\nEND_GEMMA_KERNEL\n\n"
        f"{RUNTIME_OVERRIDE}"
    )


def main() -> int:
    ap = argparse.ArgumentParser(description="MANUSCRIPT_PRESS Pilot Production Runner")
    ap.add_argument("--preflight-only", action="store_true")
    ap.add_argument("--source", default=DEFAULT_SOURCE)
    ap.add_argument("--prompt-map", default=DEFAULT_PROMPT_MAP)
    ap.add_argument("--gemma-kernel", default=DEFAULT_GEMMA)
    ap.add_argument("--writer-config", default=DEFAULT_WRITER_CONFIG)
    ap.add_argument(
        "--start-marker",
        default=None,
        help="Resume pilot from this marker id (e.g. MP:0170). "
        "Prior markers are taken from --prior-run-dir rebuilt.md files.",
    )
    ap.add_argument(
        "--end-marker",
        default=None,
        help="Last marker id to process (inclusive). Requires --start-marker.",
    )
    ap.add_argument(
        "--prior-run-dir",
        default=None,
        help="Existing Output/runs/<id> with completed marker folders (for --start-marker).",
    )
    args = ap.parse_args()

    run_id = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    run_dir = Path("Output") / "runs" / run_id
    run_dir.mkdir(parents=True, exist_ok=True)
    log_lines: List[str] = []

    if args.end_marker and not args.start_marker:
        print("FATAL: --end-marker requires --start-marker", file=sys.stderr)
        return 2

    start_idx = 0
    end_idx: Optional[int] = None # Initialize end_idx here

    def log(msg: str) -> None:
        print(msg)
        log_lines.append(msg)

    log(f"RUN_TYPE: PILOT_PRODUCTION")
    log(f"RUN_ID: {run_id}")
    log(f"preflight_only: {args.preflight_only}")

    # --- presence / utf-8 ---
    for p in (args.source, args.prompt_map, args.gemma_kernel, args.writer_config):
        if not Path(p).is_file():
            log(f"FAIL: missing file {p}")
            return 20
        try:
            read_text(p)
        except UnicodeDecodeError:
            log(f"FAIL: not utf-8 {p}")
            return 21

    writer = load_writer_config(args.writer_config)
    log(f"writer_config: n_ctx={writer['n_ctx']} max_tokens={writer['max_tokens']} "
        f"temperature={writer['temperature']} top_p={writer['top_p']}")

    source_text = read_text(args.source)
    gemma_text = read_text(args.gemma_kernel)

    # --- real parsers ---
    protected_spans, slotted_source = ProtectedSpanParser().parse(source_text)
    log(f"ProtectedSpanParser: PASS spans={len(protected_spans)}")
    marker_graph: List[Marker] = SourceParser().parse(slotted_source)
    log(f"SourceParser: PASS marker_count={len(marker_graph)}")
    if not marker_graph:
        log("FAIL: no markers")
        return 23

    # Extract SOURCE prefix before the first marker
    prefix = ""
    first_marker = None
    if marker_graph: # Ensure marker_graph is not empty
        first_marker = marker_graph[0]
        first_marker_line = f"<!-- {first_marker.marker_id} -->"
        first_pos = slotted_source.find(first_marker_line)
        if first_pos < 0:
            m = re.search(rf"<!--\s*{re.escape(first_marker.marker_id)}\s*-->", slotted_source)
            if not m:
                raise ValueError(f"First marker not found in slotted_source: {first_marker.marker_id}")
            first_pos = m.start()
        prefix = slotted_source[:first_pos]
    log(f"PREFIX_BYTES={len(prefix)}")

    prompt_map = PromptMapParser().parse(args.prompt_map)
    log(f"PromptMapParser: PASS entries={len(prompt_map)}")

    SourcePromptMapValidator().validate(marker_graph, prompt_map)
    log("SourcePromptMapValidator: PASS")

    span_by_id = {s.id: s.content for s in protected_spans}

    # inventory
    log("marker_ids: " + ", ".join(m.marker_id for m in marker_graph))

    write_text(str(run_dir / "preflight.json"), json.dumps({
        "run_id": run_id,
        "marker_count": len(marker_graph),
        "marker_ids": [m.marker_id for m in marker_graph],
        "protected_span_count": len(protected_spans),
        "n_ctx": writer["n_ctx"],
        "preflight_only": args.preflight_only,
        "status": "PREFLIGHT_PASS",
    }, indent=2))

    if args.preflight_only:
        log("PREFLIGHT_ONLY: complete, no inference")
        write_text(str(run_dir / "run.log"), "\n".join(log_lines) + "\n")
        return 0

    # --- full pilot generation ---
    if args.start_marker:
        ids = [m.marker_id for m in marker_graph]
        if args.start_marker not in ids:
            raise ValueError(f"--start-marker not in graph: {args.start_marker}")
        start_idx = ids.index(args.start_marker)
        if not args.prior_run_dir:
            raise ValueError("--start-marker requires --prior-run-dir")
        if args.end_marker:
            if args.end_marker not in ids:
                raise ValueError(f"--end-marker not in graph: {args.end_marker}")
            end_idx = ids.index(args.end_marker)
            if end_idx < start_idx:
                raise ValueError(
                    f"--end-marker {args.end_marker} precedes --start-marker {args.start_marker}"
                )
        log(f"RESUME from {args.start_marker} (index {start_idx}) prior={args.prior_run_dir}")

    llm = load_model(args.writer_config)
    log("load_model: OK")

    system_payload = build_system_payload(gemma_text)
    cache_before: Optional[str] = None
    rebuilt_intervals: List[str] = []
    completion_calls = 0

    # Seed completed intervals + cache from prior run when resuming.
    if start_idx > 0:
        prior = Path(args.prior_run_dir)
        for i in range(start_idx):
            m = marker_graph[i]
            rebuilt_path = prior / m.filesystem_id / "rebuilt.md"
            restored_path = prior / m.filesystem_id / "restored.md"
            if not rebuilt_path.is_file():
                raise ValueError(f"Missing prior rebuilt: {rebuilt_path}")
            rebuilt_intervals.append(read_text(str(rebuilt_path)))
            if restored_path.is_file():
                cache_before = read_text(str(restored_path))
            else:
                cache_before = rebuilt_intervals[-1]
        log(f"Seeded {start_idx} prior blocks; cache_len={len(cache_before or '')}")

    for idx, marker in enumerate(marker_graph):
        if idx < start_idx:
            continue
        if end_idx is not None and idx > end_idx:
            break
        next_marker = marker_graph[idx + 1] if idx + 1 < len(marker_graph) else None
        interval = extract_interval(slotted_source, marker, next_marker)
        current_source, structure_map = split_structural(interval)
        expected_slots = slots_in_text(current_source)

        entry = prompt_map.get(marker.marker_id)
        if not entry:
            raise ValueError(f"Missing prompt_map entry for {marker.marker_id}")
        long_range = entry["long_range_frame"]
        local_tf = entry["local_transformation"]

        user_payload = build_user_payload(
            long_range, local_tf, current_source, cache_before if idx > 0 else None
        )

        est = estimate_tokens(system_payload) + estimate_tokens(user_payload)
        log(f"{marker.marker_id}: context_estimate={est} n_ctx={writer['n_ctx']} "
            f"current_source_len={len(current_source)} slots={expected_slots}")
        if est > writer["n_ctx"]:
            raise ValueError(
                "SEGMENTATION_TOO_LARGE_FOR_CURRENT_WRITER_CONFIGURATION: "
                f"{marker.marker_id} estimate={est} n_ctx={writer['n_ctx']}"
            )

        # evidence: payload before inference
        marker_dir = run_dir / marker.filesystem_id
        marker_dir.mkdir(parents=True, exist_ok=True)
        write_text(str(marker_dir / "payload.txt"), user_payload)
        write_text(str(marker_dir / "structure.json"), json.dumps(structure_map, ensure_ascii=False, indent=2))
        write_text(str(marker_dir / "slotted.md"), "[PENDING_INFERENCE]")
        write_text(str(marker_dir / "restored.md"), "[PENDING_INFERENCE]")

        response = llm.create_chat_completion(
            messages=[
                {"role": "system", "content": system_payload},
                {"role": "user", "content": user_payload},
            ],
            max_tokens=writer["max_tokens"],
            temperature=writer["temperature"],
            top_p=writer["top_p"],
        )
        completion_calls += 1

        if not response or "choices" not in response or not response["choices"]:
            raise ValueError(f"Empty model response for {marker.marker_id}")
        generated = response["choices"][0]["message"]["content"]
        if generated is None:
            raise ValueError(f"Empty generated content for {marker.marker_id}")
        generated = str(generated)
        # Always persist raw model text before slot checks (forensics).
        write_text(str(marker_dir / "raw_output.md"), generated)

        if not generated.strip() and not expected_slots:
            raise ValueError(f"Empty generated content for {marker.marker_id}")

        slotted, recovery = normalize_slots(generated, expected_slots)
        if recovery != "none":
            log(f"{marker.marker_id}: slot_recovery={recovery}")
        restored = restore_protected(slotted, span_by_id)
        rebuilt = rebuild_interval(structure_map, restored)

        write_text(str(marker_dir / "slotted.md"), slotted)
        write_text(str(marker_dir / "restored.md"), restored)
        write_text(str(marker_dir / "rebuilt.md"), rebuilt)

        rebuilt_intervals.append(rebuilt)
        cache_before = restored  # pilot: previous restored prose
        log(f"{marker.marker_id}: PASS output_len={len(restored)}")

    if end_idx is not None:
        log(f"END_MARKER_REACHED: end={args.end_marker} processed_upto_idx={end_idx}")
        log(f"completion_calls_total: {completion_calls}")
        log("status: SUCCESS_RANGE scope: PILOT_PRODUCTION")
        log("FINAL not written (range mode)")
        write_text(str(run_dir / "run.log"), "\n".join(log_lines) + "\n")
        write_text(str(run_dir / "summary.json"), json.dumps({
            "status": "SUCCESS_RANGE",
            "scope": "PILOT_PRODUCTION",
            "start_marker": args.start_marker,
            "end_marker": args.end_marker,
            "marker_count": len(marker_graph),
            "completion_calls_total": completion_calls,
            "final_written": False,
            "run_dir": str(run_dir),
        }, indent=2))
        return 0

    final_text = prefix + "".join(rebuilt_intervals)
    if not final_text.strip():
        log("FAIL: empty FINAL")
        write_text(str(run_dir / "run.log"), "\n".join(log_lines) + "\n")
        return 30

    final_path = Path("Output") / "FINAL.manuscript.md"
    write_text(str(final_path), final_text)
    log(f"FINAL: {final_path} size={len(final_text)}")
    log(f"completion_calls_total: {completion_calls} markers: {len(marker_graph)}")
    log("status: SUCCESS scope: PILOT_PRODUCTION")
    log("deferred: STABLE_CONFIG, PRODUCTION_REVISION freeze, commit ledger, "
        "interactive ACCEPT/REJECT, resume, SPEC §19 path")

    write_text(str(run_dir / "run.log"), "\n".join(log_lines) + "\n")
    write_text(str(run_dir / "summary.json"), json.dumps({
        "status": "SUCCESS",
        "scope": "PILOT_PRODUCTION",
        "marker_count": len(marker_graph),
        "completion_calls_total": completion_calls,
        "final_path": str(final_path),
        "final_size": len(final_text),
        "run_dir": str(run_dir),
    }, indent=2))
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception as e:
        print(f"FATAL: {type(e).__name__}: {e}", file=sys.stderr)
        sys.exit(1)
