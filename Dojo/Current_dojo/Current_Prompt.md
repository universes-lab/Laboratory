# CURRENT PROMPT — MANUSCRIPT_PRESS

PROJECT: MANUSCRIPT_PRESS
ROOT: D:\Gemini\dojo

ACTIVE_MODE: DIAGNOSTICIAN

ACTIVE OPERATION:
CONTINUITY_INFERENCE_BLOCKER — PHASE B2 READ-ONLY LOCALIZATION.

PURPOSE:
Localize why the latest post-fix continuity bench still reports
CREATE_CHAT_COMPLETION_CALLS: 0 without performing any new execution.

This phase is diagnostic only.

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

PHASE B2 — READ-ONLY LOCALIZATION: AUTHORIZED

PHASE C — CONTROLLED RERUN: LOCKED

No inference rerun is authorized.
No code modification is authorized.
No Git operation is authorized.

Only the read-only localization work explicitly listed below may be performed.

---

## B2 ALLOWED

Read-only inspection only:

- inspect `src/continuity_cache_bench.py`
- inspect `src/loader.py`
- inspect the proven working smoke / generator `create_chat_completion` call path
- inspect exactly ONE physical:
  `Output/CONT_MP-0102.run.log`
  representing the last real invocation currently on disk

Use the physical run.log as authoritative execution evidence when it conflicts
with narrative, remembered state, or structured chat reports.

The existing Samurai edit in `src/continuity_cache_bench.py` is:

CANDIDATE DIFF / DIAGNOSTIC EVIDENCE

It is NOT an accepted route merely because it exists on disk.

Do not destroy it.
Do not extend it.
Do not revert it.
Do not normalize it.

---

## B2 FORBIDDEN

Do NOT:

- edit any file
- run `python src/continuity_cache_bench.py`
- run any inference
- execute `load_model()` for testing
- perform trial execution
- perform Git operations
- expand or revert the candidate diff
- alter parsers
- alter CACHE semantics
- alter marker extraction
- rewrite SPEC
- proceed to Phase C
- convert a hypothesis into an execution claim

If a new technical possibility is discovered, REPORT IT.
Do not test it by execution.

---

## AUTHORITATIVE QUESTIONS FOR B2

From existing code and the one physical run.log, establish only:

1. LAST SUCCESSFUL STAGE
   What is the last execution stage physically supported by the run.log?

2. EXACT STOP / ERROR
   What exact error, exception, early return, condition, or abort prevented
   `create_chat_completion` from being reached?

3. LOAD_MODEL RETURN
   Does the physical evidence show that `load_model()` actually returned,
   or only that execution reached model-loading code?

4. PREFLIGHT STATE
   In this exact physical run, is preflight PASS or FAIL?
   Resolve `SourcePromptMapValidator` from the log itself, not narrative.

5. ZERO COMPLETION CAUSE
   Why does the same physical run report:
   `CREATE_CHAT_COMPLETION_CALLS: 0`?

6. WORKING PATH COMPARISON
   Compare the current bench call path with the already proven working smoke /
   generator call pattern using read-only code inspection only.

Do not solve beyond the evidence requested above.

---

## EXECUTION DISCIPLINE

### NO EXECUTION CLAIM WITHOUT EXECUTION EVIDENCE

No completed-action claim may be reported without physical or directly
observable evidence.

Narrative memory is not execution evidence.
A structured report is not authoritative when it conflicts with physical log
evidence.
An intended result is not an observed result.

### NO SILENT STATE TRANSITION

Every substantial diagnostic-state transition must leave an observable trace.

For B2 the authorized chain is:

CODE_PATH_INSPECTED
→ WORKING_PATH_COMPARED
→ PHYSICAL_LOG_INSPECTED
→ EVIDENCE_CORRELATED
→ PHASE_B2_REPORT
→ STOP

No edit, rerun, inference, or Phase C action belongs to this chain.

---

## SAMURAI DIAGNOSTIC SENSORS

This is a narrow, previously unstable diagnostic area.

Emit SHORT telemetry after each substantial B2 transition.

These are diagnostic micro-reports, not authorization requests and not final
conclusions.

Do NOT create new telemetry files during B2.
Emit sensors only in the active session output/chat.

Required sensor shape:

SENSOR:
  STATE: <current B2 state>
  OBSERVED: <literal fact only>
  EVIDENCE: <file/code location or physical log line>
  DRIFT_CHECK: OK / STOP
  NEXT_WITHIN_AUTHORIZED_B2: <next read-only action>

Use sensors at these points:

1. after inspecting current bench code path
2. after comparing working completion path
3. after reading the one physical run.log
4. after correlating code path with log evidence

If `DRIFT_CHECK: STOP`:
- do not continue;
- report the mismatch;
- wait for Sensei / Grok / Shogun.

Sensors must never invent missing state.

---

## TEC / METSUKE CHECK

Before every substantial action, confirm internally:

- PROJECT = MANUSCRIPT_PRESS
- ACTIVE_MODE = DIAGNOSTICIAN
- ACTIVE_PHASE = B2 READ-ONLY LOCALIZATION
- PHASE C = LOCKED
- EDIT AUTHORITY = NONE
- INFERENCE AUTHORITY = NONE
- GIT AUTHORITY = NONE

If any current instruction appears to authorize more than this frame,
STOP and report the authority conflict instead of choosing by inference.

---

## PHASE B2 REPORTING CONTRACT

Return one factual final report:

PHASE_B2_REPORT:
  LAST_SUCCESSFUL_STAGE: <physical evidence>
  EXACT_STOP_OR_ERROR: <literal finding>
  LOAD_MODEL_RETURNED: true / false / not_proven
  PREFLIGHT:
    ProtectedSpanParser: PASS / FAIL / not_proven
    SourceParser: PASS / FAIL / not_proven
    PromptMapParser: PASS / FAIL / not_proven
    SourcePromptMapValidator: PASS / FAIL / not_proven
    BlockBoundary: PASS / FAIL / not_proven
    PayloadStructure: PASS / FAIL / not_proven
  CREATE_CHAT_COMPLETION_CALLS: 0
  ZERO_COMPLETION_CAUSE: <evidence-based localization>
  WORKING_PATH_COMPARISON: <concise read-only finding>
  CANDIDATE_DIFF_STATUS:
    supported / unsupported / unresolved
  NEW_HYPOTHESES:
    - <if any; clearly labeled as hypothesis>
  AUTHORITY_VIOLATIONS_OBSERVED:
    - <if any>
  NEXT: WAIT_FOR_DEEPSEEK_AND_GROK

Do not include a SUCCESS claim for continuity bench.
Do not recommend or execute a rerun.
Do not apply a fix.

---

## END CONDITION

After B2:

VERIFY
→ REPORT
→ STOP
→ WAIT_FOR_DEEPSEEK / GROK / SHOGUN.

Cold-session rule:
Treat this physical Current_Prompt.md, the physical STEP.md, and the global
Samurai constitution as current authority.

Do not reconstruct authorization from prior Gemini chat history.
