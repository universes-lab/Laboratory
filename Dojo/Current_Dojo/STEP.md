# STEP.md — MANUSCRIPT_PRESS PHASE 1 / PILOT PRODUCTION RUNNER

```yaml
IDENTITY:
  Project: MANUSCRIPT_PRESS
  Phase: 1
  Step: PILOT_PRODUCTION_RUNNER
  Version: 1.0
  Status: CANDIDATE — READY FOR GROK REVIEW
  Date: 2026-09-19
  Step Type: PILOT_IMPLEMENTATION

  Technical Authority:
    - SPEC v3.2.2 — target system architecture (universal authority)
    - PILOT_EXECUTION_PROFILE (FINAL_ROUTE_AUTHORITY_DELTA) — current execution authority for first full run
    - ROUTE_DELTA_2 — structural passthrough / protected restore / §18 context validation (NEW_REQUIRED)
    - FINAL_ROUTE_DECISION — locked route, single canonical entrypoint

  Scope Claim: PILOT_PRODUCTION — NOT full SPEC runtime.
  Implementation MUST NOT claim full SPEC compliance.
```

---

## OBJECTIVE

Реализовать тонкий **pilot production runner**, который одним вызовом обрабатывает **все** MP-маркеры из `Input/SOURCE_MANUSCRIPT.md` в порядке SOURCE, с continuity, protected restore, structural passthrough и финальной сборкой в `Output/FINAL.manuscript.md`.

---

## CANONICAL INPUTS

```yaml
inputs:
  source: Input/SOURCE_MANUSCRIPT.md
  prompt_map: Input/PROMPT_MAP.yaml
  gemma_kernel: Gemma.md
  writer_config: config/writer_config.yaml
```

**Запрещено:**
- Использовать `Input/TEST_SOURCE_MANUSCRIPT.md` или `Input/TEST_PROMPT_MAP.yaml`
- Использовать `source/` freeze tree для этого pilot
- Читать содержимое SOURCE / PROMPT_MAP вручную — только через рантайм-парсеры

**Context discipline:** никогда не инжектить весь PROMPT_MAP (~857 KB) или весь SOURCE в один prompt. Только:
- текущий marker: LONG_RANGE_FRAME + LOCAL_TRANSFORMATION
- текущий блок: CURRENT_SOURCE (rewritable segments + slots)
- CACHE_BEFORE (для marker[k>0])

---

## PROVEN RUNTIME TO REUSE

```yaml
reuse:
  parsers:
    - src/parser/protected_span_parser.py
    - src/parser/source_parser.py
    - src/parser/prompt_map_parser.py
    - src/parser/source_prompt_map_validator.py
    - src/parser/atx_heading_extractor.py  # только для detection логики, не для USER assembly
  loader:
    - src/loader.py
  completion_pattern:
    - numeric knobs (int/float) из writer_config
    - llm.create_chat_completion(messages=[system, user], max_tokens, temperature, top_p)
```

**Не воскрешать:**
- `paired_runner.py`
- `builder.py` / CONCEPT_PACKAGE production path
- `generator.py` как orchestrator

---

## ALLOWED WORKING FILES

**Создать:**
- `src/production_runner.py` (новый canonical entrypoint)
- `Output/runs/<timestamp>/` — per-run evidence (payload, blocks, log)

**Изменить:**
- `run_manuscript_press.bat` — заменить тело на вызов `python -m src.production_runner`

**Создать (финальный артефакт):**
- `Output/FINAL.manuscript.md`

**Не трогать:**
- `Input/SOURCE_MANUSCRIPT.md`
- `Input/PROMPT_MAP.yaml`
- `Input/TEST_*` (оставить как fixtures)
- `Gemma.md` content
- `SPEC.md`
- `src/parser/*` semantics
- `src/loader.py` (если не доказано, что сломан)
- `config/writer_config.yaml` (только чтение)

---

## DESIGN LOCKS (уже зафиксированы, не пересматриваются)

```yaml
locked_design:
  entrypoint: src/production_runner.py
  invocation: python -m src.production_runner
  bat: run_manuscript_press.bat → production_runner only

  traversal: exact ordered marker graph from SourceParser; one inference per marker
  prompt_map_match: validator SOURCE ↔ map keys; missing/extra key → STOP
  continuity:
    marker[0]: no CONTINUITY_CACHE
    marker[k>0]: CACHE_BEFORE = verbatim prose предыдущего успешно сгенерированного блока в этом же run
    (pilot exception: auto-chain on successful generation, НЕ interactive ACCEPT)
  protected: существующий protected-first parse; слоты модели; механический restore перед persist/assembly
  structural: см. STRUCTURAL_PASSTHROUGH_ALGORITHM ниже
  config: config/writer_config.yaml only; int/float knobs at completion call
  stable_config: OMITTED for pilot; документировать в runner report
  failure: любой preflight/parse/completion/restore failure → STOP; no skip-ahead
  assembly: concatenate rebuilt intervals in marker order → Output/FINAL.manuscript.md
  claims: PILOT_PRODUCTION / not full SPEC commit-runtime
```

---

## FROZEN SPEC BEHAVIOR — AUTHORITATIVE (активировано в pilot)

Из SPEC v3.2.2:

- §1: ONE TRANSACTION = ONE PRODUCTION MARKER BLOCK
- §3: SOURCE / PROMPT_MAP marker semantics; execution order из SOURCE
- §4: protected-first parse; SLOTTED_SOURCE; механический restore
- §8: context assembly (SYSTEM + USER section grammar) — **в pilot: STRUCTURAL_CONTEXT / PROTECTED_CONTEXT / STABLE_CONFIG не эмитятся** (см. PILOT EXCEPTIONS)
- §11: structural passthrough — ATX headings восстанавливаются из SOURCE (см. DELTA_2)
- §18: context-window validation → `SEGMENTATION_TOO_LARGE_FOR_CURRENT_WRITER_CONFIGURATION` → STOP
- §20: failure taxonomy (использовать только существующие коды)

---

## PILOT EXCEPTIONS (явно, в пределах PILOT_PROFILE)

```yaml
pilot_exceptions:
  cache:
    pilot: verbatim prose предыдущего успешного блока в этом же run
    not: SPEC "cache from accepted commit"
  stable_config:
    pilot: omitted; документировать как deferred
  structural_context_section:
    pilot: не эмитить BEGIN_STRUCTURAL_CONTEXT в USER
    reason: proven benches reject it; structure enforced by extraction + assembly
  protected_context_section:
    pilot: не эмитить BEGIN_PROTECTED_CONTEXT
    reason: слоты внутри CURRENT_SOURCE; restore механический
  output_path:
    pilot: Output/FINAL.manuscript.md
    not: SPEC §19 assembly/final_manuscript.md (canonical SPEC assembly)
  acceptance:
    pilot: auto-chain on successful generation; НЕ interactive ACCEPT/REJECT
```

---

## USER PAYLOAD GRAMMAR (PILOT)

```text
BEGIN_LONG_RANGE_FRAME
<per-marker LONG_RANGE_FRAME>
END_LONG_RANGE_FRAME

[marker[k>0] only:]
BEGIN_CONTINUITY_CACHE
<CACHE_BEFORE = verbatim prose предыдущего блока>
END_CONTINUITY_CACHE

BEGIN_CURRENT_SOURCE
<CURRENT_SOURCE = только concatenated REWRITABLE segments; protected slots вставлены как slot tokens>
END_CURRENT_SOURCE

BEGIN_LOCAL_TRANSFORMATION
<per-marker LOCAL_TRANSFORMATION>
END_LOCAL_TRANSFORMATION
```

**Запрещено эмитить:**
- `BEGIN_STRUCTURAL_CONTEXT`
- `BEGIN_PROTECTED_CONTEXT`
- `BEGIN_STABLE_CONFIG`

---

## SYSTEM PAYLOAD (PILOT)

```text
BEGIN_GEMMA_KERNEL
<exact Gemma.md content>
END_GEMMA_KERNEL

BEGIN_RUNTIME_CONTRACT_OVERRIDE
For this pilot production run, treat the legacy Concept Package / Package Prompt
wording in the Gemma kernel as superseded by the structured USER message.

The authorities for this inference are only the USER sections actually present:
LONG_RANGE_FRAME,
CONTINUITY_CACHE,
CURRENT_SOURCE,
LOCAL_TRANSFORMATION.

Do not invent substantive material beyond those supplied authorities.
Do not require a legacy Concept Package or Package Prompt.
END_RUNTIME_CONTRACT_OVERRIDE
```

(STABLE_CONFIG не эмитится.)

---

## STRUCTURAL_PASSTHROUGH_ALGORITHM (DELTA_2 — LOCKED)

**Ownership:** `src/production_runner.py`. Использовать detection-логику из `src/parser/atx_heading_extractor.py`; wiring и orchestration — на runner.

### Алгоритм

1. После protected-first parse → `SLOTTED_SOURCE`.
2. На `SLOTTED_SOURCE` идентифицировать ATX headings **вне** protected slot tokens. Detection — reuse из `atx_heading_extractor.py`, если он корректно классифицирует ATX и уважает protected spans; иначе — эквивалентная логика в runner.
3. Для каждого production marker interval (marker → следующий marker / EOF):
   - Разбить интервал на ordered segments: `REWRITABLE` | `STRUCTURAL_HEADING`.
   - `CURRENT_SOURCE` для Gemma = **только concatenated REWRITABLE segments** (protected slots уже внутри).
   - Persist per-marker **structure map**: ordered list `{type: heading|prose_slot, text_or_ref}`.
4. Gemma **никогда** не получает heading lines как free prose в `CURRENT_SOURCE`.
5. После validated model output для rewritable span(s):
   - Rebuild marker interval = interleave **exact SOURCE heading text** с model prose для rewritable spans (затем protected restore).
6. `Output/FINAL.manuscript.md` = concatenation rebuilt intervals в marker order.

**Не использовать:**
- «headings остаются внутри CURRENT_SOURCE как ordinary text»
- эмиссию `BEGIN_STRUCTURAL_CONTEXT` в Gemma

---

## PROTECTED PIPELINE (DELTA_2 — LOCKED)

```yaml
protected_pipeline:
  parse:
    - ProtectedSpanParser → protected_spans + SLOTTED_SOURCE
    - protected body → slot token ⟦MP_PROTECTED:PXX_YY⟧
  model_input:
    - Gemma видит только slot tokens внутри CURRENT_SOURCE (rewritable segments)
  post_inference_validation:
    - каждый expected slot ID встречается РОВНО один раз
    - нет missing slots
    - нет duplicate slots
    - нет unknown slots
    - slot IDs не мутированы
    - expected order сохранён
    - FAIL → PROTECTED_MATERIAL_VIOLATION → STOP → no partial FINAL
  restore:
    - механическое восстановление exact frozen protected bodies
    - до write/assembly
```

`BEGIN_PROTECTED_CONTEXT` в USER **не эмитится** (align with proven benches).

---

## CONTEXT-WINDOW VALIDATION (§18 — NEW_REQUIRED)

Перед **каждым** `create_chat_completion`:

1. Вычислить фактический размер system+user контекста.
2. Сравнить с `n_ctx` из `config/writer_config.yaml`.
3. При overflow → `SEGMENTATION_TOO_LARGE_FOR_CURRENT_WRITER_CONFIGURATION` → **STOP**.
4. **No** truncation. **No** auto-split. **No** batching. **No** drop CACHE/config.

---

## EXECUTION SEQUENCE (PILOT RUNNER)

```text
1. Preflight:
   - Input/SOURCE_MANUSCRIPT.md exists, non-empty, utf-8
   - Input/PROMPT_MAP.yaml exists, non-empty, utf-8
   - Gemma.md exists, non-empty
   - config/writer_config.yaml exists; generation knobs numeric
   - ProtectedSpanParser.parse → SLOTTED_SOURCE + protected_spans
   - SourceParser.parse(SLOTTED_SOURCE) → ordered marker_graph (unique, ordered)
   - PromptMapParser.parse(PROMPT_MAP) → prompt_map
   - SourcePromptMapValidator.validate(marker_graph, prompt_map) → PASS
   - failure → STOP, no inference

2. Per-marker loop (в SOURCE order):
   a. Extract marker interval from SLOTTED_SOURCE
   b. Split interval into REWRITABLE / STRUCTURAL_HEADING segments
   c. CURRENT_SOURCE = concatenated REWRITABLE (с protected slots)
   d. Assemble USER payload:
      - LONG_RANGE_FRAME (from prompt_map)
      - CONTINUITY_CACHE (if marker[k>0]; CACHE = previous block prose)
      - CURRENT_SOURCE
      - LOCAL_TRANSFORMATION
   e. Assemble SYSTEM payload (Gemma.md + RUNTIME_CONTRACT_OVERRIDE)
   f. §18 context-window validation → overflow → STOP
   g. create_chat_completion (numeric knobs from writer_config)
   h. Extract generated_content
   i. Protected slot validation on SLOTTED_CANDIDATE:
      - exact once, no dup, no unknown, order preserved
      - FAIL → PROTECTED_MATERIAL_VIOLATION → STOP
   j. Mechanical protected restore → RESTORED block
   k. Rebuild interval: interleave SOURCE headings + restored block prose
   l. Persist per-marker evidence under Output/runs/<timestamp>/
   m. Update CACHE_BEFORE = restored block prose (for next marker)

3. Assembly:
   - Concatenate rebuilt intervals in marker order
   - Write Output/FINAL.manuscript.md (non-empty)
   - Write run log with marker list, per-marker PASS/FAIL, completion counts, FINAL path/size

4. Report:
   - Status: SUCCESS / FAILURE / BLOCKED
   - Scope claim: PILOT_PRODUCTION
   - Deferred items listed (STABLE_CONFIG, freeze, commit, ACCEPT, resume, §19 path)
```

---

## RUN LOG REQUIRED FIELDS

```yaml
run_log:
  run_type: PILOT_PRODUCTION
  invocation: python -m src.production_runner
  inputs:
    source: Input/SOURCE_MANUSCRIPT.md
    prompt_map: Input/PROMPT_MAP.yaml
    gemma: Gemma.md
    writer_config: config/writer_config.yaml
  preflight:
    protected_parser: PASS / FAIL
    source_parser: PASS / FAIL
    prompt_map_parser: PASS / FAIL
    validator: PASS / FAIL
    marker_count: <N>
  per_marker:
    - marker_id: MP:XXXX
      current_source_length: <chars>
      context_estimate: <tokens>
      n_ctx: <value>
      completion_calls: 1
      protected_slots_expected: <list>
      protected_slots_validated: PASS / FAIL
      structural_segments: <count>
      output_length: <chars>
  final:
    output_path: Output/FINAL.manuscript.md
    output_size: <bytes>
    completion_calls_total: <N>
    markers_processed: <N>
    status: SUCCESS / FAILURE / BLOCKED
    scope: PILOT_PRODUCTION
    deferred:
      - STABLE_CONFIG
      - PRODUCTION_REVISION freeze
      - commit ledger
      - interactive ACCEPT / REJECT
      - resume / recovery
      - SPEC §19 canonical assembly path
```

---

## TESTS / PREFLIGHT ACCEPTANCE

**До inference:**
- `python -m py_compile src/production_runner.py` → PASS
- Preflight on production inputs:
  - marker_count ≥ 1
  - validator PASS
  - writer_config knobs numeric (int/float)
- Greppable check: `src/production_runner.py` не содержит путей `Input/TEST_*`
- `run_manuscript_press.bat` содержит `production_runner`, ноль `paired_runner`

**После authorized full run:**
- либо `Output/FINAL.manuscript.md` non-empty **и** `completion_calls == marker_count`
- либо honest STOP с логом, называющим failing marker (не silent partial FINAL)
- No edit timestamps on SOURCE / PROMPT_MAP

---

## NON-GOALS (PILOT)

```yaml
non_goals:
  - PRODUCTION_REVISION freeze
  - frozen authority tree
  - STABLE_CONFIG emission
  - interactive ACCEPT / REJECT / ACCEPT_PATCHED
  - COMMIT_RECORD / commit ledger
  - cache from accepted commit
  - commit-chain / state reconstruction / resume
  - SPEC §19 assembly/final_manuscript.md as canonical path
  - full revision isolation
  - config/WRITER_CONFIG.yaml rename
  - removing TEST_* fixtures
  - root parser duplicates cleanup
  - paired_runner resurrection
  - CONCEPT_PACKAGE / builder.py path
  - generator.py as orchestrator
  - SOURCE / PROMPT_MAP editing
  - automatic segmentation
  - automatic oversized split
  - truncation
  - batching around oversized marker
  - semantic PATCH validation
  - global manuscript review
  - autonomous rewrite of protected material
```

---

## STOP CONDITIONS

Любой из:
- missing / empty / non-utf8 input
- preflight parse failure
- SOURCE ↔ PROMPT_MAP validator FAIL
- duplicate / unordered marker graph
- §18 context overflow
- create_chat_completion exception
- empty generated content
- protected slot validation FAIL
- protected restore mismatch

→ **STOP**, no skip-ahead, no partial FINAL. Записать honest failure в run log.

---

## COMPLETION REPORT FORMAT

```yaml
PILOT_PRODUCTION_RUNNER_REPORT:
  STATUS: SUCCESS / FAILURE / BLOCKED
  RUN_TYPE: PILOT_PRODUCTION
  SCOPE: PILOT_PRODUCTION — not full SPEC runtime

  FILES_CREATED:
    - src/production_runner.py
    - run_manuscript_press.bat (modified)
    - Output/FINAL.manuscript.md (if SUCCESS)
    - Output/runs/<timestamp>/... (per-marker evidence)

  PREFLIGHT:
    inputs_present: true
    utf8: PASS
    protected_parser: PASS
    source_parser: PASS
    marker_count: <N>
    prompt_map_parser: PASS
    validator: PASS
    writer_config_knobs_numeric: PASS

  GENERATION:
    completion_calls_total: <N>
    markers_processed: <N>
    context_overflow_events: 0
    protected_violations: 0

  FINAL:
    output_path: Output/FINAL.manuscript.md
    output_size: <bytes>
    output_non_empty: true

  DEFERRED:
    - STABLE_CONFIG
    - PRODUCTION_REVISION freeze
    - commit ledger
    - interactive ACCEPT / REJECT
    - resume / recovery
    - SPEC §19 canonical assembly path

  NEXT: WAIT_FOR_GROK_REVIEW
```

---

## END PROTOCOL

```text
IMPLEMENT → PY_COMPILE → PREFLIGHT → STOP → WAIT_FOR_GROK
(Full run authorized only after implementation ACCEPT by Grok/Shogun.)
```

---

```yaml
BRIGADIER_STATUS:
  step: MANUSCRIPT_PRESS_PILOT_PRODUCTION_RUNNER
  status: DRAFT — READY FOR GROK REVIEW
  route: LOCKED — not reconsidered
  spec: v3.2.2 unchanged (target authority)
  execution_authority: PILOT_EXECUTION_PROFILE
  deltas_integrated:
    - FINAL_ROUTE_DECISION
    - FINAL_ROUTE_AUTHORITY_DELTA
    - ROUTE_DELTA_2
  content_of_SOURCE_or_PROMPT_MAP: NOT READ
  next: WAIT_FOR_GROK_SIGN_OFF
  stop: true
```

---
Бригадир на линии. STOP.