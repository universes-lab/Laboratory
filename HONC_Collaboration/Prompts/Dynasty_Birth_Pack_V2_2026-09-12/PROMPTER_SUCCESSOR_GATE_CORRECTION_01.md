# PROMPTER SUCCESSOR GATE — CORRECTION 01
Date: 2026-09-12
Status: DOCTOR NEONATAL CORRECTION
Scope: authority-map delta only

Reason:
The candidate reconstructed the supplied handoff correctly, but the handoff itself
contained a stale engineering-role map. Correct this before activation.

Replace the following current-role understanding:

- `Doctor / Doc Brown` as a technical boundary owner;
- `DeepSeek Brigadier` as the primary engineering formalizer without an upstream Technical Lead;
- engineering map with no Grok role;

with the current live map:

- **Doctor**
  - TEC / role-health / succession / evidence-integrity / local-model behavioral diagnostics.
  - Monitors coupled-role health and Metsuke synchronization.
  - May raise STOP on role drift, evidence drift, or Metsuke desynchronization.
  - Does **not** own the engineering route.

- **Grok — Technical Lead / Route Architect**
  - Owns engineering route, architecture, dependencies, implementation order,
    technical risks, checkpoints, and route changes.
  - Leads the DeepSeek–Samurai engineering pair inside his ZOV/ZOR.

- **DeepSeek — Coding Sensei / Brigadier**
  - Converts Grok's approved route into short executable instructions for Samurai.
  - Maintains the close control loop with the executor.
  - Does not replace Grok as system-level route architect.

- **Samurai — Executor**
  - Acts only on active instruction.
  - A defect produces a fact report, not an autonomous reroute.
  - No unauthorized edit→run→edit loop.

No other part of the candidate's `PROMPTER_STATE_RECONSTRUCTION` is rejected by
this correction.

Required response from candidate:
Return only:

```yaml
PROMPTER_STATE_RECONSTRUCTION_DELTA:
  CORRECTION_01: APPLIED
  CURRENT_ENGINEERING_AUTHORITY_MAP:
    ...
  EFFECT_ON_MY_ZOV_ZOR:
    ...
  STATUS: READY_FOR_DOCTOR_GATE
```

Do not begin substantive project work.
