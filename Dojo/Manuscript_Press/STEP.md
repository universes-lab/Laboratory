# STEP.md — MANUSCRIPT_PRESS

## IDENTITY

**Project:** MANUSCRIPT_PRESS  
**Phase:** 1  
**Step:** SMOKE_BRIDGE  
**Version:** 1.1  
**Date:** 2026-09-06  
**Step Type:** DIAGNOSTIC_SMOKE  

Operation_ID: PHASE1_SMOKE_BRIDGE_V1_1
Status: ACTIVE
Execution_State: NOT_EXECUTED

**Technical Authority:**
- MANUSCRIPT_PRESS ENGINEERING SPEC v3.2.2:
  - §1 — ONE TRANSACTION = ONE PRODUCTION MARKER BLOCK
  - §3 — SOURCE_MANUSCRIPT / PROMPT_MAP marker semantics
  - §4 — protected-first processing
  - §8 — CONTEXT ASSEMBLY
  - §21 — first block has no CACHE_BEFORE
- Accepted Phase-1 Steps 1–4
- Accepted Step-5 structural semantics
- Existing proven Gemma runtime
- Shogun-authorized diagnostic exception permitting this smoke without STABLE_CONFIG
- Grok SYSTEM REVIEW: PASS_WITH_PATCHES
- DOC REVIEW: APPROVED — 2026-09-06

---

## OBJECTIVE

Prove the shortest real connectivity path:

```text
ONE WHOLE SOURCE_MANUSCRIPT
        +
ONE PROMPT_MAP
        ↓
accepted parser chain
        ↓
one existing production block: MP:0101
        ↓
§8-shaped diagnostic payload
        ↓
existing Gemma runtime
        ↓
real non-empty generated prose
```

The required generated artifact is:

```text
Output/SMOKE_MP-0101.md
```

This STEP tests connectivity.

It does NOT establish production readiness or literary acceptance.

---

## CANONICAL INPUT MODEL

MANUSCRIPT_PRESS receives:

1. one complete `SOURCE_MANUSCRIPT`;
2. one accompanying `PROMPT_MAP`.

The SOURCE is already segmented logically by production markers such as:

```text
<!-- MP:0101 -->
```

The system MUST NOT create separate source-fragment files.

The system MUST NOT perform automatic segmentation.

Marker blocks are internal views over the one complete SOURCE document.

---

## INPUTS

Use exactly:

```text
Input/TEST_SOURCE_MANUSCRIPT.md
Input/TEST_PROMPT_MAP.yaml
Gemma.md
config/writer_config.yaml
```

Selected marker:

```text
MP:0101
```

Existing model configured by `writer_config.yaml`:

```text
D:/Gemini/models/Gemma-The-Writer-9B-D_AU-q5_k_m.gguf
```

---

## ACCEPTED COMPONENTS TO REUSE

Use canonical package implementations only:

```text
src/parser/protected_span_parser.py
src/parser/source_parser.py
src/parser/prompt_map_parser.py
src/parser/source_prompt_map_validator.py
src/loader.py
```

Do NOT use root-level duplicate parser modules.

Do NOT modify accepted components.

---

## ALLOWED WORKING FILES

Create:

```text
src/smoke_bridge.py
Output/SMOKE_MP-0101.md
Output/SMOKE_MP-0101.payload.txt
Output/SMOKE_MP-0101.run.log
```

Do NOT create a new test module for this diagnostic STEP.

Do NOT modify:

```text
Gemma.md
config/
src/loader.py
src/generator.py
src/parser/*
src/core/*
SPEC.md
Current_Prompt.md
```

except normal activation of this physical STEP by Shogun outside Samurai execution.

---

# DIAGNOSTIC-ONLY RULE

`src/smoke_bridge.py` is a disposable diagnostic driver.

It is NOT:

- a production orchestrator;
- a public runtime API;
- a future commit/resume engine;
- a second MANUSCRIPT_PRESS architecture.

Production code MUST NOT depend on `smoke_bridge.py`.

Its sole purpose is to prove the bridge and then stop.

---

# EXECUTION SEQUENCE

## 1. Load Complete SOURCE

Read:

```text
Input/TEST_SOURCE_MANUSCRIPT.md
```

as one complete text document.

Do not split it into physical files.

---

## 2. Protected-First Parse

Execute:

```python
ProtectedSpanParser().parse(source)
```

Obtain:

```text
protected_spans
slotted_source
```

Required preflight evidence:

- protected span `P01_01` is detected;
- its raw protected body is absent from `slotted_source`;
- its slot representation is present in `slotted_source`.

Failure → STOP.

---

## 3. Build SOURCE Marker Graph

Execute a fresh:

```python
SourceParser().parse(slotted_source)
```

Required graph includes, in SOURCE order:

```text
MP:0101
MP:0102
MP:0103
```

The selected marker is:

```text
MP:0101
```

Do not derive execution order from PROMPT_MAP.

---

## 4. Parse PROMPT_MAP

Execute:

```python
PromptMapParser().parse("Input/TEST_PROMPT_MAP.yaml")
```

For `MP:0101`, obtain non-empty:

```text
long_range_frame
local_transformation
```

---

## 5. Validate SOURCE ↔ PROMPT_MAP

Execute:

```python
SourcePromptMapValidator().validate(marker_graph, prompt_map)
```

Must PASS before inference.

Do not bypass or duplicate this validator.

---

# CURRENT BLOCK EXTRACTION

## 6. Derive MP:0101 Body

`MP:0101` is boundary metadata.

The marker itself:

```text
<!-- MP:0101 -->
```

MUST NOT appear inside `BEGIN_CURRENT_SOURCE`.

For this smoke:

```text
CURRENT_SOURCE =
exact slotted_source content
after the MP:0101 marker
and before the MP:0102 marker
```

Do not include MP:0102.

Do not trim, rewrite, summarize, or normalize the block merely for convenience.

Use accepted SourceParser marker syntax when locating the selected and following production-marker boundaries.

The extracted block MUST correspond to the same marker order already validated by SourceParser.

---

## 7. Block-Boundary Preflight

Before inference automatically verify:

- CURRENT_SOURCE contains the MP:0101 source prose;
- CURRENT_SOURCE does NOT contain MP:0102 prose;
- CURRENT_SOURCE does NOT contain `<!-- MP:0101 -->`;
- CURRENT_SOURCE does NOT contain `<!-- MP:0102 -->`.

For the supplied fixture, the check may use unique known phrases from MP:0101 and MP:0102 to prove the boundary.

Failure → STOP before model loading.

---

# OPTIONAL §8 SECTIONS FOR THIS BLOCK

## CACHE_BEFORE

`MP:0101` is the first production block.

Therefore:

```text
CACHE_BEFORE = absent
```

Do NOT emit:

```text
BEGIN_CONTINUITY_CACHE
END_CONTINUITY_CACHE
```

Do NOT create fake empty previous prose.

---

## PROTECTED_CONTEXT

The protected span `P01_01` is not inside the MP:0101 current block.

The selected block therefore expects no protected slots.

For this smoke:

```text
PROTECTED_CONTEXT = absent
```

Do NOT emit an empty protected-context section.

---

## STRUCTURAL_CONTEXT

The heading:

```text
## 1.6 The organizing question
```

appears before the first production marker.

Under accepted Step-5 semantics it is pre-marker structural material, not material bound to `MP:0101`.

Therefore for this smoke:

```text
STRUCTURAL_CONTEXT = absent
```

Do NOT invent a heading → MP:0101 association.

Do NOT emit an empty structural-context section.

---

# USER PAYLOAD

## 8. Assemble Exact USER Message

Construct exactly the present sections:

```text
BEGIN_LONG_RANGE_FRAME
<MP:0101 LONG_RANGE_FRAME>
END_LONG_RANGE_FRAME

BEGIN_CURRENT_SOURCE
<exact extracted slotted MP:0101 body>
END_CURRENT_SOURCE

BEGIN_LOCAL_TRANSFORMATION
<MP:0101 LOCAL_TRANSFORMATION>
END_LOCAL_TRANSFORMATION
```

The USER payload MUST NOT contain:

- `BEGIN_CONTINUITY_CACHE`;
- `BEGIN_PROTECTED_CONTEXT`;
- `BEGIN_STRUCTURAL_CONTEXT`;
- CONCEPT_PACKAGE material;
- legacy compiled_input material;
- another MP block.

Persist the exact USER message BEFORE inference to:

```text
Output/SMOKE_MP-0101.payload.txt
```

This file is primary physical evidence.

---

# SYSTEM PAYLOAD

## 9. Existing Gemma Kernel

Read physical:

```text
Gemma.md
```

without modifying it.

Wrap it:

```text
BEGIN_GEMMA_KERNEL
<exact Gemma.md content>
END_GEMMA_KERNEL
```

---

## 10. Transitional Runtime Contract Override

`Gemma.md` still contains legacy `Concept Package / Package Prompt` terminology.

Do NOT rewrite `Gemma.md` in this STEP.

For this diagnostic inference only, append the following transient system-side block after the Gemma kernel:

```text
BEGIN_RUNTIME_CONTRACT_OVERRIDE
For this diagnostic run, treat the legacy Concept Package / Package Prompt
wording in the Gemma kernel as superseded by the structured USER message.

The authorities for this inference are only the USER sections actually present:
LONG_RANGE_FRAME,
CURRENT_SOURCE,
LOCAL_TRANSFORMATION,
and any STRUCTURAL_CONTEXT, PROTECTED_CONTEXT, or CONTINUITY_CACHE section
when such a section is present.

Do not invent substantive material beyond those supplied authorities.
Do not require a legacy Concept Package or Package Prompt.
END_RUNTIME_CONTRACT_OVERRIDE
```

This override exists only to make the connectivity experiment semantically interpretable.

It is NOT a permanent Gemma.md redesign.

Record in the run log:

```text
RUNTIME_CONTRACT_OVERRIDE=PRESENT
```

---

# STABLE_CONFIG DIAGNOSTIC EXCEPTION

Full SPEC §8 production context includes STABLE_CONFIG.

No canonical STABLE_CONFIG is supplied for this diagnostic run.

Therefore this explicitly authorized smoke:

- MUST NOT invent one;
- MUST NOT emit an empty STABLE_CONFIG section;
- MUST be labelled `NON_PRODUCTION_SMOKE`;
- MUST NOT claim full production §8 compliance.

Absence of STABLE_CONFIG is not a blocker for this diagnostic experiment.

---

# INFERENCE

## 11. Reuse Proven Runtime Primitive

Use:

```python
from src.loader import load_model
```

Load the existing model through:

```text
config/writer_config.yaml
```

Then call the loaded Llama instance directly with:

```python
messages = [
    {"role": "system", "content": system_payload},
    {"role": "user", "content": user_payload},
]
```

and:

```python
llm.create_chat_completion(...)
```

Use generation parameters physically present in `writer_config.yaml`.

Current expected values are:

```text
n_ctx: 8192
max_tokens: 2048
top_p: 0.9
temperature: 0.0
```

Report actual loaded/configured values rather than assuming them.

---

## 12. Legacy Runtime Exclusion

Do NOT call:

```text
src.generator.generate(...)
```

Do NOT use:

```text
compiled_input.txt
CONSTANTS CHECK
CONCEPT_PACKAGE
Package Prompt
builder.py
paired_runner.py
```

`src/generator.py` is historical evidence for the proven completion-call pattern only.

The smoke uses:

```text
loader.py → loaded Llama → create_chat_completion()
```

directly.

---

## 13. Exactly One Real Completion

Perform exactly one real:

```text
create_chat_completion
```

call.

No retries.

No second marker.

No alternate prompt experiment.

No temperature sweep.

If generation raises an exception, returns no choices, or returns empty assistant content:

```text
GENERATION_FAILED
```

Report failure and STOP.

---

# OUTPUT

## 14. Extract Generated Content

Use:

```python
output["choices"][0]["message"]["content"]
```

The result must be non-empty after:

```python
content.strip()
```

Do NOT run legacy CONSTANTS CHECK.

Do NOT perform literary acceptance.

---

## 15. Persist Exact Generated Text

Write exact returned assistant content to:

```text
Output/SMOKE_MP-0101.md
```

Do not prepend:

- diagnostic commentary;
- metadata;
- PASS markers;
- explanation.

The file contains only Gemma's returned text.

---

# RUN LOG

Create:

```text
Output/SMOKE_MP-0101.run.log
```

It must record at least:

```text
RUN_TYPE=NON_PRODUCTION_SMOKE
SELECTED_MARKER=MP:0101

PROTECTED_PARSE=PASS
SOURCE_GRAPH=PASS
PROMPT_MAP_PARSE=PASS
SOURCE_PROMPT_MAP_VALIDATION=PASS
BLOCK_BOUNDARY_CHECK=PASS
PAYLOAD_STRUCTURE_CHECK=PASS

CACHE_EMITTED=false
PROTECTED_CONTEXT_EMITTED=false
STRUCTURAL_CONTEXT_EMITTED=false
RUNTIME_CONTRACT_OVERRIDE=PRESENT

MODEL_PATH=<actual>
N_CTX=<actual>
MAX_TOKENS=<actual>
TOP_P=<actual>
TEMPERATURE=<actual>

SYSTEM_PAYLOAD_LENGTH=<actual>
USER_PAYLOAD_LENGTH=<actual>

CREATE_CHAT_COMPLETION_CALLS=1
OUTPUT_LENGTH=<actual>
OUTPUT_NON_EMPTY=true
```

If execution fails, record the factual failure before STOP where possible.

---

# AUTOMATED PREFLIGHT CHECKS

Before model inference, `smoke_bridge.py` must automatically verify only these six conditions:

1. ProtectedSpanParser succeeds on the physical TEST SOURCE and extracts known protected material correctly.
2. SourceParser returns the expected ordered marker graph containing MP:0101 → MP:0102 → MP:0103.
3. Extracted MP:0101 CURRENT_SOURCE contains MP:0101 prose and excludes MP:0102 prose / boundary markers.
4. PROMPT_MAP provides non-empty LONG_RANGE_FRAME and LOCAL_TRANSFORMATION for MP:0101.
5. SOURCE ↔ PROMPT_MAP validator passes.
6. USER payload:
   - contains LONG_RANGE_FRAME;
   - contains CURRENT_SOURCE;
   - contains LOCAL_TRANSFORMATION;
   - omits CONTINUITY_CACHE;
   - omits PROTECTED_CONTEXT;
   - omits STRUCTURAL_CONTEXT;
   - contains no CONCEPT_PACKAGE assembly.

These checks are part of the diagnostic driver.

Do NOT create another test suite merely to repeat them.

Only after all six PASS may the real model be loaded and inference executed.

---

# PRIMARY ACCEPTANCE EVIDENCE

A successful SMOKE BRIDGE requires all three artifacts:

```text
Output/SMOKE_MP-0101.md
Output/SMOKE_MP-0101.payload.txt
Output/SMOKE_MP-0101.run.log
```

PASS requires:

### Generated Output

- one real Gemma inference occurred;
- output file exists;
- generated assistant content is non-empty.

### Exact Payload Evidence

The saved USER payload proves:

- LONG_RANGE_FRAME came from MP:0101;
- CURRENT_SOURCE is only the MP:0101 body;
- LOCAL_TRANSFORMATION came from MP:0101;
- no CACHE was emitted;
- no legacy CONCEPT_PACKAGE input was used.

### Runtime Evidence

The run log proves:

- accepted parser path executed;
- validation passed;
- one completion call occurred;
- existing loader/model path was used;
- transitional runtime override was active;
- output was persisted.

A non-empty output without valid payload evidence is NOT sufficient for PASS.

---

# WHAT THIS SMOKE PROVES

A PASS proves only:

> The new canonical whole-document SOURCE + PROMPT_MAP pipeline can select one already-marked production block through the accepted parser chain, construct the intended diagnostic runtime context, feed it into the existing Gemma inference backend, and obtain real generated prose.

---

# WHAT THIS SMOKE DOES NOT PROVE

It does NOT prove:

- literary quality;
- production readiness;
- final Gemma.md contract;
- STABLE_CONFIG behavior;
- protected restoration through inference;
- CACHE continuity;
- multi-block sequencing;
- revision integrity;
- candidate eligibility;
- commit behavior;
- resume/recovery;
- final assembly.

---

# NON-GOALS

Do NOT implement:

- revision validator;
- authority-freeze changes;
- candidate pipeline;
- commit ledger;
- resume/recovery;
- CACHE simulation;
- multi-block execution;
- final assembly;
- STABLE_CONFIG;
- Gemma.md rewrite;
- automatic segmentation;
- CONCEPT_PACKAGE compatibility;
- builder compatibility;
- paired_runner replacement;
- project ROOT migration;
- Git operations;
- new failure-taxonomy codes.

---

# REPORT FORMAT

```yaml
SMOKE_BRIDGE_REPORT:
  STATUS: SUCCESS / FAILURE / BLOCKED

  RUN_TYPE: NON_PRODUCTION_SMOKE

  FILES_CREATED:
    - src/smoke_bridge.py
    - Output/SMOKE_MP-0101.md
    - Output/SMOKE_MP-0101.payload.txt
    - Output/SMOKE_MP-0101.run.log

  SOURCE:
    FILE: Input/TEST_SOURCE_MANUSCRIPT.md
    SELECTED_MARKER: MP:0101

  PROMPT_MAP:
    FILE: Input/TEST_PROMPT_MAP.yaml

  PREFLIGHT:
    ProtectedSpanParser: PASS / FAIL
    SourceParser: PASS / FAIL
    PromptMapParser: PASS / FAIL
    SourcePromptMapValidator: PASS / FAIL
    BlockBoundary: PASS / FAIL
    PayloadStructure: PASS / FAIL

  PAYLOAD:
    CACHE_EMITTED: false
    PROTECTED_CONTEXT_EMITTED: false
    STRUCTURAL_CONTEXT_EMITTED: false
    RUNTIME_CONTRACT_OVERRIDE: PRESENT
    SYSTEM_LENGTH: <actual>
    USER_LENGTH: <actual>

  GENERATION:
    MODEL: <actual path>
    N_CTX: <actual>
    MAX_TOKENS: <actual>
    TEMPERATURE: <actual>
    TOP_P: <actual>
    CREATE_CHAT_COMPLETION_CALLS: 1
    OUTPUT_LENGTH: <actual>
    OUTPUT_NON_EMPTY: true / false

  PRIMARY_EVIDENCE:
    OUTPUT: Output/SMOKE_MP-0101.md
    USER_PAYLOAD: Output/SMOKE_MP-0101.payload.txt
    RUN_LOG: Output/SMOKE_MP-0101.run.log

  LIMITATIONS:
    - NON_PRODUCTION_SMOKE
    - STABLE_CONFIG not exercised
    - continuity/cache not exercised
    - no literary acceptance

  NEXT: WAIT_FOR_DEEPSEEK
```

---

# END PROTOCOL

After execution:

```text
VERIFY
→ REPORT
→ STOP
→ WAIT_FOR_DEEPSEEK
```

Do not continue to another marker.

Do not begin another STEP.

---

END OF SMOKE BRIDGE STEP