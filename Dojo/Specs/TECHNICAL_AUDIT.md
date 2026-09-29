# TECHNICAL_AUDIT — MANUSCRIPT_PRESS
Date: 2026-09-29
Source snapshot: github.com/universes-lab/Laboratory / Dojo/Manuscript_Press @ main
Target ROOT: E:\Gemini\Dojo\Manuscript_Press
Mode: READ-ONLY audit. No inference. No Samurai prompt.

---

## 1. Verdict in one paragraph

The GitHub snapshot is a **mixed working tree**: a proven **PILOT production runner** plus reusable parsers/loader, sitting on top of a large amount of **legacy Dojo / bench / paired-run debris** and a **target SPEC v3.2.2 that the runner does not implement**. After disk loss, restore the **pilot engine + production inputs + Gemma kernel + writer_config**, archive historical Output and Samurai control files, and treat SPEC v3.2.2 as **target architecture**, not as the current execution contract.

STATUS: **RECONSTRUCT_AS_PILOT — HARDENING PENDING**
CAN_REUSE_SPEC_V3_2_2_AS_TARGET: yes
CAN_REUSE_SPEC_V3_2_2_AS_CURRENT_EXECUTION: no
PRODUCTION_INFERENCE: forbidden until Shogun GREEN on the new ROOT

---

## 2. What the snapshot actually contains

### Canonical / keep
- `src/production_runner.py` (18439 B) — current pilot entrypoint
- `src/parser/protected_span_parser.py`
- `src/parser/source_parser.py`
- `src/parser/prompt_map_parser.py`
- `src/parser/source_prompt_map_validator.py`
- `src/parser/atx_heading_extractor.py` (exists; **not wired** into runner)
- `src/parser/__init__.py`
- `src/loader.py`
- `src/__init__.py`
- `Gemma.md`
- `Input/SOURCE_MANUSCRIPT.md` (214982 B)
- `Input/PROMPT_MAP.yaml` (857403 B)
- `config/writer_config.yaml`
- `templates/` (editorial templates; not runtime)

### Launchers
- `run_manuscript_press.bat` — intended clean launcher (must be rewritten for E:\ and `python -m src.production_runner` only)
- `manuscript_press.bat` — **historical resume command** for run `20260923T144611Z` / `MP:0170` — **NOT default**

### Target / stale control docs
- `SPEC.md` — ENGINEERING SPEC v3.2.2 **target** (freeze, commit, STABLE_CONFIG, source/, work/revisions/)
- `STEP.md` — old Samurai PILOT_PRODUCTION_RUNNER / Dojo operational STEP
- `Current_Prompt.md` — old Samurai operational frame
- `GEMINI.md` — old Dojo root `D:\Gemini\dojo`
- `README.md` — book/multigenre philosophy; **does not describe the engine**

### Legacy code (do not use as production path)
- `src/builder.py`, `src/generator.py` — CONCEPT_PACKAGE / old Manuscript Writer
- `src/smoke_bridge.py`, `src/continuity_cache_bench.py`, `src/test_inference.py`
- `src/parser.py`, `src/prompt_map_parser.py`, `src/protected_span_parser.py` (root duplicates of parser package)
- `src/atx_heading_extractor.py`, `src/authority_freeze.py`, `src/revision_validator.py`, `src/core/authority_freeze.py` — Phase-1 SPEC machinery, **not used by production_runner**

### Historical evidence
- `Output/Old/*` — smoke/continuity/old 01_T00 artifacts
- No `Output/FINAL.manuscript.md` in this snapshot
- No `Output/runs/20260923T144611Z/` in this snapshot
- Resume prior-run directory from D: is **gone unless separately archived by Shogun**

### Git hygiene
- `.gitignore`, `dojo_git.bat`, `git_tools/` — keep as project tools; they are Dojo-era and must not define production invocation

---

## 3. SPEC v3.2.2 vs actual `production_runner.py`

| SPEC v3.2.2 requirement | In runner? | Classification |
|-------------------------|------------|----------------|
| One MP block = one Gemma call | YES | CANONICAL (pilot) |
| Markers `<!-- MP:XXXX -->` | YES | CANONICAL |
| Protected spans → `⟦MP_PROTECTED:ID⟧` | YES | CANONICAL |
| PromptMap LONG_RANGE + LOCAL | YES | CANONICAL |
| SOURCE↔PROMPT_MAP exact ID set | YES | CANONICAL |
| Gemma.md as SYSTEM kernel | YES | CANONICAL |
| writer_config numeric knobs | YES (nested `model`/`generation`) | CANONICAL (schema ≠ SPEC flat example) |
| CACHE_BEFORE from previous block | YES, auto from previous **generated** restored prose | PILOT (SPEC: accepted canonical only) |
| ATX headings excluded from CURRENT_SOURCE and rebuilt | YES (local rebuild) | PILOT (SPEC: restore from frozen SOURCE at assembly) |
| `--preflight-only` | YES | PILOT operational |
| `--start-marker` / `--prior-run-dir` | YES | RECOVERY / not default |
| `normalize_slots` append if model dropped all slots | YES | PILOT EXCEPTION (SPEC: missing slot = VIOLATION / STOP) |
| Input from `Input/` | YES | PILOT (SPEC: `source/` + frozen `work/revisions/`) |
| Output `Output/FINAL.manuscript.md` | YES | PILOT (SPEC: `assembly/final_manuscript.md` after all commits) |
| PRODUCTION_REVISION freeze + hashes | NO | TARGET only |
| STABLE_CONFIG file + SYSTEM section | NO | TARGET only |
| BEGIN_STRUCTURAL_CONTEXT / BEGIN_PROTECTED_CONTEXT in USER | NO (explicitly forbidden in runner) | PILOT lock (Doctor/Grok) |
| Human REJECT / ACCEPT_AS_IS / ACCEPT_PATCHED | NO | TARGET only |
| commit ledger / state.yaml / resume-from-commit | NO | TARGET only |
| CONTROL_RESPONSE `<<QUERY:>>` gate | NO | MISSING vs SPEC; also missing **delimiter strip** vs first-run evidence |
| Pre-marker SOURCE prefix in FINAL | NO | HARDENING REQUIRED (exposed by first full run) |
| Newline before reinserted ATX heading | NO | HARDENING REQUIRED |
| §18 exact token count | NO — char/4 estimate | PILOT approximation |
| max_tokens 3500 as SPEC example | NO — config has 2048 | CONFIG fact; not silently change |

Conclusion: **v3.2.2 remains the frozen target.** Current executable architecture is **PILOT_EXECUTION_PROFILE**. Do not pretend the snapshot is a v3.2.2 implementation.

---

## 4. Last approved technical route vs snapshot

Approved route after first full run:
1. Engine SUCCESS (full marker traversal happened on lost D:).
2. PUBLICATION RETURN.
3. Required hardening (not in this snapshot’s runner):
   - copy SOURCE prefix before first marker into FINAL
   - whitespace-safe heading reinsertion
   - strip/fail on payload delimiters and control phrases
   - optional FLAG if markdown table appears where CURRENT_SOURCE had none

Snapshot runner has resume + slot-drop recovery, **does not** contain the three mechanical hardening fixes.

---

## 5. Decisions locked by this audit

1. Clean project = PILOT engine, not v3.2.2 freeze machine.
2. Default invocation = `python -m src.production_runner` or `run_manuscript_press.bat` **without** `--start-marker`.
3. `manuscript_press.bat` = archive or delete from clean ROOT.
4. `Output/Old/` = archive only.
5. Old `GEMINI.md` / `Current_Prompt.md` / `STEP.md` = **not** operational on E:\ (Doctor/Sensei rewrite later). Audit does not rewrite them.
6. `writer_config.yaml` model path still says `D:/Gemini/models/...` — **must be updated on E:\** by Shogun/Sensei to the real new model path. Unknown here.
7. No production inference during reconstruct.
8. Slot-append recovery stays PILOT-only and must be logged; it is not a silent product rule of v3.2.2.
9. Duplicate parser files at `src/*.py` (non-package) are STALE relative to `src/parser/`.
