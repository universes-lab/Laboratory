# MANUSCRIPT_PRESS ENGINEERING SPEC v3.3

STATUS: CURRENT ARCHITECTURE AFTER DISK-LOSS AUDIT (2026-09-29)
SUPERSEDES AS EXECUTION AUTHORITY: informal pilot notes and Dojo STEP text
DOES NOT REPEAL: ENGINEERING SPEC v3.2.2 as **target** architecture

Two layers are in force.

```yaml
LAYER_T:
  name: TARGET_ARCHITECTURE
  document: ENGINEERING SPEC v3.2.2
  status: FROZEN TARGET
  implemented: no

LAYER_P:
  name: PILOT_EXECUTION_PROFILE
  status: CURRENT EXECUTION AUTHORITY
  implemented: yes (with known hardening gaps)
```

This file specifies **Layer P** completely and states which v3.2.2 requirements remain target-only.

No production inference is authorized by this document.

---

## 0. Purpose

Manuscript_Press transforms:

- one whole SOURCE_MANUSCRIPT with production markers and protected spans
- one aligned PROMPT_MAP
- Gemma.md system kernel
- writer_config generation knobs

into a pilot assembled manuscript via **stateless** per-marker Gemma inference on a local writer model.

The engine must not invent research content as a product goal. First full run proved the engine can traverse a real article and also exposed mechanical assembly defects and Gemma ceiling violations. Those defects are in scope for hardening; they do not reopen paired-run / resident-session / CONCEPT_PACKAGE architecture.

---

## 1. Terminology

```yaml
SOURCE_MANUSCRIPT: whole editor-prepared manuscript with <!-- MP:XXXX --> markers
PROMPT_MAP: YAML mapping MP:XXXX -> LONG_RANGE_FRAME + LOCAL_TRANSFORMATION
Gemma.md: system kernel, SYSTEM role only
WRITER_CONFIG: config/writer_config.yaml (nested model + generation)
MARKER: <!-- MP:XXXX --> start of an elementary prose block
BLOCK: from a marker to the next marker or EOF
PROTECTED_SPAN: <!-- MP:PROTECTED id="ID":BEGIN --> ... END -->
SLOT_TOKEN: ⟦MP_PROTECTED:ID⟧
SLOTTED_SOURCE: SOURCE with protected bodies replaced by slot tokens
CURRENT_SOURCE: rewritable text of one block (headings stripped)
CACHE_BEFORE: verbatim restored prose of previous processed block (pilot)
FINAL: Output/FINAL.manuscript.md — pilot assembly path
```

ONE TRANSACTION = ONE MARKER = ONE create_chat_completion.

---

## 2. Filesystem (current / clean ROOT)

```text
E:\Gemini\Dojo\Manuscript_Press\
  Gemma.md
  config/writer_config.yaml
  Input/SOURCE_MANUSCRIPT.md
  Input/PROMPT_MAP.yaml
  src/production_runner.py
  src/loader.py
  src/parser/*
  Output/FINAL.manuscript.md          # generated
  Output/runs/<run_id>/               # generated evidence
  run_manuscript_press.bat            # clean launcher
```

Not part of current execution:
- `source/`, `work/revisions/`, `assembly/` (v3.2.2 target layout)
- `STABLE_CONFIG.yaml` (target)
- `manuscript_press.bat` historical resume
- `Output/Old/`
- Samurai `GEMINI.md` / `Current_Prompt.md` / `STEP.md` as engine inputs

---

## 3. Inputs and parser contract

### 3.1 SOURCE
- UTF-8
- Ordered unique markers `<!-- MP:dddd -->`
- Optional protected spans with unique IDs, no nesting
- Material before first marker is **SOURCE prefix** and must appear in FINAL unchanged (hardening requirement; missing in snapshot runner)

### 3.2 PROMPT_MAP
- Keys exactly the SOURCE marker ID set
- Each entry: non-empty `LONG_RANGE_FRAME` and `LOCAL_TRANSFORMATION`
- Parser may normalize keys to `long_range_frame` / `local_transformation` internally
- Extra or missing keys → `SOURCE_PROMPT_MAP_MISMATCH`

### 3.3 Parsers (canonical package)
```text
ProtectedSpanParser.parse(text) -> (spans, slotted_source)
SourceParser.parse(slotted_source) -> list[Marker]
PromptMapParser.parse(path) -> dict
SourcePromptMapValidator.validate(marker_graph, prompt_map) -> True or raise
```

Root-level `src/protected_span_parser.py` etc. are not canonical.

### 3.4 writer_config (actual schema)

```yaml
model:
  path: <local .gguf path>
  n_ctx: 8192
generation:
  max_tokens: 2048
  temperature: 0.0
  top_p: 0.9
```

SPEC v3.2.2 flat example is not the on-disk schema. Do not invent `WRITER_CONFIG.yaml` as a second file.

---

## 4. Runtime invocation

### Default (clean)
```text
python -m src.production_runner
```
or `run_manuscript_press.bat` with the same meaning.

### Preflight
```text
python -m src.production_runner --preflight-only
```
Must not call `load_model` or `create_chat_completion`.

### Resume (recovery only)
```text
python -m src.production_runner --start-marker MP:XXXX --prior-run-dir Output/runs/<id>
```
Not the default. Requires intact prior `rebuilt.md` / `restored.md` for all earlier markers. Historical command targeting `20260923T144611Z` is dead after D: loss unless that run dir is separately restored.

---

## 5. Generation contract (pilot)

### SYSTEM
```text
BEGIN_GEMMA_KERNEL
<Gemma.md>
END_GEMMA_KERNEL

BEGIN_RUNTIME_CONTRACT_OVERRIDE
... pilot override including PROTECTED SLOT RULE ...
END_RUNTIME_CONTRACT_OVERRIDE
```

STABLE_CONFIG is **not** emitted (target-only).

### USER
```text
BEGIN_LONG_RANGE_FRAME
...
END_LONG_RANGE_FRAME

BEGIN_CONTINUITY_CACHE          # omit for first block
...
END_CONTINUITY_CACHE

BEGIN_CURRENT_SOURCE
<rewritable + slot tokens; no ATX headings>
END_CURRENT_SOURCE

BEGIN_LOCAL_TRANSFORMATION
...
END_LOCAL_TRANSFORMATION
```

MUST NOT emit:
- BEGIN_STRUCTURAL_CONTEXT
- BEGIN_PROTECTED_CONTEXT
- CONCEPT_PACKAGE bodies

Protected bodies stay outside the model and are restored mechanically.

### Model
- `src.loader.load_model(writer_config_path)` once per process
- `create_chat_completion(messages, max_tokens, temperature, top_p)` with numeric types
- Empty choices / empty content → GENERATION_FAILED → STOP (no partial FINAL)

### Cache (pilot exception vs v3.2.2)
CACHE_BEFORE for block k>0 = restored prose of block k-1 from **this run** (or prior-run restored.md when resuming).
Not human-accepted canonical.

### Slots (pilot exception vs v3.2.2)
1. Persist `raw_output.md` before checks.
2. If found slots == expected → use as-is.
3. If expected non-empty and found empty → **append** missing tokens in order (logged recovery).
4. Any other mismatch → PROTECTED_MATERIAL_VIOLATION → STOP.
5. Restore exact protected bodies from parsed SOURCE spans.

This recovery is PILOT. v3.2.2 target remains: missing slot = violation without auto-repair.

### Context window
Estimate tokens (pilot: ~chars/4) of SYSTEM+USER vs `model.n_ctx`.
Overflow → `SEGMENTATION_TOO_LARGE_FOR_CURRENT_WRITER_CONFIGURATION`.
No truncation, no auto-split, no dropping cache.

---

## 6. Assembly (pilot)

Order:
1. SOURCE prefix before first marker (required; **not in snapshot runner**)
2. For each marker in SOURCE order: rebuilt interval =
   - STRUCTURAL_HEADING texts from the block interval
   - restored rewritable stream
   - guaranteed newline before an ATX heading if previous chunk lacks `\n` (**not in snapshot runner**)
3. Concatenate → `Output/FINAL.manuscript.md` only if every marker succeeded

No FINAL on first hard failure.

---

## 7. Output sanitation (hardening required; not in snapshot)

After raw model text, before restore, reject or strip:
- payload delimiters `BEGIN_*` / `END_*` belonging to the runtime grammar (esp. `END_LOCAL_TRANSFORMATION`)
- control phrases leaked from PROMPT_MAP (e.g. `OPEN SOURCE DECISION`)
- explicit placeholders of the class `[To be specified based on SOURCE analysis]`

Optional FLAG (not global literary detector):
- CURRENT_SOURCE had no markdown table AND raw output contains a markdown table → FLAG/STOP that marker

---

## 8. Evidence (pilot)

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

## 9. Failure codes used by pilot

```yaml
SOURCE_PROMPT_MAP_MISMATCH
MARKER_GRAPH_INVALID
PROTECTED_MARKUP_INVALID
PROTECTED_MATERIAL_VIOLATION
SEGMENTATION_TOO_LARGE_FOR_CURRENT_WRITER_CONFIGURATION
GENERATION_FAILED
```

v3.2.2 codes REVISION_CHANGED, COMMIT_CONFLICT, CACHE_INTEGRITY_FAILURE (canonical), CONTROL_RESPONSE_PRESENT, CONTEXT_CONFLICT remain target-only unless later implemented.

---

## 10. Explicit non-goals of current execution

- No PRODUCTION_REVISION freeze
- No STABLE_CONFIG runtime
- No human ACCEPT/REJECT machine
- No commit ledger
- No resident Llama literary memory
- No CONCEPT_PACKAGE / paired half-chapters / generated handoff
- No automatic SOURCE or PROMPT_MAP editing
- No publication-ready guarantee
- No inference during reconstruct on E:\

---

## 11. Relation to v3.2.2

Keep v3.2.2 text as historical target file in the repo (`SPEC_v3.2.2.md` or unchanged archived copy). Do not implement freeze/commit as part of clean restore.

Promotion from Layer P to Layer T is a **separate Shogun architecture decision**, not part of disk reconstruction.

---

## 12. First-run evidence that binds hardening

From FINAL of the lost-D: full run (Prompter review):
- ENGINE: SUCCESS
- PROTECTED CORE: MOSTLY SUCCESS
- Missing pre-marker prefix and heading glue: runner
- Control-delimiter and invented tables / excerpt-commentary: Gemma + missing output guard
- Editorial queries that survived: inherited SOURCE
