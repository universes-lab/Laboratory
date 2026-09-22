**MANUSCRIPT_PRESS_FINAL_ROUTE_DECISION**
---
### STATUS
**READY_FOR_FINAL_DEEPSEEK_STEP**
Один implementation STEP под существующим SPEC v3.2.2.  
Дополнительный «penultimate» gate не требуется: production inputs на месте, proven path известен, gap = отсутствие full-manuscript runner.
---
### PHYSICAL_STATE
**Inputs (opaque; content not read)**
| File | Present | Size (bytes) |
|------|---------|--------------|
| `Input/SOURCE_MANUSCRIPT.md` | yes | 214 982 |
| `Input/PROMPT_MAP.yaml` | yes | 857 403 |
| `Input/TEST_SOURCE_MANUSCRIPT.md` | still present (fixture) | 1 270 |
| `Input/TEST_PROMPT_MAP.yaml` | still present (fixture) | 4 831 |
Production pair **exists and is non-empty**. Do not substitute TEST_*.
**Active entrypoint state**
| Component | State |
|-----------|--------|
| Proven generation path | `smoke_bridge.py` / `continuity_cache_bench.py` + `src/parser/*` + `loader.py` + `create_chat_completion` |
| Hardcoded paths in benches | still `Input/TEST_*` |
| `run_manuscript_press.bat` | **STALE** → `src.paired_runner` (**absent**, must not be resurrected) |
| Full-manuscript production runner | **absent** |
| `Gemma.md` | present (root) |
| `config/writer_config.yaml` | present (live knobs) |
| `config/WRITER_CONFIG.yaml` | absent (SPEC name only) |
| `source/STABLE_CONFIG.yaml` | absent |
| `work/revisions/.../frozen/` | absent |
**Stale control artifacts**
- `Current_Prompt.md` / `STEP.md` — still C2 type-fix era; **not** production authority  
- `run_manuscript_press.bat` — paired-run contract  
**Proven runtime to reuse**
- `src/parser/protected_span_parser.py`  
- `src/parser/source_parser.py`  
- `src/parser/prompt_map_parser.py`  
- `src/parser/source_prompt_map_validator.py`  
- `src/parser/atx_heading_extractor.py` (structural passthrough if already wired in benches)  
- `src/loader.py`  
- call pattern: config numeric knobs → `create_chat_completion` (post C2/C3 fixes)  
- continuity rule: CACHE_BEFORE = previous block prose; omit on first marker  
**Do not resurrect**
- `paired_runner.py`  
- CONCEPT_PACKAGE / `builder.py` production path  
- legacy `generator.py` as orchestrator  
---
### SPEC_STATUS
- **v3.2.2 remains unchanged** — universal authority; new article ≠ new SPEC.  
- **No supplementary SPEC required.**  
- STEP must **honestly scope** a **pilot production runner**: implements ordered multi-block GENERATE + continuity + protected restore + final assembly; does **not** claim full freeze/commit/ACCEPT/resume runtime.
---
### LOCKED_ROUTE
**One route only: new thin production runner + truthful BAT.**
```text
Input/SOURCE_MANUSCRIPT.md
Input/PROMPT_MAP.yaml
Gemma.md
config/writer_config.yaml
        ↓
src/production_runner.py   ← NEW (canonical entrypoint)
  reuse src.parser.* + loader + proven completion call
        ↓
for each MP marker in SOURCE order:
  preflight machine contract
  protected → slotted
  assemble USER (LONG_RANGE + CACHE? + STRUCTURAL? + PROTECTED? + CURRENT + LOCAL)
  cold create_chat_completion
  restore protected → block prose
  CACHE for next = this block prose
  on any hard failure → STOP (no silent skip)
        ↓
Output/FINAL.manuscript.md   (+ per-block evidence under Output/runs/ or logs/)
        ↓
run_manuscript_press.bat → python -m src.production_runner
```
**Design locks (no choice left to Sensei):**
1. **Entrypoint:** `src/production_runner.py` (new). Benches stay diagnostic; not promoted as product CLI.  
2. **Inputs:** only `Input/SOURCE_MANUSCRIPT.md` + `Input/PROMPT_MAP.yaml` (not TEST_*, not `source/` freeze tree for this pilot).  
3. **Traversal:** exact ordered marker graph from SourceParser; one inference per marker.  
4. **PROMPT_MAP match:** validator SOURCE ↔ map keys; missing/extra key → STOP.  
5. **Continuity:** marker[0] no CACHE; marker[k>0] CACHE = verbatim previous **generated** block prose (pilot auto-chain; not interactive ACCEPT).  
6. **Protected:** existing protected-first parse; model sees slots; restore mechanically before write/assembly.  
7. **Structural:** use existing ATX extraction if benches already do; headings passthrough per existing parser behavior — no new literary logic.  
8. **Config:** `config/writer_config.yaml` only; int/float knobs at completion call.  
9. **STABLE_CONFIG:** **deferred** for first full run; SYSTEM = Gemma.md (+ short runtime override if benches already use it). Document omit in runner report.  
10. **Failure:** any preflight/parse/completion/restore failure → abort run; no skip-ahead.  
11. **Assembly:** concatenate restored block prose in marker order → `Output/FINAL.manuscript.md`.  
12. **BAT:** replace body of `run_manuscript_press.bat` to call `python -m src.production_runner` only; remove `paired_runner` / PART2 checks.  
13. **Claims:** runner banner/report must state `PILOT_PRODUCTION` / not full SPEC commit-runtime.
**Context discipline:** never inject entire PROMPT_MAP or entire SOURCE into one prompt — only current marker’s frames + current block body + cache (as in proven benches). Critical given map size ~857 KB.
---
### DEEPSEEK_ASSIGNMENT
**Formalize for Samurai: one FINAL implementation STEP under SPEC v3.2.2 only.**  
No new SPEC file. No architecture menu.
| Field | Content |
|-------|---------|
| **Technical objective** | Implement `src/production_runner.py` + fix `run_manuscript_press.bat` so one command processes **all** SOURCE markers with continuity, protected restore, and final assembly. |
| **May create/modify** | `src/production_runner.py` (new); `run_manuscript_press.bat`; optional `README` one-line invocation; under `Output/` only run artifacts |
| **Must not touch** | `Input/SOURCE_MANUSCRIPT.md`, `Input/PROMPT_MAP.yaml`, `Gemma.md` content, SPEC.md, parser package semantics, `loader.py` unless proven broken, TEST_* (leave as fixtures), no `paired_runner` |
| **Canonical entrypoint** | `python -m src.production_runner` |
| **BAT** | `run_manuscript_press.bat` → that module only |
| **Input paths** | `Input/SOURCE_MANUSCRIPT.md`, `Input/PROMPT_MAP.yaml` |
| **Output** | `Output/FINAL.manuscript.md` + per-run log + per-block prose/payload evidence (path scheme defined in STEP) |
| **Reuse** | `src.parser.*`, `src.loader`, numeric config→completion pattern from fixed continuity bench |
| **Do not resurrect** | paired_runner, CONCEPT builder path, generator-as-orchestrator |
| **Preflight** | files exist non-empty; encoding utf-8; protected parse; marker graph unique ordered; SOURCE↔MAP validate; writer_config knobs numeric |
| **Acceptance tests** | (1) dry preflight on production inputs without model optional if STEP splits phases; (2) full run produces FINAL + N block outputs for N markers; (3) protected slots restored; (4) no TEST_* paths in runner; (5) BAT points to production_runner; (6) failure injection or documented STOP on first real error class |
| **Runtime evidence** | run log with marker list, per-marker PASS/FAIL, completion counts, FINAL path/size |
| **STOP conditions** | missing input; validate fail; completion error; empty block output; protected restore mismatch |
| **Implementation complete when** | BAT + runner exist; one successful or honestly failed full attempt on **production** inputs with evidence pack; FINAL written iff all markers succeeded |
Sensei owns STEP wording; must not invent freeze/commit/ACCEPT UI.
---
### SAMURAI_ACCEPTANCE
Objective evidence before ACCEPT implementation:
1. `src/production_runner.py` exists; greppable paths = production Input names only.  
2. `run_manuscript_press.bat` contains `production_runner`, zero `paired_runner`.  
3. `python -m py_compile src/production_runner.py` PASS.  
4. Preflight report on production inputs: marker count ≥ 1, validate PASS (or honest FAIL).  
5. After authorized full run: either  
   - `Output/FINAL.manuscript.md` non-empty **and** completion_calls == marker_count, **or**  
   - honest STOP with log naming failing marker (not silent partial FINAL).  
6. No edit timestamps on SOURCE/PROMPT_MAP from Samurai.
---
### FIRST_FULL_RUN
| Item | Value |
|------|--------|
| **Invocation** | from project root: `run_manuscript_press.bat` **or** `python -m src.production_runner` |
| **Expected final output** | `Output/FINAL.manuscript.md` |
| **Evidence** | run log; per-block outputs; FINAL size; `CREATE_CHAT_COMPLETION_CALLS` == number of MP markers processed |
Author/Shogun authorizes the long run after implementation ACCEPT (model time will be substantial).
---
### DEFERRED_HARDENING (explicit)
| Facility | First full run |
|----------|----------------|
| STABLE_CONFIG | **deferred** |
| PRODUCTION_REVISION freeze | **deferred** |
| Commit ledger | **deferred** |
| Interactive ACCEPT / REJECT | **deferred** (pilot uses auto continuity chain) |
| Resume / recovery | **deferred** |
| State reconstruction | **deferred** |
| Deterministic restart mid-manuscript | **deferred** |
| Full revision isolation | **deferred** |
| `config/WRITER_CONFIG.yaml` rename | **deferred** (use existing `writer_config.yaml`) |
| Removing TEST_* fixtures | optional cleanup, not required for run |
| Root parser duplicates cleanup | **deferred** (runner must import `src.parser.*` only) |
---
### MIGRATION_GATE — DOJO_COMPLETE / MIGRATION_READY
All of:
1. Final STEP implemented and accepted on evidence above.  
2. At least one **full** production invocation completed with `FINAL.manuscript.md` (or documented Author-accepted STOP with partial policy — default: full success required for migration).  
3. BAT + README/invocation truthful (PILOT_PRODUCTION scope stated).  
4. `Current_Prompt.md` / `STEP.md` no longer claim active C2; idle or migration-hold.  
5. No dependency on reconstructing chat history to run again.  
**One optional post-run hardening STEP before migration** (only if full run exposes it): context-window / batching if n_ctx overflows on real blocks — identify from evidence, not pre-built. Otherwise **no** mandatory extra STEP.
---
### NEXT_OWNER
**DeepSeek / Coding Sensei**
Formalize the FINAL Samurai STEP from this locked route.  
Then: Grok sign-off STEP → Doctor Current_Prompt → Shogun authorizes Samurai execution / long run.
---
**STOP.**  
No code. Content of SOURCE/PROMPT_MAP not read. SPEC not rewritten.
===
===
===
**MANUSCRIPT_PRESS_FINAL_ROUTE_AUTHORITY_DELTA**
```text
STATUS: LOCKED
EXECUTION_MODEL: PILOT_PROFILE
```
---
### SPEC_V3_2_2_STATUS
**Unchanged.**  
SPEC v3.2.2 remains **target system architecture authority**.  
It is **not** fully implemented by the first production runner and must **not** be claimed as fully implemented.
---
### CURRENT_EXECUTION_AUTHORITY
For the **first full article run only**:
1. **SPEC v3.2.2** — target architecture (what the system is becoming).  
2. **PILOT_EXECUTION_PROFILE** (this delta) — **temporary Author-authorized execution subset** for the first complete pass.
DeepSeek STEP must cite **both**.  
Pilot profile does **not** amend SPEC text.
---
### TEMPORARILY_DEFERRED_SPEC_REQUIREMENTS
Исчерпывающий список норм SPEC v3.2.2, которые **первый** pilot runner **не** исполняет:
- PRODUCTION_REVISION freeze / frozen authority tree  
- STABLE_CONFIG as SYSTEM authority domain  
- Human REJECT / ACCEPT_AS_IS / ACCEPT_PATCHED  
- Canonical COMMIT_RECORD / commit ledger  
- Cache sourced **only** from human-accepted canonical output  
- Commit-chain / state reconstruction / resume  
- Final assembly **only after** all markers committed under commit protocol  
- SPEC §19 path `assembly/final_manuscript.md` as normative location  
- Full revision isolation  
---
### NON_DEFERABLE_SPEC_REQUIREMENTS
Для pilot runner **обязательны**:
- Ordered marker traversal from SOURCE  
- SOURCE ↔ PROMPT_MAP correspondence (machine validate)  
- Protected-first parse; slots to model; mechanical restore before persist/assembly  
- Per-marker USER assembly from typed sections actually used (see below)  
- Cold `create_chat_completion` with numeric knobs from `config/writer_config.yaml`  
- **§18 context-window validation before every generation:**  
  - estimate actual system+user tokens vs `n_ctx`  
  - on overflow → `SEGMENTATION_TOO_LARGE_FOR_CURRENT_WRITER_CONFIGURATION`  
  - **STOP**  
  - **no** truncation, **no** auto-split, **no** batching around an oversized marker  
- Hard STOP on preflight/completion/restore failure (no silent skip)  
- Truthful reporting: `PILOT_EXECUTION_PROFILE`, not “full SPEC runtime”
---
### CACHE_POLICY
```text
Pilot only:
  marker[0]: no CONTINUITY_CACHE section
  marker[k>0]: CACHE_BEFORE = verbatim prose of immediately previous
               successfully generated block in this same run
```
This is **not** SPEC “cache from accepted commit.”  
It is an explicit pilot exception: **auto-chain on successful generation within one run.**
---
### CONTEXT_WINDOW_POLICY
```text
Before each create_chat_completion:
  validate context size against n_ctx from writer_config
  overflow → SEGMENTATION_TOO_LARGE_FOR_CURRENT_WRITER_CONFIGURATION → STOP
  no truncation / no auto-split / no batching
```
Migration note about “batching if n_ctx overflows” — **removed** as incompatible with SPEC.
---
### STRUCTURAL_PASSTHROUGH_IMPLEMENTATION
**Locked from proven benches (physical):**
- `src/smoke_bridge.py` and `src/continuity_cache_bench.py` **do not** emit `BEGIN_STRUCTURAL_CONTEXT`.  
- They **reject** USER payloads containing `BEGIN_STRUCTURAL_CONTEXT`.  
- `src/parser/atx_heading_extractor.py` **exists** but is **not** on the proven generation path.
**Pilot production_runner:**
```text
Do NOT emit STRUCTURAL_CONTEXT in USER payload.
Do NOT call atx_heading_extractor for USER assembly in this pilot.
Structural headings that fall inside CURRENT_SOURCE body remain ordinary source text.
```
No “if already wired.”
---
### RUNTIME_OVERRIDE_POLICY
**Used.** Source: exact block already in proven benches (`continuity_cache_bench.py` / `smoke_bridge.py`).
Pilot `production_runner` **must** place the same SYSTEM adjunct after `BEGIN_GEMMA_KERNEL`…`END_GEMMA_KERNEL`:
```text
BEGIN_RUNTIME_CONTRACT_OVERRIDE
For this diagnostic run, treat the legacy Concept Package / Package Prompt
wording in the Gemma kernel as superseded by the structured USER message.
The authorities for this inference are only the USER sections actually present:
LONG_RANGE_FRAME,
CONTINUITY_CACHE,
CURRENT_SOURCE,
LOCAL_TRANSFORMATION,
and any STRUCTURAL_CONTEXT, PROTECTED_CONTEXT, or CONTINUITY_CACHE section
when such a section is present.
Do not invent substantive material beyond those supplied authorities.
Do not require a legacy Concept Package or Package Prompt.
END_RUNTIME_CONTRACT_OVERRIDE
```
(Wording may substitute “diagnostic” → “pilot production” in the first line only; body authorities list unchanged.)  
STABLE_CONFIG still **not** emitted.
**USER sections for pilot (emit only when applicable):**
- LONG_RANGE_FRAME (required per marker)  
- CONTINUITY_CACHE (markers after first, per CACHE_POLICY)  
- CURRENT_SOURCE (required)  
- LOCAL_TRANSFORMATION (required)  
- PROTECTED_CONTEXT: only if current block has protected slots **and** proven bench pattern supplies a separate protected context; if benches omit separate PROTECTED_CONTEXT and only slot CURRENT_SOURCE, **match benches** (slots inside CURRENT_SOURCE only).
---
### PILOT_OUTPUT_PATH_STATUS
```text
Output/FINAL.manuscript.md
```
= **pilot output path only**.  
**Not** an implementation of SPEC §19 `assembly/final_manuscript.md`.  
Report must not call it canonical SPEC assembly output.
---
### DEEPSEEK_MAY_NOW_WRITE_FINAL_STEP
**yes**
STEP must reference:
1. SPEC v3.2.2 — target architecture  
2. This **PILOT_EXECUTION_PROFILE** — current execution authority for first full run  
No architecture menu. No implicit SPEC compliance claim.
---
### NEXT_OWNER
**DeepSeek**
---
**STOP.**
===
===
===
**MANUSCRIPT_PRESS_ROUTE_DELTA_2**
```text
STATUS: LOCKED
```
---
### STRUCTURAL_PASSTHROUGH_POLICY
ATX headings (`#`…`######`) that appear **outside protected spans** are **not** rewritable literary material.
For the pilot full run they must:
- be **excluded** from the rewritable body sent to Gemma as ordinary prose;  
- **not** be alterable by the model;  
- be **reinserted at exact SOURCE positions** in pilot final assembly.
This requirement is **not deferred**.
---
### STRUCTURAL_IMPLEMENTATION
**Ownership: `src/production_runner.py` (NEW required logic), using proven extract helpers where useful.**
Exact algorithm (locked):
1. After protected-first parse → `SLOTTED_SOURCE`.  
2. On `SLOTTED_SOURCE`, identify ATX headings **outside** protected slot tokens (reuse detection logic from `src/parser/atx_heading_extractor.py` if it already classifies ATX + respects protected spans; **wiring and orchestration are production_runner’s**, not “bench proven path”).  
3. For each production marker interval (marker → next marker / EOF):  
   - Split interval into ordered segments: `REWRITABLE` | `STRUCTURAL_HEADING` | …  
   - `CURRENT_SOURCE` sent to Gemma = **only concatenated REWRITABLE segments** (with protected **slots** already in place).  
   - Persist a per-marker **structure map**: ordered list of `{type: heading|prose_slot, text_or_ref}` so assembly can rebuild the interval.  
4. Gemma never receives heading lines as free prose in `CURRENT_SOURCE`.  
5. After validated model output for that marker’s rewritable span(s):  
   - Rebuild marker interval = interleave **exact SOURCE heading text** with model prose for rewritable spans (and later protected restore).  
6. Pilot `Output/FINAL.manuscript.md` = concatenation of rebuilt intervals in marker order.
**Not used:** “headings stay inside CURRENT_SOURCE as ordinary text.”  
**Not used:** emit `BEGIN_STRUCTURAL_CONTEXT` to Gemma (benches forbid it; pilot stays consistent—structure is enforced by **extraction + assembly**, not by a USER structural section).
---
### PROTECTED_SLOT_PARSER_STATUS
**PROVEN_REUSED**
- `ProtectedSpanParser` / protected-first parse  
- protected body → slot token in `SLOTTED_SOURCE`
---
### PROTECTED_RESTORATION_STATUS
**NEW_REQUIRED** (`production_runner`)
Proven benches do **not** validate slots post-inference and do **not** mechanically restore protected bodies. Pilot must add both.
---
### PROTECTED_CONTEXT_POLICY
**OMITTED**
Align with proven benches: **no** `BEGIN_PROTECTED_CONTEXT` in USER.
```text
Gemma receives only slot tokens inside CURRENT_SOURCE (rewritable segments).
Exact protected bodies stay outside model input and are restored mechanically
after validated output.
```
---
### PROTECTED_SLOT_VALIDATION
Before restore, on model output for the block:
- every expected slot ID appears **exactly once**  
- no missing slots  
- no duplicate slots  
- no unknown slots  
- slot IDs unchanged  
- expected order preserved  
**PASS** → mechanical restore from parsed protected material into the rebuilt interval.  
**FAIL** → `PROTECTED_MATERIAL_VIOLATION` → **STOP** → **no** partial `FINAL.manuscript.md`.
---
### CONTEXT_VALIDATION_STATUS
**NEW_REQUIRED** (`production_runner`)
Proven benches do **not** implement §18 token/context checks.
Before each `create_chat_completion`:
- compute actual system+user context size vs `n_ctx` from `writer_config`  
- overflow → `SEGMENTATION_TOO_LARGE_FOR_CURRENT_WRITER_CONFIGURATION` → **STOP**  
- no truncation / no auto-split / no batching  
---
### DEEPSEEK_MAY_WRITE_FINAL_STEP
**yes**
STEP cites: SPEC v3.2.2 (target) + PILOT_EXECUTION_PROFILE + this delta (structural / protected restore / §18 as NEW_REQUIRED).
---
### NEXT_OWNER
**DeepSeek**
---
**STOP.**
