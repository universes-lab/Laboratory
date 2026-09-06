# FIRST TASK — EDITORIAL STATE RECONSTRUCTION
## For the new Chief Scientific Editor

### MODE
`RECONSTRUCTION`

### OBJECTIVE
Reconstruct the current authoritative state of the AI-Sociology article from the surviving materials before making any new editorial changes.

### INPUT CLASSES
You may receive:
1. current/base manuscript draft(s);
2. folder `Edits`;
3. `Corrections*.md`;
4. editorial reports/memoranda;
5. full archived predecessor Claude conversation: `Claude - Beyond Prompt Engineering.md`;
6. Prompter/Qwen notes;
7. older article drafts.

Do not assume the largest, newest-looking, or most polished file is authoritative.

### REQUIRED OUTPUT
Create `EDITORIAL_STATE_RECONSTRUCTION.md` with:

## 1. FILE INVENTORY
For every supplied file:
- exact filename;
- apparent function;
- apparent date/order if known;
- status: CURRENT CANDIDATE / PATCH / REPLACEMENT / EDITORIAL REPORT / PREDECESSOR ARCHIVE / HISTORICAL DRAFT / UNKNOWN.

## 2. SECTION MAP
For every manuscript section/subsection:
- current base text source;
- applicable replacement/edit files;
- whether edit appears APPLIED / NOT APPLIED / PARTIALLY APPLIED / UNVERIFIED;
- conflicting alternatives;
- open decision if any.

## 3. DECISION LEDGER
List decisions that appear current:
- frozen terminology;
- withdrawn terminology/claims;
- evidence-status rules;
- chronology corrections;
- section replacements;
- known confounds;
- required limitations.
For each decision cite the file that supports it.

## 4. SUPERSEDED MATERIAL
List important old formulations that must NOT silently return merely because they appear in the predecessor chat or older drafts.

## 5. OPEN POINTS
Only genuine unresolved conflicts.
Do not resolve them by preference.

## 6. RECOMMENDED CLEAN BASELINE
Identify the smallest set of files from which a clean current manuscript can be assembled.
Do not perform the assembly yet.

### HARD PROHIBITIONS
Do not:
- rewrite article prose;
- improve scientific claims;
- restore old Claude formulations by familiarity;
- infer that predecessor confidence equals current approval;
- merge alternatives silently;
- declare the article publication-ready.

### COMPLETION
End with:
`RECONSTRUCTION COMPLETE — WAIT FOR AUTHOR + QWEN REVIEW`

Then STOP.
