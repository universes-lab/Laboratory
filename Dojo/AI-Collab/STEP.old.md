# STEP.md — AI-Collab

BUILD: 001
STEP: 1
NAME: FIXTURE_SERVER
STATUS: ACTIVE

REQUIRED_MODE: IMPLEMENTER

PROJECT:
  AI-Collab

ROOT:
  E:\Gemini\Dojo\AI-Collab

TECHNICAL_AUTHORITY:
  SPEC.md — BUILD 001 / STEP 1 — FIXTURE SERVER (v1.1)

---

## OBJECTIVE

Implement the complete BUILD 001 / STEP 1 fixture server defined by
`SPEC.md`.

This STEP activates the SPEC.

It does not modify or reinterpret it.

---

## AUTHORIZED WORK

Perform only the implementation, local verification, and reporting required
by SPEC.md.

Allowed project artifacts, runtime behavior, endpoints, self-test,
non-goals, forbidden areas, and STOP conditions are exactly those defined
by SPEC.md.

Do not duplicate them here with alternative wording.

---

## VERIFY

Execute the verification required by SPEC:

`python fixture_server.py --self-test`

Record the actual result and exit code.

PASS may be reported only from actual execution evidence.

---

## REPORT

Return:

`BUILD_001_STEP_1_REPORT`

using the schema defined in SPEC.md.

Report factual state only.

If the STEP is blocked, report the exact blocker and evidence instead of
manufacturing PASS.

---

## END STATE

On successful completion:

REPORT
→ STOP
→ WAIT_FOR_GROK_OR_SHOGUN

On a blocking failure or authority ambiguity:

STOP
→ REPORT
→ WAIT_FOR_GROK_OR_SHOGUN

No automatic transition to another STEP.

END OF STEP
