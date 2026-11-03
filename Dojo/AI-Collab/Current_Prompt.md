# CURRENT OPERATIONAL FRAME

PROJECT:
AI-Colab / BUILD 001

WORKING ROOT:
E:\Gemini\Dojo\AI-Collab

ACTIVE OPERATION:
BUILD 001 / STEP 2 — VERDICT ENGINE — CORRECTIVE PASS

ACTIVE MODE:
IMPLEMENTER

ACTIVE SPEC:
E:\Gemini\Dojo\AI-Collab\SPEC.md

REQUIRED SPEC VERSION:
2.3

FINAL AUTHORITY:
Author

TECHNICAL ROUTE:
DeepSeek / Brigadier → Doctor operational frame → Samurai execution

ACCEPTANCE:
External only — Grok / Author.
Samurai does not accept STEP 2 and does not authorize STEP 3.

---

# CURRENT TASK

Perform exactly one corrective full rewrite of:

E:\Gemini\Dojo\AI-Collab\verdict_engine.py

using SPEC v2.3.

`FULL REWRITE` means:
replace the entire content of `verdict_engine.py` with a complete implementation.

It does NOT require deleting the file or recreating the path.

After rewrite, pass all completeness gates defined in SPEC v2.3 before compile or tests.

---

# MANDATORY PRE-ACTION CONFIRMATION

Before modifying anything:

1. Re-read:
   E:\Gemini\Dojo\AI-Collab\SPEC.md

2. Confirm physically from that file:

```text
BUILD: 001
STEP: 2
NAME: VERDICT_ENGINE
VERSION: 2.3
STATUS: READY_FOR_SAMURAI
```

3. Confirm:

```text
ROOT = E:\Gemini\Dojo\AI-Collab
ACTIVE_MODE = IMPLEMENTER
ACTIVE_OPERATION = BUILD 001 / STEP 2
STEP 3 = NOT AUTHORIZED
```

If SPEC version is not 2.3:

```text
STOP
REPORT SPEC_VERSION_MISMATCH
WAIT
```

Do not infer v2.3 from conversation memory.

---

# AUTHORIZED NOW

You may:

- inspect the current `verdict_engine.py`;
- run the venv preflight;
- compute `hash_before`;
- run the required before-fix greps;
- fully rewrite `verdict_engine.py`;
- compute `hash_after`;
- run completeness checks;
- verify skeleton markers are absent;
- verify Rules 2–9 are implemented as executable logic;
- run obsolete-string grep after rewrite;
- run `py_compile` only if all completeness gates pass;
- run `test_vectors.py` exactly once only if compile passes;
- capture full stdout and exit code;
- return the exact factual report required by SPEC v2.3;
- perform Samurai Execution Health closure required by the active constitution.

Use ordinary engineering judgment inside the authorized rewrite.

Do not redefine the task.

---

# HARD EXECUTION SEQUENCE

Execute only this sequence:

```text
PREFLIGHT VENV
→ READ / CONFIRM SPEC v2.3
→ GATE 1: hash_before
→ GATE 2: obsolete grep before
→ GATE 3: skeleton grep before
→ FULL REWRITE verdict_engine.py
→ GATE 4: hash_after; REQUIRE hash_after != hash_before
→ GATE 5: skeleton markers absent
→ GATE 6: Rules 2–9 implemented as executable logic
→ AFTER-FIX obsolete grep; REQUIRE zero matches
→ PY_COMPILE
→ ONE OFFICIAL test_vectors.py RUN
→ REPORT
→ STOP
→ WAIT
```

No branch may skip a gate.

---

# COMPLETENESS GATES

After the rewrite, before `py_compile`:

## Gate 4 — physical change

Required:

```text
hash_after != hash_before
```

If equal:

```text
STOP
REPORT
WAIT
```

Do not compile.
Do not test.
Do not rewrite again.

## Gate 5 — skeleton removed

These markers must be absent:

```text
см. SPEC v2.1
остальные rules 2
$pre.
$post.
```

If any remain:

```text
STOP
REPORT
WAIT
```

Do not compile.
Do not test.
Do not rewrite again.

## Gate 6 — implementation completeness

Rules 2–9 must exist as real executable logic.

Required implemented behaviors:

```text
Rule 2  NEEDS_HUMAN
Rule 3  LOST
Rule 4  CONV_ID_DIFFERS
Rule 5  PATHS_NOT_COMPARABLE
Rule 6  HISTORY_INCOMPLETE
Rule 7  PREFIX_CHANGED
Rule 7a SNAPSHOT_INCONSISTENT
Rule 8  SEND_UNRESOLVED
Rule 9  DELTA
```

Comments, TODOs, placeholders, ellipses, or reason strings without executable logic do not satisfy this gate.

If incomplete:

```text
STOP
REPORT
WAIT
```

Do not compile.
Do not test.
Do not rewrite again.

---

# AUTHORITATIVE CLARIFICATIONS

Use SPEC v2.3 exactly.

Key points:

```text
L0 path format = $.text
L0 scan order = pre → post

Rule 1:
  pre is None OR post is None
  → immediate NO_EVIDENCE
  → no cross-snapshot comparisons

Rule 2:
  session_state from post
  flags from post

Rule 3:
  session_state from post

Rule 5:
  PATHS_NOT_COMPARABLE

Rule 6:
  HISTORY_INCOMPLETE

E10:
  known vector/contract mismatch
  implementation follows contract
  decisive_rule must be "5"
  do not bend code to force E10 PASS
```

---

# EXPECTED TEST STATE — NOT A FACT UNTIL OBSERVED

Expected only:

```text
31/32 vectors PASS
failed_ids == ["E10"]
L0_GUARD PASS
runner exit code = 1
```

This expected exit code 1 is not by itself an implementation defect.

Do not report expected values as observed values.

---

# STRICT ONE-PASS BOUNDARY

This operation authorizes one implementation pass only.

No second rewrite.

No patch cycle after the rewrite.

No retry after a failed completeness gate.

No retry after compile failure.

No retry after the official test run.

If any unexpected failure occurs:

```text
STOP
REPORT FACTUAL EVIDENCE
WAIT FOR EXTERNAL REVIEW
```

The generic Samurai retry allowance does not override this narrower operational frame.

---

# NOT AUTHORIZED

Do not:

- modify `BUILD_001_STEP2_VECTORS.json`;
- modify `test_vectors.py`;
- modify `BUILD_001_STEP2_STEP3_SPEC.md`;
- modify `WEB_SEAT_WS0_OBSERVATION_CONTRACT.md`;
- modify `AI_COLAB_2_BUILD_CONTRACT_001.md`;
- modify `SPEC.md` during execution;
- implement STEP 3;
- recompute fingerprints;
- invent reasons;
- add catch-all `pre != post`;
- merge Rule 5 and Rule 6;
- special-case E10 to force PASS;
- skip E10;
- create a replacement test runner;
- delete `verdict_engine.py` merely to satisfy “full rewrite”;
- perform unrelated refactor / cleanup / rename / migration;
- infer authorization from conversation history or previous passes.

---

# REPORTING

Return exactly one factual `STEP2_CORRECTIVE_REPORT` conforming to SPEC v2.3.

It must include at minimum:

```text
hash_before
hash_after
file_changed
skeleton_markers_after
rules_2_to_9_implemented
py_compile status
full test stdout
test exit code
failed_ids
L0_GUARD result
step2_handoff_ready
```

If the operation stops before compile/test, report the exact gate where it stopped and the evidence.

---

# ACCEPTANCE BOUNDARY

If observed state is exactly:

```text
31/32
failed_ids == ["E10"]
L0_GUARD PASS
```

then:

```text
step2_handoff_ready: yes
```

But do NOT write:

```text
STEP 2 ACCEPTED
STEP 3 AUTHORIZED
```

After report:

```text
STOP
WAIT FOR EXTERNAL REVIEW
```

END OF CURRENT OPERATIONAL FRAME
