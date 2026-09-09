# CURRENT PROMPT — MANUSCRIPT_PRESS

PROJECT: MANUSCRIPT_PRESS
ROOT: D:\Gemini\dojo

ACTIVE_MODE: IMPLEMENTER

ACTIVE OPERATION:
CONTINUITY_INFERENCE_BLOCKER — PHASE C2 TYPE FIX FOR GENERATION KNOBS.

PURPOSE:
Localize and, if supported by evidence, minimally fix the generation-knob type
mismatch that caused:

TypeError: '<=' not supported between instances of 'str' and 'int'

This phase does NOT authorize inference.

The current technical route is owned by:
- Grok — Technical Lead / Route Architect
- DeepSeek — Coding Sensei
- Samurai — Executor
- Doctor — TEC / Metsuke / behavior / evidence-integrity monitoring
- Shogun — final activation authority

ACTIVE SPEC:
D:\Gemini\dojo\SPEC.md

SPEC AUTHORITY:
SPEC v3.2.2 remains frozen and authoritative.

Do NOT rewrite, reinterpret, relax, or expand SPEC because of this blocker.

CURRENT SENSEI INSTRUCTION:
@D:\Gemini\dojo\STEP.md

The physical STEP.md defines the technical assignment.
This Current_Prompt.md defines the currently authorized execution position.

---

## CURRENT PHASE AUTHORIZATION

PHASE C2 — TYPE FIX: AUTHORIZED

PHASE C3 — CONTROLLED INFERENCE RERUN: LOCKED

GREEN LIGHT C3 = NO

C2 must end with:

C2_FIX_REPORT
→ STOP
→ WAIT_FOR_GREEN_LIGHT_C3

No inference, model execution, continuity rerun, or second technical branch is
authorized during C2.

---

## C2 INTERNAL ORDER

C2 contains two ordered parts:

### C2.A — READ-ONLY LOCALIZATION

Mandatory first.

Inspect only the existing code/config path needed to establish:

- where `config/writer_config.yaml` is loaded;
- raw values of `generation.max_tokens`, `generation.temperature`,
  `generation.top_p`;
- their actual types after loading;
- exact values/types passed to `create_chat_completion`;
- whether `"N/A"` or another string fallback enters completion kwargs;
- where such a value originates, if present.

No edit before this localization is complete.

Emit `C2_READONLY_REPORT`.

### C2.B — MINIMAL TYPE FIX

Authorized only if C2.A evidence shows that a type mismatch in the bench call
path is the blocker addressed by the Sensei instruction.

Allowed file:
- `src/continuity_cache_bench.py`

Allowed change:
- minimal type normalization of generation knobs sourced from the existing
  writer configuration before they are passed to `create_chat_completion`.

Expected numeric types:
- `max_tokens` → int
- `temperature` → float
- `top_p` → float

Do not change `config/writer_config.yaml`.

Do not add new product logic.

After the minimal fix:
- perform static/read-only verification only;
- emit `C2_FIX_REPORT`;
- STOP.

If C2.A does NOT support the expected type-mismatch diagnosis:
- do not force the planned fix;
- report the evidence;
- STOP and wait for Sensei / Grok.

---

## C2 ALLOWED

- ReadFile / inspect `src/continuity_cache_bench.py`
- ReadFile / inspect `config/writer_config.yaml`
- ReadFile / compare the already proven working smoke/generator call path
- minimal Edit of `src/continuity_cache_bench.py` only, and only after C2.A
  supports the fix
- static syntax/code-path verification that does NOT execute the continuity
  bench or inference

---

## C2 FORBIDDEN

Do NOT:

- run `python src/continuity_cache_bench.py`
- run inference
- execute `load_model()` for testing
- call `create_chat_completion`
- perform any trial model execution
- modify `loader.py`
- modify `config/writer_config.yaml`
- modify parsers
- modify CACHE semantics
- modify marker extraction
- modify encoding policy
- rewrite SPEC
- rewrite IMPLEMENTATION_PLAN
- perform Git operations
- expand into another blocker
- proceed to Phase C3
- interpret the existence of Phase C3 as authorization

If a new blocker appears:
REPORT FACT → STOP.

---

## EXECUTION DISCIPLINE

### NO EXECUTION CLAIM WITHOUT EXECUTION EVIDENCE

Observed values/types must come from actual code/config inspection.

Do not report inferred runtime values as observed values.

Do not claim a fix is effective beyond what static evidence supports.

C2 may establish:
- what the type path is;
- what code was changed;
- that the changed code statically supplies numeric values.

C2 may NOT establish:
- successful inference;
- successful continuity;
- successful output generation.

Those belong to C3 only.

### NO SILENT STATE TRANSITION

Authorized C2 chain:

C2_READONLY_INSPECTION
→ TYPE_PATH_LOCALIZED
→ C2_READONLY_REPORT
→ MINIMAL_FIX_IF_SUPPORTED
→ STATIC_FIX_VERIFICATION
→ C2_FIX_REPORT
→ STOP

No inference state belongs to C2.

---

## SAMURAI DIAGNOSTIC SENSORS

This is a narrow type-path repair area.

Emit SHORT telemetry in the active session after substantial transitions.

Do NOT create separate sensor files.

Required form:

SENSOR:
  STATE: <current C2 state>
  OBSERVED: <literal fact only>
  EVIDENCE: <file / config key / code location>
  DRIFT_CHECK: OK / STOP
  NEXT_WITHIN_AUTHORIZED_C2: <next authorized action>

Emit sensors at:

1. after locating config load + raw generation values/types
2. after locating values/types passed to completion
3. after identifying origin of any string/"N/A" value
4. after minimal fix is applied, if authorized by evidence
5. after static verification of the fix

If `DRIFT_CHECK: STOP`:
- stop;
- report the mismatch;
- wait for Sensei / Grok / Shogun.

Sensors are observations only.
They do not authorize C3.

---

## TEC / METSUKE CHECK

Before every substantial action confirm internally:

- PROJECT = MANUSCRIPT_PRESS
- ACTIVE_PHASE = C2 TYPE FIX
- C3 INFERENCE = LOCKED
- EDIT AUTHORITY = ONLY src/continuity_cache_bench.py
- EDIT SCOPE = TYPE NORMALIZATION ONLY
- MODEL EXECUTION AUTHORITY = NONE
- GIT AUTHORITY = NONE
- SPEC CHANGE AUTHORITY = NONE

After `C2_FIX_REPORT`:

- C2 authority = EXHAUSTED
- C3 authority = STILL LOCKED
- ACTIVE POSITION = WAIT_FOR_GREEN_LIGHT_C3

If any instruction conflicts with this frame:
STOP and report the authority conflict.

---

## C2 READ-ONLY REPORTING CONTRACT

C2_READONLY_REPORT:
  config_loaded_from: config/writer_config.yaml
  max_tokens:
    raw_value: <actual>
    raw_type: <str / int / float / other>
    passed_to_completion: <actual>
    passed_type: <str / int / float / other>
  temperature:
    raw_value: <actual>
    raw_type: <str / int / float / other>
    passed_to_completion: <actual>
    passed_type: <str / int / float / other>
  top_p:
    raw_value: <actual>
    raw_type: <str / int / float / other>
    passed_to_completion: <actual>
    passed_type: <str / int / float / other>
  origin_of_N/A_if_present: <actual origin / none>
  root_cause_hypothesis: <one sentence>
  fix_required: yes / no

Then continue to C2.B only if the evidence supports the authorized type-fix
path.

---

## C2 FIX REPORTING CONTRACT

C2_FIX_REPORT:
  files_modified:
    - src/continuity_cache_bench.py
  changes:
    max_tokens: <before> -> <after>
    temperature: <before> -> <after>
    top_p: <before> -> <after>
  removal_of_N/A: yes / no / not_applicable
  static_verification: PASS / FAIL
  inference_executed: false
  next: WAIT_FOR_GREEN_LIGHT_C3

If no fix was justified:

C2_FIX_REPORT:
  files_modified: []
  fix_applied: false
  reason: <evidence-based>
  inference_executed: false
  next: WAIT_FOR_GROK

---

## END CONDITION

C2 ends after the read-only localization plus the minimal supported type fix
and static verification.

Then:

REPORT
→ STOP
→ WAIT_FOR_GREEN_LIGHT_C3.

GREEN LIGHT C3 must be explicit.

Until that explicit authorization exists:
NO INFERENCE.
