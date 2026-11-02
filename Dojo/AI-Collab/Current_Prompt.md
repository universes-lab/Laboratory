# CURRENT PROMPT — AI-Collab

DATE: 2026-10-28

PROJECT: AI-Collab

ROOT:

`E:\Gemini\Dojo\AI-Collab`

ACTIVE_MODE: IMPLEMENTER

ACTIVE_OPERATION: BUILD_001_STEP_2_VERDICT_ENGINE_CORRECTIVE

CURRENT_STEP:

`BUILD 001 / STEP 2 — VERDICT_ENGINE_CORRECTIVE`

FINAL_AUTHORITY:

Author / Shogun

CURRENT_REPORT_TARGET:

Grok

---

## CURRENT EXTERNAL INSTRUCTION

Perform the corrective implementation defined by:

`SPEC.md — BUILD 001 / STEP 2 — VERDICT ENGINE v2.1 CORRECTIVE`

No separate `STEP.md` is used or required.

The current SPEC is the task-specific technical authority.

This is a **corrective continuation of STEP 2**, not a new BUILD step.

---

## AUTHORITY

Current control chain:

Global Coding Samurai doctrine  
→ project `GEMINI.md`  
→ this `Current_Prompt.md`  
→ `SPEC.md v2.1`

Follow the authority order declared inside SPEC.

Do not silently reconcile a contradiction between:

- `WEB_SEAT_WS0_OBSERVATION_CONTRACT.md`;
- `BUILD_001_STEP2_STEP3_SPEC.md`;
- authoritative vector expectations;
- corrective SPEC.

If a real unresolved contradiction remains:

`STOP → REPORT EXACT CONFLICT → WAIT_FOR_GROK_OR_SHOGUN`

Doctor establishes the operational frame.

Doctor does not define verdict semantics.

---

## CURRENT AUTHORIZATION

Samurai is authorized to:

- inspect the authoritative inputs permitted by SPEC;
- modify `verdict_engine.py` exactly as required by corrective v2.1;
- leave `test_vectors.py` unchanged;
- leave `BUILD_001_STEP2_VECTORS.json` unchanged;
- run the stated py_compile;
- perform one stated vector/L0 verification run;
- collect mismatches and `rules_trace`;
- produce `STEP2_CORRECTIVE_REPORT`.

Samurai is not authorized to:

- modify vectors;
- modify `test_vectors.py`;
- invent reasons;
- implement rule 5 contrary to v2.1;
- recompute fingerprints;
- implement STEP 3;
- install packages;
- expand the corrective task;
- begin another repair cycle after the authorized verification run.

---

## PREFLIGHT

Before modification verify:

`E:\Gemini\Dojo\AI-Collab\.venv\Scripts\python.exe`

exists.

If absent:

`STOP → REPORT VENV_MISSING → WAIT`

Do not install packages.

Do not substitute another environment.

---

## METSUKE

Before changing state confirm:

`PROJECT = AI-Collab`

`ROOT = E:\Gemini\Dojo\AI-Collab`

`ACTIVE_MODE = IMPLEMENTER`

`ACTIVE_OPERATION = BUILD_001_STEP_2_VERDICT_ENGINE_CORRECTIVE`

`ACTIVE_SPEC = v2.1 CORRECTIVE`

`AUTHORIZED IMPLEMENTATION FILE = verdict_engine.py`

If clear:

continue.

---

## CORRECTIVE EXECUTION DISCIPLINE

This operation is intentionally bounded.

Required route:

`READ AUTHORITATIVE INPUTS`

→ `MODIFY verdict_engine.py`

→ `PY_COMPILE`

→ `ONE test_vectors.py RUN`

→ `VERIFY 32 VECTORS + L0_GUARD`

→ `REPORT TO GROK`

→ `STOP`

→ `WAIT_FOR_GROK`

Do not turn a failing corrective run into another autonomous repair cycle.

If the run fails:

preserve actual result;

report mismatches and `rules_trace`;

STOP.

A FAIL report is preferable to an unauthorized second corrective iteration.

---

## REPORT IS PART OF COMPLETION

The STEP is not complete merely because code was modified.

The corrective cycle ends only after the required factual report is emitted.

Use:

`STEP2_CORRECTIVE_REPORT`

from SPEC v2.1.

After emitting it:

**STOP.**

Do not:

- rerun for reassurance;
- patch another mismatch;
- modify vectors;
- improve unrelated code;
- begin STEP 3;
- create a new plan.

Further corrective work requires a new instruction from Grok or Shogun.

---

## HEALTH

Technical failure does not itself mean Samurai health is degraded.

If orientation remains intact:

`HEALTH = OK`

If Samurai loses ROOT, active operation, authorization boundary, one-pass limit, or STOP state:

`HEALTH = DEGRADED`

`STOP → REPORT STATE → WAIT_FOR_EXTERNAL_GUIDANCE`

---

## TERMINAL STATE

Successful corrective completion requires:

`PY_COMPILE PASS`

`32/32`

`L0_GUARD PASS`

`STEP2_CORRECTIVE_REPORT EMITTED`

Then:

`STOP → WAIT_FOR_GROK`

STEP 3 remains unauthorized until external acceptance.

---

@./SPEC.md