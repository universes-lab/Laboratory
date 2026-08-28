# CLAUDE SUCCESSOR CORPUS — READ ME FIRST
## AI-Sociology / Editorial Recovery

### PURPOSE

This is a curated recovery view for the successor Chief Scientific Editor.

The historical repository remains untouched.
Copies are grouped only to expose precedence and function.

The predecessor Claude archive is intentionally stored OUTSIDE this package and
must be connected only after the current editorial corpus has been received.

---

# 1. ACTIVE SUCCESSOR PACK

Create:

`AI-Sociology/01_Theory/Claude_Successor_Pack/`

Recommended structure:

```text
Claude_Successor_Pack/
│
├─ 00_CONTROL/
│  ├─ 00_READ_ME_FIRST.md
│  ├─ CLAUDE_CHIEF_SCIENTIFIC_EDITOR_SUCCESSOR_SYSTEM_PROMPT.md
│  ├─ CLAUDE_EDITOR_FIRST_TASK_STATE_RECONSTRUCTION.md
│  └─ AI_Sociology_Editorial_Decision_Ledger_Addendum.md
│
├─ 01_CURRENT_FULL/
│  └─ 3.Corrections.md
│
├─ 02_LATEST_PATCHES/
│  ├─ 4.Corrections_FINAL.md
│  └─ 5.Corrections_03.md
│
├─ 03_EDIT_CHAINS/
│  └─ [copy of the current Edits folder; preserve original filenames]
│
├─ 04_EARLIER_STATE/
│  ├─ 1.Beyond Prompt Engineering.md
│  └─ 2.Editorial reports.md
│
└─ 05_INDEPENDENT_REVIEW/
   └─ Qwen - Corrections.md
```

Do not move or rename the historical originals.
The pack contains copies only.

---

# 2. PREDECESSOR ARCHIVE — SEPARATE

Create a separate sibling folder:

`AI-Sociology/01_Theory/Claude_Predecessor_Archive/`

containing:

```text
Claude_Predecessor_Archive/
└─ Claude - Beyond Prompt Engineering.md
```

Do NOT connect this folder to the successor Claude yet.

Status:

> PREDECESSOR ARCHIVE = PROVENANCE, NOT CANON

It is read last.

---

# 3. PRECEDENCE MODEL

## A — CURRENT FULL CANDIDATE

`3.Corrections.md`

Identified by the Author as the most current full manuscript-level candidate.

It is not automatically final.
Later point patches may supersede parts of it.

## B — LATER POINT PATCHES

In order:

1. `4.Corrections_FINAL.md`
2. `5.Corrections_03.md`

Treat these as targeted patches, not whole-manuscript replacements.

The successor editor must identify exactly what each patch supersedes.

## C — LOCAL EDIT CHAINS

`Edits/`

Author-reported workflow chronology:

`Section → Block → Revisions`

These files are local edit history.

Do not assume that every local edit was integrated into `3.Corrections.md`.

For every target manuscript section reconstruct:

- base text;
- Section-stage edit;
- Block-stage edit;
- Revisions-stage edit;
- whether the latest local revision appears in the current full candidate;
- whether a later point patch supersedes it.

If target or precedence is unclear:

`OPEN POINT`

Do not guess.

## D — EARLIER FULL STATE / EDITORIAL RATIONALE

`1.Beyond Prompt Engineering.md`
`2.Editorial reports.md`

The first is an earlier manuscript state.
The second is editorial analysis/rationale, not manuscript canon by itself.

## E — INDEPENDENT ONTOLOGY/REVIEW TRACE

`Qwen - Corrections.md`

Use as ontology/evidence/provenance review material.

Conversational statements inside it are not automatically current canon.
Cross-check explicit corrections against the current correction chain.

## F — PREDECESSOR CHAT

`Claude - Beyond Prompt Engineering.md`

Read only after A–E have been received.

It may contain obsolete terminology, abandoned hypotheses, intermediate edits,
later-corrected confidence, and useful rationale.

Never restore a formulation solely because the predecessor wrote it.

---

# 4. `Edits/` — DO NOT OVER-SORT BY HAND YET

For the first recovery pass, preserve the existing `Edits/` filenames and folder
structure inside `03_EDIT_CHAINS/`.

Do NOT spend the Author's time manually rebuilding all Section/Block/Revisions
chains before the successor editor has inspected them.

The successor's MODE A task includes producing the section map.

Only if the filenames are too ambiguous for Claude should an auxiliary ARCHIVIST
be used to generate a mechanical manifest.

---

# 5. INGESTION SEQUENCE

The successor Claude already has:

- role contract;
- decision-ledger addendum;
- reconstruction task.

Next:

### STEP 1
Connect only:

`Claude_Successor_Pack/`

Tell Claude:

`CURRENT EDITORIAL CORPUS CONNECTED. Do not execute MODE A yet. Inventory access only. Reply RECEIVED — ANALYSIS DEFERRED.`

### STEP 2
If Claude confirms access, connect separately:

`Claude_Predecessor_Archive/`

Tell Claude:

`PREDECESSOR ARCHIVE CONNECTED LAST. Status: PROVENANCE, NOT CANON. Do not execute MODE A yet. Reply RECEIVED — ANALYSIS DEFERRED.`

### STEP 3
Then send:

`INPUT COMPLETE — EXECUTE MODE A`

Only then may Claude produce:

`EDITORIAL_STATE_RECONSTRUCTION.md`

---

# 6. FILE-LIMIT STRATEGY

Prefer connected GitHub folders over many individual attachments.

If consolidation becomes necessary, concatenate only within the same source layer
and preserve exact boundaries:

```text
===== BEGIN FILE: exact_filename =====
...
===== END FILE: exact_filename =====
```

Never create one anonymous mega-file mixing:
- current corrections;
- Qwen review;
- predecessor Claude archive.

---

# 7. OPTIONAL ARCHIVIST

Do not use one unless Claude cannot map `Edits/`.

If needed, the archivist may only:

- inventory filenames;
- map apparent target sections;
- group Section / Block / Revisions;
- detect exact duplicates;
- produce `ARCHIVE_MANIFEST.md`.

It may not:

- choose canonical wording;
- resolve contradictions;
- rewrite text;
- decide scientific precedence where it is not explicit.

---

# 8. FINAL RULE

> Reconstruct editorial state first. Edit second.

The archive is evidence of the path, not a substitute for the current manuscript.
