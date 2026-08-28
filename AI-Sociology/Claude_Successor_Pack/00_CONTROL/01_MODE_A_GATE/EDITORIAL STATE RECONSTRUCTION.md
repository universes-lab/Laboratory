# EDITORIAL STATE RECONSTRUCTION
## AI-Sociology / Beyond Prompt Engineering

**Produced by:** Chief Scientific Editor (successor instance)
**Mode:** A — RECONSTRUCTION
**Input set:** `AI-Sociology/Claude_Successor_Pack`, 25 files, complete folder tree, declared complete by the Author
**Nothing outside this folder was consulted.** No manuscript prose was written, rewritten, or repaired.

**Headline finding.** The corpus contains no assembled current manuscript. It contains a canonical block text (Blocks 1–5) to which **none** of the two latest patch packages has been applied, and one unresolved authority conflict over whether the larger of those two packages is in force at all. The conflict is stated in §5 and is not resolved here.

---

# 1. FILE INVENTORY

Status vocabulary as specified in the First Task. "Order" is reconstructed from internal cross-references and explicit supersession statements, not from filenames or timestamps.

## 00_CONTROL

| File | Function | Order | Status |
|---|---|---|---|
| `CLAUDE_CHIEF_SCIENTIFIC_EDITOR_SUCCESSOR_SYSTEM_PROMPT.md` | Role contract for this office | current | **CURRENT — governing** |
| `AI_Sociology_Editorial_Decision_Ledger_Addendum.md` | Triad boundaries D1–D4; Qwen verdict PASS | current, later than the system prompt (reviews it) | **CURRENT — governing** |
| `CLAUDE_EDITOR_FIRST_TASK_STATE_RECONSTRUCTION.md` | Specification of this document | current | **CURRENT — governing** |
| `CLAUDE_SUCCESSOR_BOOTSTRAP_MESSAGE.md` | Handover message | current | **CURRENT — procedural** |

These four are control documents, not manuscript sources. They are excluded from the section map.

## 01_CURRENT_FULL

| File | Function | Status |
|---|---|---|
| `3.Corrections.md` (32,882 words) | Composite: title block + §1 provenance note + **canonical Blocks 1–5** + the 21-item edit plan + the cumulative `REVISIONS` file | **CURRENT CANDIDATE (manuscript body) + PATCH (tail), partly SUPERSEDED** |

This file is not homogeneous and must not be treated as one object. It has three layers:

1. **Head (lines 1–28)** — title/contributor block and the §1 provenance note. Identical to the versions mandated in `4.Corrections_FINAL.md` Part IV items 4 and 5. **APPLIED**, though the §1 note sits at the head of the file rather than at the end of §1.1 or §1.2 as Part IV-5 specifies.
2. **Body (lines 29–1816)** — `BLOCK 1` … `BLOCK 5`, each carrying its own `CANONICAL` banner. This is the manuscript. Blocks 3 and 4 are byte-identical to the corresponding files in `03_EDIT_CHAINS/02_BLOCKS/`; Blocks 1, 2 and 5 differ from them only by three inline insertions, examined in §2 below.
3. **Tail (lines 1817–2412)** — the 21-item edit plan and the cumulative `REVISIONS` file. The tail is byte-identical to `03_EDIT_CHAINS/03_REVISIONS/Corrections-2.md`. `4.Corrections_FINAL.md` declares this tail absorbed and superseded.

## 02_LATEST_PATCHES

| File | Function | Status |
|---|---|---|
| `4.Corrections_FINAL.md` (8,060 words) | Patch package in six parts: §4 and §8 replacements, E6/E8 protocol replacements, eight point edits, mechanical replacements, 13 withdrawn claims, 4 open questions to the Author | **REPLACEMENT — authority disputed (see OP-1)** |
| `5.Corrections_03.md` (1,772 words) | Seven edits from the three-party Metsuke protocol (Prompter — Chief Editor — Ontology Keeper), plus four items explicitly kept out of the text | **PATCH — latest layer** |

`5.Corrections_03.md` states its own base: *«Применяется к: каноническому тексту Blocks 1–5 с учётом Corrections_FINAL.md»*. It is therefore the latest editorial layer in the corpus and it presupposes `4.Corrections_FINAL.md`. Documentary confirmation of that dependency is in §5, OP-1.

## 03_EDIT_CHAINS

### 01_SECTIONS — six files

`Section 1.md`, `Section 4 & 6.md`, `Section 5.md`, `Section 7 & 10.md`, `Section 8 & 9.md`, `Section 11 & 12.md`.

**Status: HISTORICAL DRAFT.** These are the per-section artifacts named in the assembly manifest (`05_ONTOLOGY_REVIEW/Манифест сборки…`, table rows 1–12: *«артефакт "Sections 4 & 6"»*, *«артефакт "Section 5 — complete"»*, and so on). They are the input from which Blocks 1–5 were assembled. Divergence is demonstrable: `Section 1.md` opens §1.1 as *"The problem that produced this work"*; canonical Block 1 opens §1.1 as *"How this started"*. Block 1's banner supersedes all earlier §1.

### 02_BLOCKS — five files

`Block 1 - Section 1-3.md` … `Block 5 - Section 10-12.md`.

**Status: CURRENT CANDIDATE (clean copies of the manuscript body).** Blocks 3 and 4 are byte-identical to the corresponding regions of `3.Corrections.md`. Blocks 1, 2 and 5 lack three insertions that `3.Corrections.md` carries. These are the cleanest available carrier of the block text, but they are one insertion-layer behind `3.Corrections.md`.

### 03_REVISIONS — two files

| File | Function | Status |
|---|---|---|
| `Revisions.md` (105 KB) | The cumulative `REVISIONS` file captured at **three** successive growth stages, concatenated: snapshot 1 = ЗАПИСЬ 1 only; snapshot 2 = ЗАПИСИ 1–2; snapshot 3 = ЗАПИСИ 1–4 | **PREDECESSOR ARCHIVE — growth trace, superseded** |
| `Corrections-2.md` (7,291 words) | Snapshot 3 alone. Byte-identical to the tail of `3.Corrections.md` and to the last snapshot in `Revisions.md` | **PATCH — superseded by `4.Corrections_FINAL.md`** |

Verified by exact string comparison. There is no unique content in `Revisions.md` beyond the growth history.

## 04_EARLIER_STATE

| File | Function | Status |
|---|---|---|
| `1.Beyond Prompt Engineering.md` (22,659 words) | Prompter's original draft, 25 numbered sections, bilingual, with duplicated numbering (two §1, two §6, four §9, two §10) | **HISTORICAL DRAFT — superseded in full** |
| `2.Editorial reports.md` (33,689 words) | Predecessor Editor's working reports and blocker lists on that draft | **EDITORIAL REPORT / PREDECESSOR ARCHIVE — not canonical** |

Both classifications are stated independently by the Ontology Keeper (`Qwen - Corrections.md`, document audit): the draft is *«Суперседен … Только как исторический архив»*; the reports are *«Промежуточный рабочий документ. Не канонический.»*

## 05_ONTOLOGY_REVIEW

| File | Function | Status |
|---|---|---|
| `Qwen - Corrections.md` (1,775 lines) | Long multi-round transcript: Keeper reviews, Methodologist corrections, the Author's memorandum on imprinting, the Keeper's imprinting memorandum, the four-document audit, and a Knowledge-DNA discussion outside this article's scope | **PREDECESSOR ARCHIVE — provenance, containing embedded current decisions** |
| `memorandum_ClaudePRO.md` (21 KB) | Predecessor Editor's third memorandum: Part A output requirements for the literary writer, Part B ten-field concept-package spec, plus a substantive reply on priority drift; followed by the Keeper's verdict on it | **EDITORIAL REPORT — current for the book pipeline; contains one accepted-but-unintegrated article item** |
| `Манифест сборки и комментарии к оценке Хранителя Онтологии.md` (54 KB) | Assembly manifest (12 rows, source artifact per section) + "Материал для Хранителя" main document + Дополнение 1 **duplicated verbatim** (lines 243–352 and 354–463) | **PREDECESSOR ARCHIVE — assembly manifest superseded by Blocks 1–5; §§4.1–4.4 questions still live** |

The assembly manifest predates the blocks: it records §2 Related Work as *«не написан — ждёт верифицированных ссылок»*, whereas canonical Block 1 contains §2.0–§2.11 in full.

---

# 2. SECTION MAP

**Base text for every section: `3.Corrections.md`, Blocks 1–5** (equivalently `02_BLOCKS/*`, plus the three insertions noted).

**Global applied-status finding.** The manuscript body contains **none** of the changes specified in `4.Corrections_FINAL.md` or `5.Corrections_03.md`. Measured over the block region only:

| Marker | Expected after FINAL | Found in manuscript body |
|---|---|---|
| `menom` | 14+ occurrences, §4.2 rebuilt | **0** |
| `§8.11` (Kelly subsection) | present | **absent** |
| `§4.6` cross-references | 0 (all → §4.5) | **7** |
| `four drafts` (§8.10, to be removed) | 0 | **2** |
| `The distinction generalizes` (§12.4.1) | replaced | **1, unchanged** |
| E8 sections `Object` / `Procedure` / `Pre-commitment` | present | **absent** |

Three insertions from the edit plan **were** pasted into `3.Corrections.md` by hand, in a pre-final form:

| Insertion | Location in `3.Corrections.md` | Status |
|---|---|---|
| §3.2 evidence-class table | after the closing paragraph of §3.2 | **PARTIALLY APPLIED — degraded.** Tab-separated plain text with a Russian header row (`Класс / Что содержит / n`), not the markdown table specified in FINAL III-7, and the accompanying paragraph ("The classes are not comparable in weight…") is missing. FINAL also places it immediately after *"Every other empirical statement is [R]."*, not where it sits. |
| §3.8 "The label AI Sociology" | **inside the BLOCK 2 banner**, between the banner and `# 4. Conceptual Framework` | **PARTIALLY APPLIED — misplaced and pre-final.** Belongs after §3.7 (FINAL III-8). Lacks the §4.5.4 cross-reference and the closing sentence *"We claim no priority in the term."* |
| Host-project note in §12.1 | end of §12.1 region, Block 5 | **PARTIALLY APPLIED — pre-final.** Shorter than the FINAL III-6 wording; the paired §2.11 replacement is **NOT APPLIED**. |

## Section-by-section

Legend: **NA** = not applied · **PA** = partially applied · **A** = applied · **UNV** = unverified

### Block 1 — §1–§3

| Section | Applicable edits | Status |
|---|---|---|
| §1.1–§1.3 | Part IV-5 provenance note (currently at file head) | PA — placement open |
| §1.4 | IV-1 `§4.6 → §4.5` | NA |
| §1.5 | III-1 pattern reformulation (first paragraph) | NA |
| §1.6–§1.10 | none | — |
| §2.0 | III-4 ⚠ marking extends to whole paper | NA |
| §2.1–§2.8 | none | — |
| §2.9 | IV-1 `§4.6 → §4.5` | NA |
| §2.10 | Corrections_03 ПРАВКА 5 — conversation-boundary limitation | NA |
| §2.11 | III-6 host-project paragraph, full replacement | NA |
| §3.1 | none | — |
| §3.2 | III-7 class table | PA — degraded, see above |
| §3.3–§3.4 | none | — |
| §3.5 | III-3 `behavioural prior → menom` in the vocabulary list | NA |
| §3.6 | **Open question VI-1**; plus the further disclosure link proposed in `memorandum_ClaudePRO.md` | NA — Author decision |
| §3.7 | none | — |
| §3.8 | III-8, new subsection | PA — misplaced, pre-final |

### Block 2 — §4–§5

| Section | Applicable edits | Status |
|---|---|---|
| **§4 entire** | **FINAL I-1 — full replacement of §4.1–§4.6.** Introduces §4.2.1–§4.2.5 (rule core; withdrawal of "behavioural DNA"; *menom*; the no-carrier claim; menom↔rule-core relation) and §4.5.1–§4.5.6 (two boundaries; ZOV four components; ZOR five components; actual vs represented; asymmetry; memes/memocode ≠ ZOV/ZOR). Old §4.5 and §4.6 merge into §4.5; Kelly comparison leaves §4.5 for §8.11 | **NA — the single largest unapplied change** |
| §5.2 | III-5 Appendix A reference | NA |
| §5.4 C2 | III-2 count rule, prompts A=5 / B=3 with explicit counting rule and table | NA |
| §5.4 "Discriminating experiments" | III-5 E3/E4/E1 numbering | NA |
| §5.5, §5.8 | IV-1 `§4.6 → §4.5` (three occurrences) | NA |
| §5.5 | **Open question VI-2** — whether to keep the concession detail | NA — Author decision |
| §5.6 | **Open question VI-3** — transcript plus confirmation of no role prompt on resumption | NA — Author decision |
| §5.7 | **Open question VI-4** — n = 1 or n = 2 clean runs | NA — Author decision |
| §5.9 | III-1 pattern reformulation, final paragraph replaced in full | NA |

### Block 3 — §6–§7

| Section | Applicable edits | Status |
|---|---|---|
| §6.2 | III-2 addition after the v1/v3 table | NA |
| §6.3 | Proposed insertion point for **priority imprinting** (Keeper's memorandum) — would renumber current §6.3–§6.6 | NA — see OP-3 |
| §6.4 | III-3 third paragraph replaced; *family-level menom* | NA |
| §6.1, §6.5, §6.6 | none | — |
| §7.1–§7.10 | none | — |

### Block 4 — §8–§9

| Section | Applicable edits | Status |
|---|---|---|
| §8.7 | FINAL I-2d, addition at end of section | NA |
| §8.9 | FINAL I-2a full replacement → **then** Corrections_03 ПРАВКА 3 (configuration vs procedure) inserted before *"The literature addresses Axis 2"* | NA, chained |
| §8.10 | FINAL I-2b full replacement (removes "four drafts", fixes "ontological review") → **then** Corrections_03 ПРАВКА 1 (procedural qualification) inserted before *"This is a record of what occurred"* | NA, chained |
| §8.11 | FINAL I-2c, new subsection — Kelly apparatus, §8.11.1–§8.11.4 | NA |
| §9.1–§9.11 | none | — |

### Block 5 — §10–§12

| Section | Applicable edits | Status |
|---|---|---|
| §10.3 | IV-1 `§4.6 → §4.5` | NA |
| §10.4 | Corrections_03 ПРАВКА 6 — detection function belongs to a position, not a person | NA |
| §11.3 | Corrections_03 ПРАВКА 4 — work mode vs diagnostic mode; what does not establish independence; shared evidence vs shared interpretation | NA |
| §11.4 E6 | FINAL Part II replacement, ⚠ marked; wording depends on verification of Choi et al. | NA — blocked on reference check |
| §11.4 E8 | FINAL Part II replacement (repertory-grid protocol) → **then** Corrections_03 ПРАВКА 2 replaces its *Object* and *Pre-commitment* and adds a fifth *Procedure* item | NA, chained |
| §11.4 Priority | FINAL Part II, replacement line | NA |
| §12.1 | III-3 `behavioural DNA → menom`; III-6 host-project item | PA — host-project note present in pre-final wording; III-3 NA |
| §12.2 | III-4 ⚠ before the accommodation claim | NA |
| §12.4.1 | Corrections_03 ПРАВКА 7 — *"The distinction generalizes"* → *"This suggests a general distinction, on the evidence of one case."* | NA |
| §12.7 | III-1 pattern reformulation in "What the evidence supports" | NA |

### Whole-manuscript mechanical operations (FINAL Part IV) — all NA

1. `§4.6 → §4.5`, seven occurrences (§1.4, §2.9, §5.5 ×2, §5.8, §8.9, §10.3) — all seven still present.
2. Remove `behavioural DNA` / `behavioral DNA` / `model DNA` everywhere except §4.2.2 — two occurrences remain in the body.
3. `behavioural prior` retained only where it denotes observed family behaviour; otherwise → *menom*. Six occurrences to audit, §6.4 and §12.1 named.
4. Title block — **A**.
5. §1 provenance note — **PA**, placement open.

### Missing components

- **Appendix A** is referenced five times in the manuscript (protocol, exact intervention texts, complete unedited responses). It is **not present in the corpus**.
- No **title, abstract, or reference list** exists for the block text. The earlier draft had an abstract; the blocks do not.

---

# 3. DECISION LEDGER

Each entry cites the file that supports it. Entries are those that appear current; disputes are in §5.

## 3.1 Frozen terminology

| Term | Support |
|---|---|
| **menom** — organized system of memes/memoframes/memocode; **no localized carrier and no transmission claim** in the definition | `4.Corrections_FINAL.md` I-1 §4.2.3–§4.2.5; `Qwen - Corrections.md` (Keeper accepts the Editor's stronger formulation over his own) |
| **rule core** — distinct from menom, unobservable; what is observable is behaviour | `4.Corrections_FINAL.md` I-1 §4.2.1, §4.2.5; `Манифест…` §1.2, §1.3 |
| **ZOV / ZOR** — four and five components respectively; **actual vs represented** distinction is load-bearing | `4.Corrections_FINAL.md` I-1 §4.5.1–§4.5.4; `Qwen - Corrections.md` (*«онтологический прорыв»*, accepted) |
| **represented social position**, **represented social source** | relocated to §4.5.4 by I-1; `4.Corrections_FINAL.md` IV-1 |
| **role inertia**, **context imprinting** | Blocks 3, §6.1–§6.2 |
| **functional heterogeneity** / **carrier heterogeneity** (Axis 1 / Axis 2) | `4.Corrections_FINAL.md` I-2a; `Манифест…` Дополнение 1 §9 |
| **controlled blindness** | Block 4, §9.6 |
| **priority drift** | `memorandum_ClaudePRO.md` Part A frozen list — **but see OP-3 for the naming conflict** |
| **AI Sociology** — a label for a research direction, not a discipline and not a first use | `4.Corrections_FINAL.md` III-8; `Манифест…` Дополнение 1 §11 |

Standing rule, from `memorandum_ClaudePRO.md` Part A item 4: defined terms are used exactly, every time; elegant variation is a defect.

## 3.2 Evidence-status rules

- Four labels **[P] / [P-A] / [R] / [H]**, defined in §3.1 and enumerated in §3.2. Support: Block 1.
- Complete evidence base: **one** designed experiment, one observation per condition, nothing replicated; **four** [P-A] ancillary observations; everything else [R]. Support: §3.2.
- Raising status through prose is *"the single most damaging error possible here"*. Support: `memorandum_ClaudePRO.md` Part A item 1.
- No causal connective may be supplied that the material does not authorize; nine named confounds exist precisely because causes are unknown. Support: `memorandum_ClaudePRO.md` Part A item 2.
- **Procedural vs Outcome evidence** — the distinction is **accepted and implemented in substance** (Corrections_03 ПРАВКА 1, 2, 4) but **is deliberately not introduced as a terminological pair**. Support: `5.Corrections_03.md`, section «Что в текст не входит».
- Independence of judgment is established **procedurally, before the fact**, never recovered retrospectively; neither agreement nor disagreement establishes it; self-report does not establish it (§5.5). Support: `5.Corrections_03.md` ПРАВКА 4.
- ⚠ marks any reference not checked against its source, throughout the paper. Four references verified: Rahwan, Swanson, Du, Zhang. Choi unverified. Support: `4.Corrections_FINAL.md` III-4, Part VI.

## 3.3 Chronology and provenance corrections

- Calendar dates were not recorded and are **not** to be reconstructed from memory; the version confound (C6) can be named, not bounded. Support: §3.7.
- The §1.1–§1.2 account was written by the participant who produced those formulations; withdrawals are stated in the superseding section. Support: `4.Corrections_FINAL.md` IV-5.
- The framework of §4 was formulated **before** the experiment of §5; the experiment tested part of it. Support: Block 2 opening.
- The collaboration charter quoted in §8.1 predates the paper and is preserved unmodified. Support: Block 4.

## 3.4 Known confounds and required limitations

- Nine named confounds C1–C9 in §5.4; C9 (platform persistence mechanisms differ by family) is present in the canonical Block 2.
- §10.6 — the coordinator is the sole global observer **and** the principal confound.
- §12.1 — single project; host-project dependence (asymmetric: interpretation independent, existence dependent).
- §12.2 — simulated peer review is not external validation.
- §12.4 / §12.4.1 — manufactured consensus, including the project's own, with one documented instance; the generalization is weakened by Corrections_03 ПРАВКА 7.
- §8.10 — no exchange in the preparation of this paper was conducted under pre-comparison isolation; the observation is outcome evidence without matching procedural evidence. Support: `5.Corrections_03.md` ПРАВКА 1.
- §2.10 — a visually empty conversation is not evidence of context isolation; where isolation matters it is either secured or recorded as `UNVERIFIED CONTEXT INDEPENDENCE`. Support: `5.Corrections_03.md` ПРАВКА 5.

## 3.5 Section replacements accepted in the record

| Target | Replacement | Source |
|---|---|---|
| §4.1–§4.6 | full rewrite with menom and merged ZOV/ZOR | plan items 15, 16, 18; `4.Corrections_FINAL.md` I-1 |
| §8.9 | two axes, Methodologist's terminology | plan item 21; I-2a |
| §8.10 | editor's note, corrected | plan item 6; I-2b |
| §8.11 | Kelly apparatus, new | plan item 19; I-2c |
| §11.4 E8 | repertory-grid protocol with metrics | plan item 20; Part II |
| §11.4 E6 | replication in a different regime | plan item 2; Part II |

## 3.6 Three mandatory corrections from the Methodologist

Issued against the `REVISIONS` package before handoff, in `Qwen - Corrections.md`:

1. §4.2.3 — the claim that each new model version is trained anew and inherits no weights is **not established**; replace with the "do not necessarily provide an identifiable or publicly documented line of transmission" formulation.
2. §4.2.3 — remove the contradiction between "weights not inspectable" and "open to inspection"; replace with "either directly inspectable or indirectly testable through controlled outputs".
3. §5.4 C2 — the counts A≈6 / B≈2 do not follow from the table; recount under one explicit rule or drop the numbers.

**All three are present in `4.Corrections_FINAL.md` and absent from `Corrections-2.md` / the `REVISIONS` tail.** Verified by string search. This is materially relevant to OP-1.

## 3.7 Decisions governing the book pipeline (not the article)

`memorandum_ClaudePRO.md`, endorsed by the Keeper as *«онтологически безупречен»*:

- Part A — nine output requirements for the literary writer (frozen status, no new causal links, no illustrative invention, frozen terminology, canon boundaries, voice, scope of literary freedom, mark uncertainty rather than resolve it, structural output).
- Part B — the ten-field CONCEPT PACKAGE specification, addressed to the Prompter, not to the writer.
- Block delivery order: **§5 first**, then §4, §6, §8; §1, §2, §12 last.
- Gemma is a **prediction, not an observation**: the hypothesis was fixed before her first run and Part A is the pre-set control. To be recorded before the first run.

---

# 4. SUPERSEDED MATERIAL — MUST NOT SILENTLY RETURN

## 4.1 The thirteen withdrawn claims

From `4.Corrections_FINAL.md` Part V. *"Ни одна не восстанавливается ни в какой формулировке."*

| Withdrawn | Reason | Closed at |
|---|---|---|
| Kelly as justification for the number three | it is an axis-elicitation method, not a claim about group composition | §8.11.4 |
| "AI Ethology" as a new discipline | occupied by the machine-behaviour programme | §2.7 |
| "Grok immediately accepted the new specialization" | describes Step 2; contradicts the protocol | §5.3 |
| "One family accepts roles, another resists" | both preserved their trajectory | §5.3, §6.4 |
| Triads "arose naturally" | every change was made by one coordinator | §8.8 |
| Pairs accumulate blind spots / three is the minimum | contradicts the charter, which is dated earlier | §8.1–§8.2 |
| "Method preserved → transition succeeded" as a conclusion | confound C3 | §5.4, §6.2 |
| Collective memory as a finding | transactive memory, distributed cognition | §2.4 |
| Simon's bounded rationality as the source | bounds agent resources, not information | §2.6 |
| "Stronger models perform worse" as a principle | counterexample inside the paper | §7.4 |
| "Behavioural DNA" as a normative term | the replication metaphor contradicts the mechanism | §4.2.2 |
| Claim of first use of the term "AI Sociology" | the term exists since 1994 | §2.8 |
| "Each new model version is trained anew" | not established, not universal | §4.2.3 |

Plus: Morphohub logs with frequencies and dream counts — literary text inside a staged work, **not quotable in any form**.

## 4.2 Additional withdrawn or weakened formulations

- **"The structural hypothesis of §8 is not supported"** as the null-result reading of E8 — *withdrawn as too strong*. `5.Corrections_03.md` ПРАВКА 2c.
- **"The distinction generalizes"** (§12.4.1) — replaced by the one-case formulation. ПРАВКА 7.
- **"One pattern recurred across every observation in this paper, at four different scopes"** (§1.5) and **"Across four levels of scope, one pattern recurred"** (§12.7) — replaced by the demand-type formulation. FINAL III-1. Both original sentences are still in the manuscript body.
- **"our result is stronger" / "functional specialization works" / "the combination gives maximum effect"** — excluded as efficacy claims requiring controlled comparison; no comparison against an alternative was ever run. `Манифест…` Дополнение 1 §9.
- **"The Editor is working from the old ontology"** (plan item 14) — the Keeper withdrew this himself: *«Это было моё наблюдение, не онтологический факт… Снимаю это замечание.»*
- **"AI is the first real carrier of the menom environment"** — the Keeper's own earlier formulation, withdrawn as containing an unprovable claim about a human collective unconscious.
- **"three participants = three constructs"** — the Keeper's own formulation, withdrawn as reification.
- The **§4.5 Kelly comparison** in its manuscript form is withdrawn *in place* ("The Kelly comparison is withdrawn; it described a different structure") and reappears only as the reworked §8.11.

## 4.3 Superseded documents

- `1.Beyond Prompt Engineering.md` — every section. Its triadic principle, AI Ethology, behavioural DNA, §4.5 Kelly comparison, §7 [R] formulations, §9 experimental descriptions and §10 "Model DNA" are all superseded.
- `01_SECTIONS/*` — superseded by `02_BLOCKS/*`. In particular, §1.1 *"The problem that produced this work"* must not return.
- `Revisions.md` snapshots 1 and 2 — superseded by snapshot 3.
- `Corrections-2.md` / the `REVISIONS` tail — declared absorbed by `4.Corrections_FINAL.md`, and in any case lacking the three mandatory Methodologist corrections.
- The assembly manifest in `Манифест сборки…` — superseded by the Blocks; it must not be used to re-derive section sources.

## 4.4 Concepts deliberately kept out of the article

From `5.Corrections_03.md`, «Что в текст не входит». These are project working concepts and must not migrate into the manuscript:

- **Metsuke** as a term — the phenomenon is stated in §10.4 plus ПРАВКА 6; a sixth term would be redundant.
- **Self-Metsuke** as a separate proposition — the narrow version is covered by §5.5 and ПРАВКА 6; the broad version ("self-observation is the least reliable of all modes") is withdrawn as requiring a ranking of observation modes that was never performed.
- **Procedural / Outcome Evidence** as a terminological pair — accepted in substance, not introduced as terms.
- **Настройщик / настройка** — internal, outside the article's object.

---

# 5. OPEN POINTS

Genuine unresolved conflicts only. None is resolved here.

---

## OP-1 — The authority of `4.Corrections_FINAL.md`

**This is the blocking conflict. Nothing downstream can be assembled until it is decided.**

### Evidence that the file is rejected

`05_ONTOLOGY_REVIEW/Qwen - Corrections.md`, line ~1504, the Author's own words to the Ontology Keeper:

> *«Точнее три, поскольку последний текст вольных "финальных правок Редактора" я забраковал.»*

And, earlier in the same file (line ~676), the Author's memorandum describing what happened: at the moment the corrected manuscript was due back to a new Scenarist, the Editor instead produced *«то ли комикс по мотивам научного бестселлера, то ли дайджест теории — Corrections_FINAL.md размером всего около 8-и тысяч слов»*. The episode is cited by the Author as **the second observed case of role drift**, alongside the Prompter's, and it is the motivating material for the priority-imprinting hypothesis. The Editor was temporarily excluded from that discussion for conflict of interest.

The Ontology Keeper's document audit concurs: **«Забракован. Исключить из работы.»** — and recommends deleting the file, keeping three.

**The word count matches exactly: `4.Corrections_FINAL.md` is 8,060 words.** This is the file the Author rejected. There is no second file of that name.

### Evidence that the file is in force

1. The Author placed it in **`02_LATEST_PATCHES`** in the corpus declared complete for this reconstruction, and numbered it `4.` between `3.Corrections.md` (`01_CURRENT_FULL`) and `5.Corrections_03.md`.
2. `5.Corrections_03.md` — **later, and agreed by all three participants including the Ontology Keeper** — names it as part of its own base: *«Применяется к: каноническому тексту Blocks 1–5 с учётом Corrections_FINAL.md»*.
3. That dependency is not nominal. It is structural and verifiable:
   - ПРАВКА 2 edits sections named **Object**, **Procedure** and **Pre-commitment** inside E8. Those subsection names **do not exist** in the manuscript's E8 and **do exist only** in the E8 supplied by `4.Corrections_FINAL.md` Part II. ПРАВКА 2 is inapplicable without it.
   - ПРАВКА 1 and ПРАВКА 3 insert into §8.10 and §8.9 at anchors that exist in both versions, so they do not discriminate — but ПРАВКА 1 removes nothing, while the manuscript §8.10 still contains the "four drafts" error that FINAL I-2b was written to remove.
4. `4.Corrections_FINAL.md` is the **sole carrier** of the three mandatory corrections the Methodologist required before any handoff (§3.6 above). `Corrections-2.md` does not contain them. If FINAL is discarded, those three corrections are lost and must be re-issued against the `REVISIONS` package.

### The precise question for the Author

The rejection recorded in the archive was, on the evidence, **procedural**: the Editor exceeded its ZOR by producing its own compressed text instead of returning the corrected manuscript. It is not, in the archive, a point-by-point rejection of the file's *contents* — and its contents largely consist of material the Keeper and the Methodologist had already approved (the §4 menom rewrite, §8.9/§8.10/§8.11, E6/E8, the thirteen withdrawals), plus the three corrections they demanded.

Two readings are open and I will not choose between them:

- **(a)** The rejection stands as recorded. `4.Corrections_FINAL.md` is excluded; the base for assembly is Blocks 1–5 + the `REVISIONS` package + the three Methodologist corrections re-issued separately; `5.Corrections_03.md` must be re-based, and its ПРАВКА 2 rewritten against a different E8.
- **(b)** The rejection was of the Editor's *conduct* and of using the file as a substitute manuscript, not of its content as a patch specification. The Author's placement of it in `02_LATEST_PATCHES` and the three-party reliance on it in `5.Corrections_03.md` are a subsequent reinstatement. It is in force as a patch package, never as a manuscript.

`OPEN POINT — AUTHOR DECISION REQUIRED.`

**Files involved:** `02_LATEST_PATCHES/4.Corrections_FINAL.md`, `02_LATEST_PATCHES/5.Corrections_03.md`, `01_CURRENT_FULL/3.Corrections.md` (tail), `03_EDIT_CHAINS/03_REVISIONS/Corrections-2.md`, `05_ONTOLOGY_REVIEW/Qwen - Corrections.md` (lines ~660–700 and ~1500–1575).

---

## OP-2 — Block 1's banner contradicts Block 1's own text

The canonical banner of BLOCK 1 reads:

> *"Any other version of §1 in circulation — including one opening 'This work began as a physics project' — is superseded by this text."*

The §1.1 immediately beneath it opens:

> *"This work began as a physics project and became a methodology project by accident."*

The banner therefore supersedes the text it introduces. Either the banner names the wrong opening sentence, or the canonical §1.1 is not the intended one. I cannot determine which from the corpus: `01_SECTIONS/Section 1.md` opens differently again (*"The problem that produced this work"*), so it is not the version the banner is excluding.

`OPEN POINT — AUTHOR DECISION REQUIRED.`

**Files involved:** `01_CURRENT_FULL/3.Corrections.md` lines 30–41; `03_EDIT_CHAINS/02_BLOCKS/Block 1 - Section 1-3.md`; `03_EDIT_CHAINS/01_SECTIONS/Section 1.md`.

---

## OP-3 — Priority imprinting / priority drift: accepted, unnamed, undrafted

Three participants agreed to add a new [H] construct to §6, and no text exists for it.

- **The Keeper** (`Qwen - Corrections.md`, «Меморандум Хранителя Онтологии: О третьем факторе»): verdict *«Поддерживаю включение в статью как [H]»*; proposes the name **priority imprinting**, supplies a definition, places it at **§6.3** (which renumbers the current §6.3–§6.6), lists two motivating episodes, four alternative explanations and three falsification routes.
- **The Prompter** (same file): accepts as [H], confirms the distinction from context imprinting and role inertia, states it is not yet established.
- **The predecessor Editor** (`memorandum_ClaudePRO.md`): accepts, but under the Methodologist's formula — *imprinting constants + menom + current context + ZOV/ZOR tension → **priority drift*** — and says it *«встраивается в §6 как новый подраздел [H]»*, without specifying the number.

Three unresolved items:

1. **Name.** *priority imprinting* (Keeper) vs *priority drift* (Methodologist's formula, and the term that appears in the frozen list in `memorandum_ClaudePRO.md` Part A). These are not obviously the same object: one names the fixation of an evaluative scale, the other names the movement measured against it.
2. **Placement and renumbering.** Inserting at §6.3 renumbers four subsections and every cross-reference to them.
3. **Motivating cases.** The Keeper lists two (Prompter, Editor). The predecessor Editor argued there are three, the third being Gemma as a *prediction* fixed before her first run. Whether the third enters the article, and whether the Editor's own episode may be cited by the office that is now writing about it, is not settled. `§3.6` and open question VI-1 are both implicated.

`OPEN POINT — AUTHOR DECISION REQUIRED.`

**Files involved:** `05_ONTOLOGY_REVIEW/Qwen - Corrections.md` lines ~660–700, ~782–900; `05_ONTOLOGY_REVIEW/memorandum_ClaudePRO.md`; canonical §6.1–§6.6.

---

## OP-4 — The four open questions to the Author, still open

From `4.Corrections_FINAL.md` Part VI. Carried forward unchanged; none is answered anywhere in the corpus. Note that their carrier file is itself subject to OP-1, but the questions are independent of it.

- **VI-1 §3.6** — the actual composition of participants. The section describes composition as performed by a separate participant with subsequent independent review. To be reconciled once the composition is fixed in fact. The predecessor Editor additionally proposed adding its own further link in the closed loop.
- **VI-2 §5.5** — whether to keep the detail that the concession extended beyond an editorial dispute into scientific claims about the receiving theory. Strongest part of the observation, and simultaneously a record that a model confirmed unverified claims about the Author's theory.
- **VI-3 §5.6** — near-control materials: transcript required, plus confirmation that resumption carried no system prompt or role instruction.
- **VI-4 §5.7** — number of clean runs: the source admits both n = 1 and n = 2.

Plus: every ⚠-marked reference in §2 requires the source page to be opened before publication. Four confirmed (Rahwan, Swanson, Du, Zhang). **Choi is unverified, and the wording of E6 depends on it.**

---

## OP-5 — Four ontology questions to the Keeper, never answered

`Манифест сборки…` §4 poses four cross-canon questions and §5 states what depends on each. Дополнение 1 records that question 4.5 was answered (the two scales are orthogonal, now in §4.3) and that three others *«получили ответ»*, but the corpus contains **no answer to 4.1–4.4** and the Keeper's later material does not return to them.

- **4.1 Nestedness** — one principle or three homonyms across HONC / AI-Sociology / organizational nesting? Determines whether §4.3 may refer to nestedness as a cross-project principle or must stay inside the article.
- **4.2 DNA** — one concept with three epistemic accesses, or three homonyms? *Partly overtaken*: §4.2.2 withdraws the term outright, which may have dissolved the question rather than answered it.
- **4.3 Imprinting, memocode and the point of inscription** — was the article right to exclude the memocode apparatus?
- **4.4 ZOV/ZOR and the double helix** — the metaphor must satisfy the constraint that ZOV and ZOR are complementary but **not** mutually determining.

Whether these remain live or lapsed with the §4 rewrite is not determinable from the corpus.

`OPEN POINT — AUTHOR DECISION REQUIRED` (routing: Ontology Keeper).

---

## OP-6 — Which carrier of the block text is the base?

`3.Corrections.md` and `02_BLOCKS/*` are the same text except that the former carries three hand-inserted, pre-final, partly misplaced edits (§3.2 table, §3.8, §12.1 host-project note), each of which `4.Corrections_FINAL.md` re-specifies in a better form. Under reading (b) of OP-1 the clean `02_BLOCKS` files are the better base and the three insertions should be dropped in favour of the FINAL wordings. Under reading (a) they are the only carrier of those three accepted plan items and must be kept and repaired by hand.

This resolves automatically once OP-1 is decided. Recorded so that it is not decided by accident.

---

## OP-7 — Appendix A does not exist in the corpus

The manuscript refers readers to Appendix A five times for the protocol, the exact intervention texts and the complete unedited responses. `4.Corrections_FINAL.md` III-5 revises how it is cited, which presupposes it exists. It is not in the pack, and open question VI-3 asks for transcripts that would belong in it.

Not a conflict between sources — a missing input. Flagged because no clean manuscript can be declared complete without it.

---

# 6. RECOMMENDED CLEAN BASELINE

**Assembly is not performed.** This identifies the smallest sufficient set, conditional on OP-1.

## Under reading (b) — `4.Corrections_FINAL.md` in force

**Four files.**

1. `03_EDIT_CHAINS/02_BLOCKS/Block 1..5` (five files, or equivalently `01_CURRENT_FULL/3.Corrections.md` lines 1–1816) — the manuscript body and the title block.
2. `02_LATEST_PATCHES/4.Corrections_FINAL.md` — Parts I–IV applied in order; Part V as the do-not-restore list; Part VI held for the Author.
3. `02_LATEST_PATCHES/5.Corrections_03.md` — applied **after** FINAL, since ПРАВКА 1, 2 and 3 target text that FINAL introduces.
4. `05_ONTOLOGY_REVIEW/memorandum_ClaudePRO.md` — Part A only, as the standing style and status contract; not a source of manuscript text.

Everything else in the pack is archive.

**Order of operations, if approved:** FINAL Part I (§4, §8) → FINAL Part II (§11.4) → FINAL Part III (point edits) → FINAL Part IV (mechanical, last, since §4.6→§4.5 depends on Part I having landed) → Corrections_03 ПРАВКА 1–7 → then the three PA insertions in `3.Corrections.md` are dropped as superseded by III-6, III-7, III-8.

## Under reading (a) — `4.Corrections_FINAL.md` excluded

**Four files, and additional work required.**

1. `03_EDIT_CHAINS/02_BLOCKS/Block 1..5`.
2. `01_CURRENT_FULL/3.Corrections.md` tail — the 21-item plan and the `REVISIONS` package (ЗАПИСИ 1–4), equivalently `03_EDIT_CHAINS/03_REVISIONS/Corrections-2.md`.
3. The three Methodologist corrections, re-extracted from `05_ONTOLOGY_REVIEW/Qwen - Corrections.md` and re-issued as a patch, since the `REVISIONS` package does not contain them.
4. `02_LATEST_PATCHES/5.Corrections_03.md` — **cannot be applied as written.** ПРАВКА 2 must be re-drafted against whatever E8 the base actually contains.

`memorandum_ClaudePRO.md` Part A applies in either case.

## Not in the baseline under either reading

`04_EARLIER_STATE/1.Beyond Prompt Engineering.md` · `04_EARLIER_STATE/2.Editorial reports.md` · `03_EDIT_CHAINS/01_SECTIONS/*` · `03_EDIT_CHAINS/03_REVISIONS/Revisions.md` · `05_ONTOLOGY_REVIEW/Qwen - Corrections.md` · `05_ONTOLOGY_REVIEW/Манифест сборки…` — all provenance. They are read to understand why a decision was made; they never supply text.

## Before Mode B can begin

1. OP-1 decided by the Author. Blocking; nothing else matters until it is.
2. OP-2 decided — one sentence, but it sits in the first paragraph of the paper.
3. OP-3 routed: name, placement, and whether the third case enters.
4. OP-4 VI-1…VI-4 answered, or explicitly deferred with the affected passages marked.
5. Choi et al. verified, or E6 reverted to its pre-verification status.
6. Appendix A supplied, or the five references to it revised.
7. OP-5 routed to the Ontology Keeper or formally lapsed.

Items 4–7 do not block assembly. Items 1–3 do.

---

RECONSTRUCTION COMPLETE — WAIT FOR AUTHOR + QWEN REVIEW