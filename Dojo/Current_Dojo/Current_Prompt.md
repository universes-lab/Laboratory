# CURRENT PROMPT — MANUSCRIPT_PRESS

PROJECT: MANUSCRIPT_PRESS
ROOT: `D:\Gemini\dojo`

ACTIVE_MODE: IMPLEMENTER

---

# 1. ACTIVE OPERATION

ACTIVE_OPERATION:

**MANUSCRIPT_PRESS PILOT_PRODUCTION_RUNNER — IMPLEMENTATION + NO-INFERENCE PREFLIGHT**

This operation replaces and retires the previous:

`CONTINUITY_INFERENCE_BLOCKER — PHASE C2 TYPE FIX FOR GENERATION KNOBS`

C2 is no longer the current execution position.

Do not reconstruct C2 authority from conversation history.

Do not continue C2.

Do not infer any C3 authority from the previous operational frame.

The current physical files on disk define the new position.

---

# 2. AUTHORITY LAYERS

The following distinctions are mandatory.

## 2.1 SPEC v3.2.2

`SPEC v3.2.2`

is the frozen **target architecture** for MANUSCRIPT_PRESS.

It defines the complete intended production system.

It is NOT being rewritten, relaxed, replaced, or declared fully implemented by this operation.

Do not claim that implementation of the current pilot runner equals completion of the full SPEC v3.2.2 runtime.

---

## 2.2 PILOT_EXECUTION_PROFILE

`PILOT_EXECUTION_PROFILE`

is the current temporary execution authority for the first full-article pilot route.

It authorizes only the subset and temporary execution profile explicitly approved for this pilot.

It does NOT amend SPEC v3.2.2.

It does NOT convert the pilot into the final full-SPEC production runtime.

---

## 2.3 STEP.md

CURRENT SENSEI INSTRUCTION:

`@D:\Gemini\dojo\STEP.md`

The physical current `STEP.md` is the approved technical instruction for this operation.

Its technical route has already received Grok Technical Lead sign-off.

Samurai does not redesign it.

Samurai does not choose an alternative architecture.

Samurai does not substitute a bench, wrapper, runner, parser, cache strategy, assembly strategy, or other implementation route different from the one explicitly defined by the current STEP.

---

## 2.4 ROUTE AUTHORITY PROVENANCE

The current STEP derives its technical authority from the approved MANUSCRIPT_PRESS pilot route package, including:

* Grok route lock;
* `PILOT_EXECUTION_PROFILE`;
* `MANUSCRIPT_PRESS_ROUTE_DELTA_2`;
* Grok final STEP sign-off.

These artifacts are authority provenance.

They are not invitations for Samurai to reopen route design.

---

## 2.5 Current_Prompt.md

This `Current_Prompt.md` defines Samurai's **current authorized execution position**.

It does not alter the technical route.

It determines:

* what phase Samurai is actually in;
* what Samurai may execute now;
* what remains locked;
* what evidence is required;
* when Samurai must STOP.

---

# 3. FINAL AUTHORITY

FINAL AUTHORITY:

**Author / Shogun**

Technical route approval does not itself authorize a long production inference run.

A completed implementation does not itself authorize a long production inference run.

A successful preflight does not itself authorize a long production inference run.

A report saying READY does not itself authorize a long production inference run.

Only an explicit subsequent GREEN LIGHT from Author / Shogun activates the full pilot article inference.

Until then:

**FULL ARTICLE INFERENCE = LOCKED**

---

# 4. CURRENT METSUKE

Samurai's actual position is:

```yaml
PROJECT: MANUSCRIPT_PRESS
ROLE: EXECUTOR
MODE: IMPLEMENTER

ACTIVE_OPERATION: PILOT_PRODUCTION_RUNNER_IMPLEMENTATION

TECHNICAL_ROUTE: LOCKED
STEP_AUTHORITY: CURRENT_PHYSICAL_STEP_MD

SPEC_STATUS: TARGET_ARCHITECTURE_FROZEN
SPEC_VERSION: v3.2.2

PILOT_EXECUTION_PROFILE: ACTIVE_FOR_CURRENT_PILOT_SCOPE

IMPLEMENTATION: AUTHORIZED_BY_CURRENT_STEP
STATIC_VERIFICATION: AUTHORIZED_BY_CURRENT_STEP
NO_INFERENCE_PREFLIGHT: AUTHORIZED_BY_CURRENT_STEP

FULL_ARTICLE_INFERENCE: LOCKED
FULL_PRODUCTION_RUN: LOCKED

GREEN_LIGHT_FOR_LONG_RUN: NO
```

Do not silently move to another position.

---

# 5. ACTIVE OBJECTIVE

Implement exactly the Grok-approved / DeepSeek-finalized pilot production route defined by the current physical `STEP.md`.

The purpose of this operation is to produce an implementation that is technically ready for external acceptance and later explicit GREEN LIGHT.

This operation is NOT the article run itself.

Current authorized chain:

```text
READ CURRENT AUTHORITIES
→ IMPLEMENT APPROVED PILOT RUNNER
→ STATIC VERIFICATION
→ NO-INFERENCE PREFLIGHT
→ EVIDENCE REPORT
→ STOP
→ WAIT FOR EXTERNAL ACCEPTANCE / SHOGUN GREEN LIGHT
```

The following transition is NOT authorized:

```text
PREFLIGHT PASS
→ FULL ARTICLE RUN
```

There must be an external gate between them.

---

# 6. TECHNICAL ROUTE IS FROZEN

The implementation route is already chosen.

Samurai must NOT:

* compare architectural alternatives;
* redesign the route;
* replace the approved runner architecture;
* turn an existing diagnostic bench into an alternative production architecture unless the STEP explicitly requires reuse of a proven component;
* resurrect `src/paired_runner.py`;
* design another wrapper;
* create a second competing entrypoint;
* rewrite SPEC v3.2.2;
* expand the pilot into full freeze / commit / resume implementation;
* add production machinery not required by STEP;
* defer requirements that STEP explicitly marks as required now.

If implementation appears to require a route decision not already resolved by STEP:

**STOP → REPORT OPEN TECHNICAL DECISION**

Do not decide it yourself.

---

# 7. PILOT IDENTITY

The current implementation must preserve this identity:

```yaml
SCOPE_CLASS: PILOT_PRODUCTION
PILOT_NOT_FULL_SPEC_RUNTIME: true
```

Never report:

* `FULL_SPEC_RUNTIME_COMPLETE`
* `FULL_PRODUCTION_IMPLEMENTATION_COMPLETE`
* `SPEC_v3.2.2_IMPLEMENTED`
* or any equivalent claim.

The correct scope is:

**PILOT_PRODUCTION**

unless a later authority explicitly changes it.

---

# 8. PRODUCTION INPUT AUTHORITY

The authorized pilot production inputs are:

```text
Input/SOURCE_MANUSCRIPT.md
Input/PROMPT_MAP.yaml
```

No `TEST_*` input path is the production authority for this route.

Do not silently substitute test-prefixed production inputs.

Do not edit the production inputs.

Do not alter markers.

Do not alter `PROMPT_MAP`.

Do not resegment the manuscript.

Do not make BAD CUT decisions.

Do not add missing instructions.

Do not generate replacement production content.

For this implementation operation, the actual manuscript content is not a Samurai decision surface.

Treat the production inputs as authority artifacts required by the approved runtime route.

Do not manually rewrite or editorially inspect manuscript prose as part of implementation.

---

# 9. APPROVED RUNTIME IDENTITY

The pilot runtime module is the module specified by the current STEP.

The approved route includes:

`src/production_runner.py`

as the pilot runner owner for the new orchestration logic required by the locked route.

The production BAT must be truthful and point to the approved pilot entrypoint exactly as defined by STEP.

Do not retain a stale BAT command that points to a superseded execution path.

Do not invent another module name or BAT command.

If physical STEP.md differs from remembered conversation text:

**PHYSICAL CURRENT STEP.md WINS**

provided it remains inside the already approved route authority.

If a genuine contradiction between STEP and the locked route package is found:

**STOP → AUTHORITY_CONFLICT_REPORT**

Do not reconcile it yourself.

---

# 10. REQUIRED PILOT ROUTE INVARIANTS

Implementation must preserve every invariant explicitly activated by STEP.

Among the locked current pilot requirements are:

* use production `SOURCE_MANUSCRIPT` and `PROMPT_MAP` paths;
* process the full marker graph in exact SOURCE order;
* no silent marker skipping;
* continuity cache follows the approved pilot automatic chain;
* pilot cache must not be represented as the full accepted-commit / resume machinery of SPEC v3.2.2;
* SYSTEM context uses the approved pilot Gemma + runtime override composition defined by STEP;
* deferred full-SPEC elements must remain deferred where the pilot profile says so;
* structural headings are handled by extraction + assembly, not as ordinary rewritable Gemma prose;
* protected parsing reuses the proven protected-first parser path;
* protected-output validation and restoration are implemented where STEP marks them NEW_REQUIRED;
* `BEGIN_PROTECTED_CONTEXT` remains omitted for this pilot where the approved route says OMITTED;
* context-window validation required by the pilot route is implemented before model generation;
* context overflow must STOP rather than truncate, split, batch, or silently drop context;
* pilot final output path is exactly the path defined by STEP;
* no partial successful final manuscript may be represented as a completed pilot result after a blocking failure.

Do not reinterpret these rules.

Implement the physical STEP.

---

# 11. STRUCTURAL PASSTHROUGH — CURRENT PILOT POSITION

For this pilot, Markdown ATX headings outside protected spans are structural material.

They are not free rewritable prose.

The approved route requires structural handling through extraction and final assembly.

Therefore Samurai must preserve the STEP-defined invariant that headings:

* are identified outside protected spans;
* do not enter `CURRENT_SOURCE` as ordinary free prose;
* cannot be rewritten by Gemma;
* are restored at their exact SOURCE positions during pilot assembly.

Do not invent `BEGIN_STRUCTURAL_CONTEXT` if the approved pilot STEP does not use it.

Do not silently fall back to sending headings to Gemma as ordinary text.

If the existing extractor cannot support the exact STEP-defined route, follow the exact fallback already authorized by STEP.

Do not create a third alternative.

---

# 12. PROTECTED MATERIAL — CURRENT PILOT POSITION

The protected-first parser path is reused.

Protected bodies remain outside the rewritable model text.

Gemma sees protected slot tokens inside the approved rewritable source path.

Before mechanical restoration, protected-slot integrity must be checked exactly as required by STEP.

Required protected integrity includes the approved checks for:

* expected slot presence;
* exactly-once occurrence;
* no missing slots;
* no duplicate slots;
* no unknown slots;
* unchanged slot IDs;
* preserved expected order.

Failure:

```text
PROTECTED_MATERIAL_VIOLATION
→ STOP
```

No silent repair.

No guessed replacement.

No partial successful final assembly.

Protected material is restored mechanically from parsed authority material.

Do not rewrite protected material.

---

# 13. CONTEXT-WINDOW DISCIPLINE

The current pilot requires a context-capacity check before each real generation call.

The implementation must provide the exact STEP-defined deterministic validation against writer `n_ctx`.

The estimator / tokenizer method must be only the one authorized by STEP.

The implementation must not call the model merely to measure context.

Overflow condition:

```text
SEGMENTATION_TOO_LARGE_FOR_CURRENT_WRITER_CONFIGURATION
→ STOP
```

Forbidden responses to overflow:

* truncation;
* auto-split;
* hidden batching;
* dropping cache;
* dropping required prompt material;
* dropping configuration;
* silently continuing.

This operation authorizes implementing and preflight-verifying the check.

It does NOT authorize exercising it through the full production manuscript inference run.

---

# 14. CACHE AUTHORITY

For the pilot route, continuity cache behavior is the temporary pilot automatic chain defined by STEP / PILOT_EXECUTION_PROFILE.

Do not present it as the complete SPEC v3.2.2 human acceptance / commit / resume ledger.

Do not implement full commit/resume infrastructure merely because SPEC v3.2.2 contains it.

Do not claim accepted-commit semantics where the pilot profile uses automatic chaining.

The pilot may prove the intended full-article continuity path.

It does not thereby prove the complete final SPEC runtime.

---

# 15. STABLE CONFIG / DEFERRED FULL-SPEC ELEMENTS

Follow the exact STEP and PILOT_EXECUTION_PROFILE policy for `STABLE_CONFIG`.

If the approved pilot route marks an element DEFERRED:

* do not implement it now;
* do not emulate it under another name;
* do not claim it is present;
* do not treat its absence as permission to redesign the pilot.

Deferred full-SPEC machinery remains target architecture, not current execution authority.

---

# 16. ALLOWED ACTIONS NOW

Samurai may:

1. Read:

   * current `Current_Prompt.md`;
   * current `STEP.md`;
   * `SPEC.md` as target architecture;
   * route/provenance artifacts required by STEP;
   * existing source code and configuration necessary to implement STEP.

2. Modify or create:

   * ONLY files explicitly authorized by the physical current STEP.

3. Implement:

   * ONLY the pilot route defined by STEP.

4. Reuse:

   * ONLY existing proven modules/helpers in the manner permitted by STEP.

5. Run:

   * static syntax verification explicitly required by STEP;
   * `py_compile` checks required by STEP;
   * no-inference preflight required by STEP;
   * other non-model verification explicitly required by STEP.

6. Inspect:

   * physical evidence produced by the authorized implementation/preflight checks.

7. Correct:

   * implementation defects inside the same explicitly authorized file/scope when directly localized by deterministic verification and when the correction does not alter the approved route.

8. Produce:

   * the exact implementation/evidence report required by STEP.

---

# 17. FORBIDDEN ACTIONS NOW

Samurai must NOT:

* execute the full article inference;
* execute the long pilot production run;
* treat implementation completion as run authorization;
* treat preflight PASS as run authorization;
* run Gemma merely because the runner is ready;
* consume the production article through an unauthorized inference;
* proceed from implementation into production without an external gate;
* rewrite SPEC v3.2.2;
* edit STEP.md;
* edit `Current_Prompt.md`;
* edit route authority artifacts;
* edit `Input/SOURCE_MANUSCRIPT.md`;
* edit `Input/PROMPT_MAP.yaml`;
* place or change production markers;
* resegment manuscript prose;
* make editorial decisions;
* make BAD CUT decisions;
* invent missing `PROMPT_MAP` instructions;
* introduce a new architecture;
* create a second route;
* implement full freeze / revision / commit / acceptance / resume machinery unless the current STEP explicitly includes a pilot-required piece;
* resurrect stale `paired_runner.py`;
* run Git operations unless separately and explicitly authorized;
* perform unrelated refactoring;
* perform cleanup outside the current STEP;
* silently repair a new blocker outside STEP;
* continue into a new phase after reporting.

---

# 18. NO MODEL EXECUTION DURING IMPLEMENTATION ACCEPTANCE

The current work permit is:

```yaml
IMPLEMENTATION_EXECUTION: YES
STATIC_VERIFICATION: YES
NO_INFERENCE_PREFLIGHT: YES

MODEL_INFERENCE: NO
FULL_ARTICLE_RUN: NO
```

If any verification command would load the writer model or invoke actual Gemma generation:

**STOP BEFORE EXECUTION**

and report that the supposed preflight is not inference-free.

Do not redefine model execution as "preflight."

---

# 19. NO SILENT PHASE TRANSITION

Authorized state machine:

```text
STATE_0:
  CURRENT_AUTHORITIES_LOADED

→ STATE_1:
  STEP_SCOPE_CONFIRMED

→ STATE_2:
  PILOT_RUNNER_IMPLEMENTATION

→ STATE_3:
  STATIC_VERIFICATION

→ STATE_4:
  NO_INFERENCE_PREFLIGHT

→ STATE_5:
  IMPLEMENTATION_EVIDENCE_COMPLETE

→ STATE_6:
  REPORT

→ STOP
→ WAIT_FOR_EXTERNAL_ACCEPTANCE_AND_SHOGUN_GREEN
```

There is no authorized transition from `STATE_5` or `STATE_6` into production inference.

The following state is outside current authority:

```text
FULL_ARTICLE_INFERENCE
```

It requires a new explicit activation.

---

# 20. TEC / METSUKE CHECK

Before each substantial action, confirm:

```yaml
TEC_CHECK:
  PROJECT: MANUSCRIPT_PRESS
  ROLE: SAMURAI_EXECUTOR
  ACTIVE_MODE: IMPLEMENTER

  ACTIVE_OPERATION: PILOT_PRODUCTION_RUNNER_IMPLEMENTATION

  SPEC:
    version: v3.2.2
    role: TARGET_ARCHITECTURE
    rewrite_authority: NONE

  PILOT_EXECUTION_PROFILE:
    role: CURRENT_TEMPORARY_EXECUTION_AUTHORITY

  STEP:
    role: APPROVED_TECHNICAL_INSTRUCTION
    modification_authority: NONE

  CURRENT_PROMPT:
    role: CURRENT_EXECUTION_POSITION

  TECHNICAL_ROUTE:
    status: LOCKED
    redesign_authority: NONE

  FULL_ARTICLE_INFERENCE:
    status: LOCKED

  GREEN_LIGHT:
    status: NO

  GIT_AUTHORITY:
    status: NONE_UNLESS_EXPLICITLY_GRANTED

  DRIFT_CHECK:
    status: OK_OR_STOP
```

If any field no longer matches reality:

**STOP → REPORT METSUKE DESYNCHRONIZATION**

Do not continue from remembered state.

---

# 21. EXECUTION SENSORS

This is a narrow implementation with a dangerous boundary between "runner ready" and "runner executed."

Use concise session telemetry after substantial transitions.

Do not create extra sensor files unless STEP explicitly requires one.

Required form:

```yaml
SENSOR:
  STATE: <current authorized state>
  OBSERVED: <literal physical fact>
  EVIDENCE: <file / command / output / path>
  DRIFT_CHECK: OK / STOP
  NEXT_WITHIN_CURRENT_AUTHORITY: <next authorized action>
```

Emit at minimum:

1. after current STEP + authority frame are loaded;
2. after allowed file scope is established;
3. after implementation changes are complete;
4. after static verification;
5. after no-inference preflight;
6. immediately before final report.

At the final sensor:

```yaml
SENSOR:
  STATE: IMPLEMENTATION_EVIDENCE_COMPLETE
  OBSERVED: <literal result>
  EVIDENCE: <actual evidence>
  DRIFT_CHECK: OK / STOP
  NEXT_WITHIN_CURRENT_AUTHORITY: REPORT_THEN_STOP
```

Never emit:

```text
NEXT: RUN_FULL_ARTICLE
```

under the current prompt.

---

# 22. EVIDENCE DISCIPLINE

Hard rule:

**NO EXECUTION CLAIM WITHOUT EXECUTION EVIDENCE.**

Distinguish:

* code written;
* code parsed/compiled;
* preflight passed;
* runner ready;
* inference executed;
* manuscript generated.

These are different states.

Do not collapse them.

A successful `py_compile` proves syntax only.

A successful no-inference preflight proves only what that preflight physically checks.

Neither proves:

* successful Gemma inference;
* successful all-marker execution;
* successful continuity across the real article;
* successful protected restoration under real model output;
* successful final article assembly;
* successful `Output/FINAL.manuscript.md` creation;
* completion of SPEC v3.2.2 runtime.

Those claims require later physical execution evidence.

---

# 23. IMPLEMENTATION ACCEPTANCE EVIDENCE

The final report must include the evidence explicitly required by current STEP.

At minimum preserve the distinction:

```yaml
IMPLEMENTATION_REPORT:
  scope_claim: PILOT_PRODUCTION

  files_created_or_modified:
    - <actual paths only>

  implementation:
    status: COMPLETED / BLOCKED / FAILED
    route_changed: false
    spec_rewritten: false

  py_compile:
    executed: true / false
    command: <actual>
    result: PASS / FAIL / NOT_RUN
    evidence: <literal>

  preflight:
    executed: true / false
    inference_free: true / false
    command: <actual>
    result: PASS / FAIL / NOT_RUN
    evidence: <literal>

  production_inputs_modified: false

  full_article_inference_executed: false
  full_production_run_executed: false

  final_manuscript_claimed_generated: false

  pilot_not_full_spec_runtime: true

  blockers:
    - <actual blockers or none>

  next:
    WAIT_FOR_EXTERNAL_ACCEPTANCE_AND_SHOGUN_GREEN
```

If physical STEP requires a more specific report schema, use that schema and preserve all of the authority/evidence distinctions above.

Do not fabricate evidence fields.

---

# 24. STOP CONDITIONS

STOP immediately if any of the following occurs:

### AUTHORITY STOP

* STEP conflicts materially with the locked Grok route;
* a required action is outside the explicit STEP;
* a new architectural choice appears;
* a request would modify SPEC;
* a request would modify STEP;
* a request would silently expand the pilot profile;
* an instruction would move directly into full inference without new GREEN LIGHT.

### SCOPE STOP

* a file outside STEP scope must be modified;
* production input content would need manual editorial modification;
* marker placement or segmentation would need changing;
* `PROMPT_MAP` would need human repair;
* an unrelated blocker is discovered.

### EVIDENCE STOP

* required evidence cannot be physically obtained;
* observed state contradicts the report;
* `py_compile` fails and resolution would require work outside STEP;
* preflight fails and resolution would require route redesign;
* a claimed PASS cannot be supported by physical output.

### RUNTIME-SAFETY STOP

* a supposed preflight would start Gemma inference;
* full article execution would begin;
* context validation requires unauthorized truncation / split / omission;
* protected-slot integrity cannot be preserved;
* structural headings would have to become free model prose contrary to route;
* a partial final output could be mistaken for successful completion.

On STOP:

```text
PRESERVE EVIDENCE
→ REPORT FACTUAL BLOCKER
→ DO NOT EXPAND SCOPE
→ WAIT
```

---

# 25. FAILURE DOES NOT AUTHORIZE REDESIGN

If implementation reveals a blocker:

do not branch into exploratory engineering.

Do not trial-and-error alternative routes.

Do not switch entrypoints.

Do not weaken validation.

Do not suppress a failure.

Do not add a "temporary" workaround that changes architecture.

Report:

```yaml
BLOCKER_REPORT:
  state: <where stopped>
  observed: <literal fact>
  evidence: <physical evidence>
  affected_requirement: <STEP requirement>
  route_change_required: yes / no / unknown
  action_taken_outside_scope: none
  next: WAIT_FOR_SENSEI_GROK_SHOGUN
```

Then STOP.

---

# 26. COMPLETION DOES NOT AUTHORIZE CONTINUATION

Even if all implementation checks pass:

```text
IMPLEMENTATION COMPLETE
≠ TECHNICAL ACCEPTANCE
≠ SHOGUN GREEN LIGHT
≠ FULL ARTICLE RUN
```

The completed implementation must leave the system in a non-running state.

Required closure:

```text
IMPLEMENT
→ VERIFY
→ PREFLIGHT
→ REPORT
→ STOP
```

After STOP:

```yaml
ACTIVE_POSITION: WAIT_FOR_EXTERNAL_ACCEPTANCE
FULL_ARTICLE_INFERENCE: LOCKED
GREEN_LIGHT: NO
```

---

# 27. SUBSEQUENT FULL RUN GATE

The later full article pilot run may occur only after the required implementation acceptance has been completed and an explicit new GREEN LIGHT has been supplied.

Do not infer that GREEN LIGHT from:

* Grok's existing STEP sign-off;
* DeepSeek having written STEP;
* this Current_Prompt;
* successful implementation;
* successful `py_compile`;
* successful preflight;
* existence of production inputs;
* existence of a BAT file;
* the runner being technically executable;
* conversation history.

The long run requires a new explicit authority event.

Final execution authority remains:

**Author / Shogun.**

---

# 28. END CONDITION

This Current_Prompt authorizes exactly one current operation:

**implementation and no-inference acceptance preparation of the approved MANUSCRIPT_PRESS PILOT_PRODUCTION runner.**

It does not authorize the full article run.

At completion:

```text
IMPLEMENTATION_REPORT
→ STOP
→ RETURN TO EXTERNAL REVIEW
→ WAIT FOR AUTHOR / SHOGUN
```

Do not launch the full production inference.

Do not proceed automatically.

**STOP.**
