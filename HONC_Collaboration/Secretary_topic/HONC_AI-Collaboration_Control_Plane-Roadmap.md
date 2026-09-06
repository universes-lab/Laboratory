# HONC AI-Collaboration Control Plane — Roadmap

Status: Research / Pre-Architecture
Updated: 2026-08-19

## 1. Current State

Discovery — CLOSED.
Mapping — CLOSED.
Architecture — NOT OPENED.

Final Mapping:

| Block | Status |
|---|---|
| Endpoint access | PATTERN |
| Message Store / Mailbox | ADAPTABLE |
| Envelope / CAS | PATTERN |
| Durable execution / timers / recovery | READY |
| Identity / role / triad registry | PATTERN / partially ADAPTABLE |
| Metadata–BODY isolation | PATTERN |
| Deliberation state | MISSING |
| Provenance model | PATTERN |
| Provenance backend | ADAPTABLE |
| Human Control Room | PATTERN |

H0 DeepSeek:
diagnostic prototype only.
Not an architecture baseline and not an implementation start.

## 2. Fixed Architectural Principles

1. The Author must cease to be the manual data bus of the collaboration.

2. The system is treated as an Organizational Control Plane with
   separate data/address/control functions.

3. Endpoint Adapter:
   deterministic mechanism;
   technical access to BODY;
   no semantic visibility.

4. Secretary:
   intelligent organizational subject;
   semantic visibility of metadata;
   no technical access to BODY.

5. Interpretation of informal Author commands and deterministic routing
   are separate functions.

6. Organizational state, communication state, deliberation state and
   knowledge provenance are different state classes and must not be collapsed.

7. Social graph and provenance/workflow graph are separate but linked.

8. Internal delivery model and external endpoint wake-up mechanism are
   separate architectural axes.

9. Security boundary:
   Secretary and BODY-handling components must operate under different
   security principals with non-identical access rights.

10. Technology candidates remain candidates until Architecture.
    Temporal, Playwright, React Flow, OPA, SQLite, H0 etc. are NOT selected stack.

## 3. Pre-Architecture Gate

Two checks remain before Architecture.

### A. Endpoint Empirical Spike

Purpose:
verify that a sufficiently stable primitive exists for:

address existing long-lived chat
→ send
→ detect response completion
→ extract only the new response
→ recover after failure.

Endpoint Spike v3.x:
methodologically accepted after the final wording correction:
API self-report is per-call;
DOM self-report may require account-level configuration.

Active spike does not automatically determine the production transport.

### B. Isolation Verification

Targeted verification only.

Determine for metadata/BODY separation:

- what exists as working code;
- what exists as a standard;
- what is only a proposal/pattern;
- whether anything can be classified ADAPTABLE rather than PATTERN.

No new broad search.

## 4. Architecture Questions

Architecture opens only after the Pre-Architecture Gate.

First decisions:

1. Interpreter-subject ↔ deterministic router separation.
2. Ownership and representation of deliberation state.
3. Mailbox / Inbox / Messenger internal delivery model.
4. Structural BODY isolation.
5. Author-visible recovery/escrow policy, if BODY encryption is used.
6. Relationship between wake and self-report.
7. Human Control Room representation of:
   - organizational graph;
   - workflow/provenance graph;
   - deliberation state;
   - task/status/timing state.

Only here may concrete carriers and technologies be selected.

## 5. Immediate Next Actions

NOW:
1. Freeze Mapping.
2. Freeze Endpoint Spike specification after the one-line wording correction.
3. Run Endpoint Spike.
4. Perform targeted Isolation verification.

THEN:
5. Record results in this Roadmap.
6. Open Architecture Phase.
7. Developers DeepSeek + Claude generate architecture alternatives.
8. Qwen checks ontology/ZOV-ZOR boundaries.
9. Methodologist integrates the architecture map.
10. Author selects the architecture direction.

NOT NOW:
- no Courier implementation;
- no Secretary implementation;
- no database schema;
- no production stack selection;
- no dashboard coding;
- no expansion into another broad literature/tool search.