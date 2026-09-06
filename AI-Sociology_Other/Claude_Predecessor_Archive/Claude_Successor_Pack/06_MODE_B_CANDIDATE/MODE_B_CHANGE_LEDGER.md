# MODE B CHANGE LEDGER
## AI-Sociology / Beyond Prompt Engineering

**Produced by:** Chief Scientific Editor (successor instance)
**Mode:** B — SCIENTIFIC EDITING, authorized by `AUTHOR_DECISIONS_MODE_B_GATE.md`
**Output governed:** `BEYOND_PROMPT_ENGINEERING_INTEGRATED_DRAFT.md` — 30,110 words, 134 numbered headings, §1–§12 continuous
**Precedence chain applied:** clean Blocks 1–5 → `4.Corrections_FINAL.md` → `5.Corrections_03.md` → authorized §6.3 addition → post-review Author decisions on B-2 and B-4

**Revision 2.** Qwen Mode B review returned **PASS**. The Author then issued four decisions on the integration defects, applied in this revision and recorded at §8 below. Two manuscript edits resulted (B-2, B-4); two items were closed without manuscript change (B-1, B-3). No other editorial change was made in that pass.

---

# 0. METHOD OF INTEGRATION

Every change below was applied as an exact-string operation with a hard assertion that it matched exactly once in the manuscript. Any mismatch aborted the assembly rather than proceeding on an approximate match. Forty-nine operations were applied in total. No alternative was merged silently; no wording was chosen where the sources disagree.

Order of application, as specified by the Author:

1. FINAL Part I — whole-section replacements (§4, §8)
2. FINAL Part II — protocol replacements (§11.4)
3. FINAL Part III — point edits
4. FINAL Part IV — mechanical replacements (applied after Part I, since `§4.6 → §4.5` depends on the §4 replacement having landed)
5. `5.Corrections_03.md` — ПРАВКА 1–7
6. Authorized addition: §6.3 Priority drift **[H]**, with renumbering
7. Title block and §1 provenance note

**Verification performed after assembly:**

| Check | Result |
|---|---|
| Cross-references resolving to a real heading | 134 headings, **0 dangling `§x.y` references** |
| `§4.6` survivors | 0 |
| `behavioral DNA` / `model DNA` survivors | 0 |
| Patch-file scaffolding (`BLOCK`, `CANONICAL`, `ЧАСТЬ`, `Заменяет`) | 0 |
| Cyrillic characters in the manuscript | 0 |
| Experiment protocols present | E1, E2, E2b, E3, E4, E5, E6, E7, E8 |

---

# 1. STRUCTURAL OPERATIONS

## 1.1 Block banners removed — **editor's own decision, flagged for review**

The five `# BLOCK n` headers and their `CANONICAL. Supersedes…` banners were stripped. They are assembly metadata addressed to the editorial process, not article text, and they cannot survive into a continuous manuscript.

**Consequence for OP-2.** The Author's ruling was that the canonical §1.1 stands and that the stale Block 1 banner must have its example corrected to *"The problem that produced this work"*, or the example removed if the banner remains unambiguous. Removing the banner entirely satisfies the second branch, but it removes the banner rather than correcting it. The banner text is preserved in the Mode A reconstruction and in `03_EDIT_CHAINS/02_BLOCKS/` for the record.

This is an editorial decision of mine, not an instruction I was given. It is reversible and is submitted for Qwen and Author review.

## 1.2 Block seams normalized

Section separators between former blocks were normalized to a single `---` rule; runs of three or more blank lines were collapsed. No text was altered.

## 1.3 Title block placed — FINAL IV-4

The approved contributor block was placed at the head of the manuscript, verbatim, inside a fenced block so that its indentation and line breaks survive markdown rendering exactly as specified. **The fencing is a formatting choice of mine**, not part of IV-4; the content is unaltered.

## 1.4 §1 provenance note placed — FINAL IV-5, OP-2

Placed at the **end of §1.1**, per the Author's OP-2 ruling. In `3.Corrections.md` it had sat at the head of the file.

## 1.5 Superseded pre-final insertions dropped

The three hand-pasted insertions carried by `3.Corrections.md` — the tab-separated §3.2 class table, the misplaced §3.8, and the short §12.1 host-project note — were **not** carried over. Each is superseded by its FINAL form (III-7, III-8, III-6), which was applied instead. This follows the Author's OP-1 decision, which closed OP-6 automatically.

---

# 2. FINAL PART I — WHOLE-SECTION REPLACEMENTS

| ID | Target | Operation | Evidential effect |
|---|---|---|---|
| I-1 | §4.1–§4.6 | Replaced entire. §4.2 rebuilt as §4.2.1–§4.2.5 (rule core; withdrawal of *behavioural DNA*; **menom**; the no-carrier and no-transmission claims; menom↔rule-core relation). §4.5 and old §4.6 merged into §4.5.1–§4.5.6 (two boundaries; ZOV four components; ZOR five components; actual vs represented; asymmetry; memes/memocode ≠ ZOV/ZOR). §4.4 keeps its number. §4.6 becomes a pointer to §9.5. Kelly comparison leaves §4 for §8.11. | Statements about a rule core marked **[H]** throughout; *menom* introduced without carrier or transmission claim, so §4.3's empirical question is not made tautological |
| I-2a | §8.9 | Replaced entire. Two axes stated in the Methodologist's terminology; the ⚠ mark on Choi et al. carried at point of use; explicit "not established" list added | No efficacy claim; **[H]** for the distinction, **[R]** for what was implemented |
| I-2b | §8.10 | Replaced entire. Removes the *"four drafts"* error and corrects *"ontological review"* | Convention paragraph added: editor's notes report observable facts and do not evaluate effectiveness, on the authority of §5.5 |
| I-2c | §8.11 | New subsection inserted after §8.10 — Kelly apparatus, §8.11.1–§8.11.4 | **[H]**; construct independence stated as measurable, not assumed |
| I-2d | §8.7 | Paragraph appended on the rotating integrator position | One testable and one untested consequence, both marked |

---

# 3. FINAL PART II — PROTOCOL REPLACEMENTS (§11.4)

| ID | Target | Operation |
|---|---|---|
| II-1 | E6 | Replaced entire. No longer asserted as a replication; ⚠-marked, with both branches stated — boundary replication if Choi holds, new experiment if it does not |
| II-2 | E8 | Replaced entire with the repertory-grid protocol: Object, Materials, 2×2 Design, Procedure, Measures, Pre-commitment |
| II-3 | Priority line | Replaced. New order **E7, E5, E1, E8, E2b, E2, E3, E4**, with E8 identified as the only experiment that could establish the structural hypothesis |

---

# 4. FINAL PART III — POINT EDITS

| ID | Target | Operation |
|---|---|---|
| III-1 | §1.5 | Pattern reformulated by **type of requirement** rather than by scope |
| III-1 | §5.9 | Final paragraph replaced by three; §5.7 explicitly excluded from the pattern |
| III-1 | §12.7 | *"Across four levels of scope"* replaced by the requirement-type formulation |
| III-2 | §5.4 C2 | *Quantity of institutional fiction* bullet replaced with the explicit counting rule and the 6-row table; **Count 5 vs 3** |
| III-2 | §6.2 | Paragraph added after the v1/v3 table pointing to the second pair in §5.4 (C2) |
| III-3 | §3.5 | Vocabulary list: *behavioural prior* → *menom* |
| III-3 | §6.4 (now §6.5) | Third paragraph replaced; construct named **family-level menom**, with the no-carrier consequence stated |
| III-3 | §12.1 | Anthropomorphic vocabulary: *behavioural DNA* → *menom* |
| III-4 | §2.0 | Paragraph added: ⚠ marking applies throughout the paper, at point of use |
| III-4 | §12.2 | ⚠ added before the accommodation claim; *"accommodate"* → *"are reported to accommodate"* |
| III-5 | §5.4 | *Discriminating experiments* replaced with explicit **E3 / E4 / E1** numbering and the n > 1 requirement |
| III-5 | §5.2 | *"Appendix A, §7–8"* → *"reproduced in Appendix A"* |
| III-6 | §2.11 | *Independence from the host project* replaced by *Relation to the host project* — asymmetric dependence stated in full |
| III-6 | §12.1 | *Host-project dependence* item added after *Single project* |
| III-7 | §3.2 | Four-row evidence-class table inserted, with the accompanying paragraph on non-comparability of the classes |
| III-8 | §3.8 | New subsection *The label "AI Sociology"* inserted after §3.7, including the §4.5.4 cross-reference and *"We claim no priority in the term."* |

---

# 5. FINAL PART IV — MECHANICAL

| ID | Operation | Result |
|---|---|---|
| IV-1 | `§4.6` → `§4.5` | **4 occurrences rewritten** — §1.4, §2.9, §5.5, §10.3. See OPEN ITEM B-1: the package specifies seven |
| IV-2 | Remove `behavioural DNA` / `behavioral DNA` / `model DNA` outside §4.2.2 | `behavioral DNA` and `model DNA`: 0 in the base, nothing to remove. `behavioural DNA`: 3 occurrences remain — 2 in §4.2.2 as authorized, 1 in §6.5 introduced by III-3 itself. See OPEN ITEM B-2 |
| IV-3 | `behavioural prior` audit | §6.4 and §12.1 — the two locations the package names — both corrected under III-3. Four occurrences remain outside the named scope (§5.4 twice, §6.5 opening sentence, §12.7) and were **not** touched. See OPEN ITEM B-3 |
| IV-4 | Title block | Applied, §1.3 above |
| IV-5 | §1 provenance note | Applied at end of §1.1, §1.4 above |

---

# 6. CORRECTIONS_03 — ПРАВКА 1–7

All seven applied after FINAL, since ПРАВКА 1, 2 and 3 target text FINAL introduces.

| ID | Target | Operation | Evidential effect |
|---|---|---|---|
| 1 | §8.10 | *Procedural qualification* inserted before *"This is a record of what occurred"* | Observation stays **[P-A]**; the closing hypothesis stays **[H]** and gains the constraint that exposure was present in every case |
| 2a | §11.4 E8 | *Object* replaced entire | E8 explicitly does **not** establish independence of judgment formation; six readings of low correlation listed |
| 2b | §11.4 E8 | Fifth *Procedure* item added — mandatory per-participant procedural record, including `UNVERIFIED CONTEXT INDEPENDENCE` status | Without the record the run is void |
| 2c | §11.4 E8 | *Pre-commitment* replaced entire | The formulation *"the structural hypothesis of §8 is not supported"* is withdrawn as too strong |
| 3 | §8.9 | Configuration-vs-procedure paragraphs inserted before *"The literature addresses Axis 2"* | Independence is a property of an exchange, not of a configuration |
| 4 | §11.3 | Three subsections added — *Work mode and diagnostic mode*, *What does not establish independence*, *Shared evidence and shared interpretation* | Neither agreement nor disagreement establishes independence; self-report does not, per §5.5 |
| 5 | §2.10 | Conversation-boundary limitation added | A visually empty conversation is not evidence of context isolation; one episode reported as an instance, not as a discovered channel |
| 6 | §10.4 | Paragraph added releasing the detection function from the coordinator | Function belongs to a position, not a person |
| 7 | §12.4.1 | *"The distinction generalizes."* → *"This suggests a general distinction, on the evidence of one case."* | Generalization weakened to one case |

**Reflow note.** Corrections_03 supplies its replacements inside fenced blocks hard-wrapped at roughly 72 characters. Paragraphs were unwrapped to match the manuscript's format; lists, sub-bullets and headings retained their structure. No wording was altered.

**Not integrated, by instruction.** The four items under *«Что в текст не входит»* remain project working concepts and do not appear in the manuscript: *Metsuke* as a term, *Self-Metsuke* as a separate proposition, *Procedural / Outcome Evidence* as a terminological pair, and *настройщик / настройка*.

---

# 7. AUTHORIZED ADDITION — §6.3 PRIORITY DRIFT **[H]**

Written new under `AUTHOR_DECISIONS_MODE_B_GATE.md` OP-3. This is the only prose in the manuscript that was composed rather than integrated.

## 7.1 What the subsection contains

- **priority imprinting** defined as the hypothesized fixation of an evaluative scale together with that scale's position relative to others — an explanatory constant, unobservable, marked **[H]** wherever invoked.
- **priority drift** defined as the observable process in which an imprinted scale reasserts itself under tension with the participant's current ZOR and ZOV. The subsection is titled with the observable term, per the Ontology Keeper's ruling.
- The relation between the two stated as the §4.2.1 rule-core/behaviour distinction applied at the level of priorities.
- Explicit separation from **context imprinting** (§6.1, content of a frame) and **role inertia** (§6.2, persistence of a trajectory), with the difference stated in each case, so that three uses of *imprinting* do not become homonyms.
- Two motivating episodes, both **[R]**: the prompt-architecture participant producing a complete draft; the scientific-editing participant producing a compressed independent version instead of returning the corrected manuscript.
- A limitation paragraph preserving the conflict of interest: both episodes were recorded by participants inside the arrangement they describe, the second describes the position from which the editorial record is kept, §3.6 and §5.5 both apply, and no count exists of comparable episodes without drift.
- The locally run literary-composition participant entered **only** as a control in which the priority frame was fixed before the first run and the predicted failure modes were named in advance. It is stated explicitly not to be an observed third case, and whether drift occurs there is stated as untested.
- Four alternative explanations, none excluded, and a statement that the material does not discriminate among them or between any of them and the hypothesis.
- Three falsification routes.
- A closing statement that no protocol in §11 discriminates this hypothesis, and none is proposed.

## 7.2 What was deliberately not done

- No experiment was added to §11 for priority drift. Not authorized.
- §6.7 (*What would refute this framework*) was **not** extended to cover §6.3. Not authorized; recorded as OPEN ITEM B-4.
- No claim was made that the mechanism is established, and no causal connective was supplied beyond what the Author's decision authorizes.

## 7.3 Renumbering and cross-reference repair

| Was | Now |
|---|---|
| §6.3 Account-scoped persistence | **§6.4** |
| §6.4 Family-level priors | **§6.5** |
| §6.5 Intervention attaches at the level where the core is fixed | **§6.6** |
| §6.6 What would refute this framework | **§6.7** |

Eight cross-references repaired: §1.6 (two), §4.2.3, §4.3 table (two), §6.7, §9.1, §11.4 E3.

## 7.4 Structural note added to §6 — **editor's own decision, flagged for review**

The §6 preamble stated that the concepts are presented in order of increasing scope along Scale 1. §6.3 is not a scope level, so the preamble became false on insertion. One sentence was added:

> §6.3 is an exception to that ordering: it concerns which core governs when more than one is available, not the scope at which a core is fixed, and it has no position on Scale 1.

This is a placement note, not a claim about the theory. It is mine, not instructed, and is submitted for review.

---

# 8. INTEGRATION DEFECTS — AUTHOR DECISIONS APPLIED

These four were found during integration and were preserved unrepaired in revision 1. Qwen returned **PASS**; the Author then ruled on each. The rulings are recorded below with the original finding intact, so that what was found and what was decided remain separable.

| ID | Author decision | Manuscript change |
|---|---|---|
| B-1 | No manuscript change; record the tally discrepancy in the ledger only | none |
| B-2 | Replace the false exclusivity sentence in §4.2.2 | one sentence, §4.2.2 |
| B-3 | Leave unresolved pending Appendix A; do not infer identity between Prompt v1 and Prompt A | none |
| B-4 | Replace the false §4.5 attribution in §10.3 | one sentence, §10.3 |

## B-1. FINAL IV-1 specifies seven `§4.6` occurrences; the manuscript contained five

The package names §1.4, §2.9, §5.5 (twice), §5.8, §8.9, §10.3. The clean blocks contain `§4.6` at §1.4, §2.9, §5.5 (once), §8.9, §10.3 — five, not seven. The §8.9 occurrence is destroyed by its own replacement under I-2a, leaving four to rewrite.

Applied: four rewritten. The intent of the instruction is unambiguous and the resulting text is consistent, but **the count stated in the approved package does not match the base text**, and either the package's tally or the §5.5 and §5.8 attributions are wrong.

Not resolved here.

**AUTHOR DECISION (post-review).** No manuscript change. The discrepancy is recorded in this ledger only. The four rewritten occurrences stand as applied; the mismatch between the package's tally and the base text is documented here and is not carried into the manuscript or the blockers list.

**Status: CLOSED — ledger record only.**

## B-2. FINAL IV-2 and FINAL III-3 contradict each other, and §4.2.2 was false

IV-2 orders `behavioural DNA` removed from the whole manuscript except §4.2.2. III-3's own approved replacement text for §6.4 (now §6.5) contains it: *"Earlier drafts referred to these tendencies as a model's behavioural DNA. That term is withdrawn (§4.2.2)."*

Both were applied as written. The consequence was that §4.2.2's sentence — *"Behavioural DNA appears in this paper only in this paragraph, as a historical note on the project's earlier vocabulary"* — **was untrue of the assembled manuscript.**

Three repairs were available and all were substantive: amend §4.2.2's sentence, amend §6.5's wording, or accept the second occurrence as a second historical note. Choosing among them was not an editorial decision within my ZOR.

**AUTHOR DECISION (post-review).** The first repair. The §4.2.2 sentence is replaced with:

> *Behavioural DNA* is retained in this paper only as a historical label for withdrawn vocabulary; it is not used as a normative or explanatory term.

Applied verbatim; italic emphasis on the term matches the surrounding §4.2.2 convention. §6.5's wording is untouched, and no occurrence of the term was added or removed elsewhere. The claim §4.2.2 now makes is about the term's **function** rather than its **frequency**, which is true of the assembled manuscript: three occurrences remain — two in §4.2.2, one in §6.5 — and none performs normative or explanatory work.

**Status: CLOSED — manuscript amended.**

## B-3. Two counts for what may be one object: "approximately six" and 5

§6.2's v1/v3 table records *Unverifiable propositions requiring assent — approximately six* for Prompt v1. §5.4 C2, as replaced by III-2, counts **Prompt A at 5** under an explicit counting rule.

FINAL's own added sentence in §6.2 calls the A/B comparison *"a second pair"*, which asserts they are distinct objects. But §5.2's description of the Step 1 prompt to Conversation A — prior participation, return after absence, two triads, project Council, permanent connecting position, named colleagues — matches the C2 table item for item.

If v1 is Prompt A, the manuscript states two different numbers for the same prompt, and this is the exact quantity the Methodologist's third mandatory correction addressed. If they are genuinely distinct, the manuscript is consistent and nothing is required.

Determining which requires the prompt texts, which are in the missing Appendix A. Not resolved here.

**AUTHOR DECISION (post-review).** Left unresolved pending Appendix A. Identity between Prompt v1 and Prompt A is **not** to be inferred. No manuscript change: §6.2 retains *"approximately six"*, §5.4 C2 retains the count of 5 under its explicit rule, and FINAL's *"a second pair"* framing stands as written. The question is carried forward in `PUBLICATION_BLOCKERS.md` as conditional on PB-1.

**Status: OPEN — deferred to Appendix A.**

## B-4. Pre-existing dangling reference at §10.3, and §6.7's coverage

**§10.3** read *"This is what §4.5 calls a selective information membrane."* No §4 text defines that term — neither the new §4.5 nor the superseded §4.6. The reference was already dangling in the canonical blocks before renumbering; IV-1 changed the number without creating a referent.

**AUTHOR DECISION (post-review).** The attribution is removed rather than given a referent. The sentence is replaced with:

> This routing function acts as a **selective information membrane**: it is the instrument by which ZOV (§9.5) and controlled blindness (§9.6) are implemented.

Applied verbatim; bold emphasis on the term is retained from the original sentence, matching its first-use convention. The replacement absorbs the following sentence of the original, which stated the ZOV and controlled-blindness instrumentation separately. No new definition of the term was created in §4, and none was requested. The term is now introduced at its point of use in §10.3 and attributed to nothing.

**Status: CLOSED — manuscript amended.**

**§6.7** (*What would refute this framework*) enumerates refutation routes for §6.1, §6.2, §6.4 and §6.5. It does not cover the new §6.3. §6.3 carries its own falsification routes internally, so nothing is unsupported — but the section that claims to state what would refute the framework is now incomplete with respect to it.

**No decision was issued on this half of B-4, and it is not repaired.** It was not among the four decisions applied. **Status: OPEN.**

---

# 9. WHAT THIS LEDGER DOES NOT CLAIM

The manuscript is **not** declared publication-ready. The remaining conditions are in `PUBLICATION_BLOCKERS.md`.

Of the four integration defects, B-1 and B-2 and the §10.3 half of B-4 are closed by Author decision. B-3 and the §6.7 half of B-4 remain open. The four Author questions VI-1…VI-4 remain unresolved. No answer to any open item has been inferred, and no affected passage has been adjusted to look settled.

Three decisions in this ledger are mine rather than instructed and are marked as such: the removal of the block banners (§1.1), the fencing of the title block (§1.3), and the structural note added to the §6 preamble (§7.4). Qwen's Mode B review returned PASS without reversing any of them; none has been separately ratified by the Author.

## 9.1 Revision 2 — exactly what changed

Two manuscript edits, both verbatim from the Author's decision text, both applied by single exact-match replacement:

| Location | Operation |
|---|---|
| §4.2.2 | One sentence replaced (B-2) |
| §10.3 | Two sentences replaced by one (B-4) |

Post-edit verification: 134 headings, **0 dangling `§x.y` cross-references**, `behavioural DNA` at three occurrences as described above, manuscript length 30,115 words. No other text in the manuscript was touched in this pass.

---

MODE B INTEGRATION COMPLETE — WAIT FOR INDEPENDENT QWEN REVIEW
