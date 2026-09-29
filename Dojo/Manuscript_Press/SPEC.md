# MANUSCRIPT_PRESS — ENGINEERING SPEC v3.3

```yaml
document: SPEC.md
version: 3.3
status: CURRENT EXECUTION AUTHORITY
date: 2026-09-29
project: MANUSCRIPT_PRESS
root: E:\Gemini\Dojo\Manuscript_Press
execution_model: PILOT_EXECUTION_PROFILE
target_architecture: SPEC v3.2.2 (archived as SPEC_v3.2.2.md, not implemented)
```

This file is the technical contract of the running system.
It does not contain Samurai work-steps, reconstruct checklists, or triad commentary.

---

## 1. Purpose

Manuscript_Press takes one marked SOURCE manuscript and one aligned PROMPT_MAP, runs local Gemma once per production marker, restores protected material mechanically, and writes a pilot assembled file:

`Output/FINAL.manuscript.md`

The engine must not invent research conclusions as a design goal.

---

## 2. Authority layers

```yaml
SPEC.md:                   current execution contract (this file)
SPEC_v3.2.2.md:            frozen target architecture (freeze / commit / STABLE_CONFIG)
Gemma.md:                  model system kernel (not a Samurai prompt)
config/writer_config.yaml: generation knobs and model path
Input/SOURCE_MANUSCRIPT.md: editorial source
Input/PROMPT_MAP.yaml:     per-marker instructions
```

v3.2.2 is not treated as implemented.
Promotion from pilot to v3.2.2 is a separate Shogun decision.

---

## 3. Filesystem

```text
E:\Gemini\Dojo\Manuscript_Press\
  SPEC.md
  SPEC_v3.2.2.md
  README.md
  Gemma.md
  config\writer_config.yaml
  Input\SOURCE_MANUSCRIPT.md
  Input\PROMPT_MAP.yaml
  src\production_runner.py
  src\loader.py
  src\parser\
  Output\FINAL.manuscript.md
  Output\runs\<run_id>\
  run_manuscript_press.bat
```

Canonical inputs are only `Input/`.
Not `source/`. Not `work/revisions/`.

---

## 4. Terminology

```yaml
SOURCE_MANUSCRIPT: whole manuscript with production markers
PROMPT_MAP:        YAML map MP:XXXX -> LONG_RANGE_FRAME + LOCAL_TRANSFORMATION
MARKER:            <!-- MP:XXXX -->
BLOCK:             from a marker to the next marker or EOF
PROTECTED_SPAN:    <!-- MP:PROTECTED id="ID":BEGIN --> ... END -->
SLOT_TOKEN:        ⟦MP_PROTECTED:ID⟧
SLOTTED_SOURCE:    SOURCE with protected bodies replaced by slot tokens
CURRENT_SOURCE:    rewritable text of one block; ATX headings removed
CACHE_BEFORE:      restored prose of the previous block in this run
FINAL:             Output/FINAL.manuscript.md
```

One marker = one `create_chat_completion`.

---

## 5. Inputs

### 5.1 SOURCE_MANUSCRIPT
- UTF-8
- Unique ordered markers `<!-- MP:XXXX -->`
- Optional protected spans, unique IDs, no nesting
- Text before the first marker is SOURCE prefix and belongs in FINAL unchanged

### 5.2 PROMPT_MAP
- Key set identical to SOURCE marker IDs
- Each entry has non-empty LONG_RANGE_FRAME and LOCAL_TRANSFORMATION
- Extra or missing keys → `SOURCE_PROMPT_MAP_MISMATCH`

### 5.3 Gemma.md
- SYSTEM kernel only
- Not concatenated into USER as a second copy

### 5.4 writer_config.yaml

```yaml
model:
  path: E:/Gemini/models/Gemma-The-Writer-9B-D_AU-q5_k_m.gguf
  n_ctx: 8192
generation:
  max_tokens: 2048
  temperature: 0.0
  top_p: 0.9
```

Default model is the 9B path above.
The 10B file `Gemma-The-Writer-N-Restless-Quill-V2-10B-D_AU-q5_k_m.gguf` is an alternative and is not used by this SPEC.

---

## 6. Parsers and loader

Canonical package: `src/parser/`

```text
ProtectedSpanParser.parse(text) -> (spans, slotted_source)
SourceParser.parse(slotted_source) -> list[Marker]
PromptMapParser.parse(path) -> dict
SourcePromptMapValidator.validate(marker_graph, prompt_map) -> True or raise
```

`src/loader.py` loads Llama from writer_config (`n_gpu_layers=-1`, `chat_format="gemma"`).

---

## 7. Invocation

Default:

```text
python -m src.production_runner
```

Preflight (no model load, no completion):

```text
python -m src.production_runner --preflight-only
```

Resume (recovery only, not default):

```text
python -m src.production_runner --start-marker MP:XXXX --prior-run-dir Output/runs/<id>
```

Launcher:

```bat
@echo off
cd /d "%~dp0"
set PYTHONPATH=%CD%
python -m src.production_runner %*
```

Preferred filename: `run_manuscript_press.bat`.
The same body under `manuscript_press.bat` is an alias, not a historical resume command.

---

## 8. Generation contract

### SYSTEM

```text
BEGIN_GEMMA_KERNEL
<Gemma.md>
END_GEMMA_KERNEL

BEGIN_RUNTIME_CONTRACT_OVERRIDE
PROTECTED SLOT RULE and pilot runtime rules
END_RUNTIME_CONTRACT_OVERRIDE
```

STABLE_CONFIG is not emitted.

### USER

```text
BEGIN_LONG_RANGE_FRAME
...
END_LONG_RANGE_FRAME

BEGIN_CONTINUITY_CACHE
...
END_CONTINUITY_CACHE

BEGIN_CURRENT_SOURCE
<rewritable text + slot tokens; no ATX headings>
END_CURRENT_SOURCE

BEGIN_LOCAL_TRANSFORMATION
...
END_LOCAL_TRANSFORMATION
```

Omit `BEGIN_CONTINUITY_CACHE` on the first block.
Do not emit `BEGIN_STRUCTURAL_CONTEXT` or `BEGIN_PROTECTED_CONTEXT`.
Protected bodies stay outside the model and are restored after generation.

### Model call
- `load_model(writer_config)` once per process
- `create_chat_completion(messages, max_tokens, temperature, top_p)` with numeric types
- empty choices or empty content → `GENERATION_FAILED` → STOP, no FINAL

### Cache
For block k > 0, CACHE_BEFORE is the restored prose of block k−1 from this run
(or from `--prior-run-dir` when resuming).

### Slots
1. Write `raw_output.md` before checks.
2. If found slots equal expected → use as-is.
3. If expected is non-empty and found is empty → append missing tokens in order (pilot recovery, must be logged).
4. Any other mismatch → `PROTECTED_MATERIAL_VIOLATION` → STOP.
5. Restore exact protected bodies from parsed SOURCE spans.

### Context window
Estimate SYSTEM+USER against `model.n_ctx`.
Overflow → `SEGMENTATION_TOO_LARGE_FOR_CURRENT_WRITER_CONFIGURATION`.
No truncation. No auto-split. No dropping cache.

---

## 9. Assembly

1. Copy SOURCE prefix before the first marker into FINAL.
2. For each marker in SOURCE order, rebuild the interval:
   - ATX headings from that interval
   - restored rewritable stream
   - a newline before an ATX heading if the previous chunk does not end with newline
3. Write `Output/FINAL.manuscript.md` only if every marker succeeded.

---

## 10. Output sanitation

Before restore, raw model text must not keep runtime grammar or control leakage:

- `BEGIN_*` / `END_*` payload delimiters
- phrases of the class `OPEN SOURCE DECISION`
- placeholders of the class `[To be specified based on SOURCE analysis]`

If CURRENT_SOURCE had no markdown table and raw output contains a markdown table, flag or stop that marker.

---

## 11. Evidence

```text
Output/runs/<run_id>/
  preflight.json
  run.log
  summary.json
  MP-XXXX/
    payload.txt
    structure.json
    raw_output.md
    slotted.md
    restored.md
    rebuilt.md
Output/FINAL.manuscript.md
```

---

## 12. Failure codes in force

```text
SOURCE_PROMPT_MAP_MISMATCH
MARKER_GRAPH_INVALID
PROTECTED_MARKUP_INVALID
PROTECTED_MATERIAL_VIOLATION
SEGMENTATION_TOO_LARGE_FOR_CURRENT_WRITER_CONFIGURATION
GENERATION_FAILED
```

---

## 13. Non-goals of v3.3 execution

- PRODUCTION_REVISION freeze
- STABLE_CONFIG runtime
- human ACCEPT / REJECT machine
- commit ledger
- resident literary memory between markers
- CONCEPT_PACKAGE / paired half-chapters / generated handoff
- automatic SOURCE or PROMPT_MAP editing
- switching to the 10B alternative model
- publication-ready guarantee

---

## 14. Known gaps

The first live article run proved marker traversal works.
It also exposed:

- missing SOURCE prefix in FINAL
- heading glued to previous sentence
- control-delimiter leakage
- invented tables / excerpt commentary on some blocks

These are hardening items. They do not reopen the architecture.

---

END OF SPEC v3.3
