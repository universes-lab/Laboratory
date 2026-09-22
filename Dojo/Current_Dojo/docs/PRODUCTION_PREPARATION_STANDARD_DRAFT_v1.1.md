# MANUSCRIPT_PRESS
# PRODUCTION_PREPARATION_STANDARD — DRAFT v1.1

**Status:** DRAFT v1.1 — for Methodologist / Scientific Editor / Doc Brown / Author review  
**Owner of draft:** Prompter  
**Applies to:** human preparation of `SOURCE_MANUSCRIPT` + `PROMPT_MAP` before `PRODUCTION_REVISION` freeze  
**Does not modify:** `MANUSCRIPT_PRESS ENGINEERING SPEC v3.2.2`

---

## 0. PURPOSE

This standard defines the **human production-preparation procedure** for Manuscript_Press.

It does **not** define machine syntax. Machine syntax is already frozen.

The preparation task is:

1. take one editor-approved manuscript;
2. identify its elementary prose moves;
3. place one production marker at the beginning of each move;
4. create the corresponding `PROMPT_MAP` entry **at the same time**;
5. identify protected / immutable manuscript material;
6. test every proposed boundary for BAD CUT;
7. obtain editorial and Author approval;
8. declare the prepared pair ready for `PRODUCTION_REVISION` freeze.

The governing principle is:

> **A production marker is not a page break, section break, word-count cut, or arbitrary chunk boundary. It is the address of one completed prose move that Gemma may transform as one transaction.**

---

# 1. FROZEN MACHINE CONTRACT — NOT REOPENED HERE

The following are assumed and are not redesigned by this standard:

```text
<!-- MP:0001 -->
```

- one `MP` marker begins one production block;
- the block ends immediately before the next production marker or at EOF;
- SOURCE order is execution order;
- every SOURCE marker has exactly one `PROMPT_MAP` entry with the same logical ID;
- one transaction = one MP block;
- marker IDs are persistent logical addresses, not line or byte offsets;
- `LONG_RANGE_FRAME` and `LOCAL_TRANSFORMATION` are non-empty free-text fields;
- Markdown ATX headings outside protected spans are structural passthrough;
- other immutable material is marked with the frozen `MP:PROTECTED` grammar;
- runtime does not place markers, decide BAD CUT, edit SOURCE, edit PROMPT_MAP, or perform semantic patch validation.

This document governs **how humans prepare those frozen inputs**.

---

# 2. ELEMENTARY PROSE MOVE

## 2.1 Definition

An **elementary prose move** is:

> one or more normally complete paragraphs that perform one completed argumentative, explanatory, narrative, or rhetorical operation and can be rewritten as one cold transaction without requiring Gemma to guess what the move was supposed to accomplish. A paragraph split is exceptional and is permitted only by explicit Scientific Editor + Author decision.

A move is defined by **function and cadence**, not by length.

Examples of one move:

- state one claim and give its immediate qualification;
- define one construct;
- introduce one distinction and explain why it matters;
- present one observation and state its evidential limit;
- move the reader from one question to the next;
- close one local argument without necessarily closing the section.

## 2.2 Hard boundary rules

A production boundary:

- **never cuts a sentence**;
- normally **never cuts a paragraph**;
- does not split a claim from a qualification that is required to keep the claim scientifically correct;
- does not split a premise from the sentence that makes clear what the premise is for;
- does not split an enumerated or tabular object if its meaning depends on the set being read together;
- does not force the next block to repair an overstatement created by the previous block ending too early;
- does not exist merely to satisfy a target word count.

A marker may occur after one paragraph or after several paragraphs.

## 2.3 Semantic/prosodic test

Before proposing a boundary, the Prompter asks:

> **If a reader paused here for several minutes, would the preceding move feel deliberately complete rather than accidentally interrupted?**

and:

> **Can the next move begin from the actual accepted prose before it, without requiring hidden knowledge of sentences that were withheld from the previous transaction?**

If either answer is no, the boundary is not ready.

This is a preparation heuristic, not a runtime test.

---

# 3. THE TWO-QUESTION BAD CUT PRECHECK

Every candidate boundary must survive both questions:

> **What move has become complete before this boundary?**

> **What new move begins after it?**

The answers must name **different operations**, not merely different topics.

Good answer:

```text
Before:
The manuscript has established why the observed cases are treated as
measurements along a nesting scale.

After:
The manuscript defines the rule core that makes that scale operational.
```

Bad answer:

```text
Before:
Discussion of rule cores.

After:
More discussion of rule cores.
```

If the distinction cannot be stated cleanly, there is no justified production boundary yet.

---

# 4. BAD CUT — POSITIVE AND NEGATIVE SIGNALS

## 4.1 Strong positive signals for a boundary

A boundary is a strong candidate when the preceding text has just:

- completed a definition;
- completed one evidential claim together with its limitation;
- completed one example and its interpretation;
- completed a local contrast;
- completed one step in a staged argument;
- changed rhetorical task, e.g. from observation → interpretation, or interpretation → proposed test;
- reached a genuine pause in argumentative pressure.

## 4.2 Strong BAD CUT signals

Do **not** cut:

- after a thesis if the next paragraph immediately narrows or limits it;
- between a claim and the evidence that makes the claim intelligible;
- between a term and its definition;
- between a quotation and the sentence that explains why it is present;
- between an observation and an immediately required evidential-status warning;
- in the middle of a crescendo whose rhetorical force depends on accumulation;
- merely because the block “looks long”;
- merely because a heading is nearby.

## 4.3 Heading rule

A heading is **not** itself a production marker.

A heading is structural material and is restored literally by the runtime.

A heading is, however, a strong **candidate signal** that a new prose move may begin immediately after it.

Default preparation behaviour:

```text
## Heading

<!-- MP:XXXX -->
First rewritable prose of the move...
```

Do not insert an MP marker merely because a heading exists if no new prose move begins there.

Conversely, one section may contain many MP blocks.

Production structure remains independent of reader-visible structure.

---

# 5. MARKER PLACEMENT PROCEDURE

For each proposed move:

1. Read the preceding SOURCE context and the current paragraphs as a continuous argument.
2. Identify the rhetorical job of the current move in one sentence.
3. Identify where that job becomes complete.
4. Apply the two-question BAD CUT precheck.
5. Check that no protected span is open at the proposed marker position.
6. Insert the next logical marker immediately before the first rewritable prose of that move.
7. **Without moving on to the next marker**, write the corresponding `PROMPT_MAP` entry.
8. Re-read `SOURCE block + PROMPT_MAP entry` as one prepared production unit.
9. Only then proceed to the next move.

The required discipline is:

> **MARKER PLACEMENT + PROMPT_MAP AUTHORING = ONE PREPARATION OPERATION.**

A marker must never be placed first with the intention that somebody else will later infer why it was placed there.

---

# 6. LONG_RANGE_FRAME — HUMAN WRITING STANDARD

`LONG_RANGE_FRAME` answers:

> **WHERE DOES THIS MOVE BELONG IN THE WHOLE ARGUMENT?**

It is not a summary of the whole manuscript and not a second SOURCE.

It must contain only the long-range orientation needed to prevent local literary success from damaging global meaning.

## 6.1 Minimum content

Every entry should make the following explicit:

```text
LOCATION:
Where the move sits in chapter / section.

FUNCTION:
What this place is doing in the larger argument.

READER_STATE_BEFORE:
What the reader should already understand or still remain uncertain about.

REQUIRED_READER_STATE_AFTER:
What the reader must understand, distinguish, or remain uncertain about
after this move.

CONSTRAINTS:
Only the relevant canon / terminology / epistemic restrictions for this move.

CLOSURE:
What may close here and what must remain open.
```

These labels are a **human convention inside the free-text field**.
The runtime does not parse them as a schema.

## 6.2 Minimum-sufficiency rule

A `LONG_RANGE_FRAME` is too weak if Gemma could produce locally elegant prose that changes the paper's argumentative position without violating the instruction.

It is too large if it restates remote material that does not constrain the current move.

Target:

> **the smallest frame that prevents a locally good block from becoming globally wrong.**

## 6.3 Reader-state rule

`READER_STATE_BEFORE` and `REQUIRED_READER_STATE_AFTER` describe the reader's epistemic position, not desired wording.

Good:

```text
READER_STATE_BEFORE:
The reader knows that the observations are heterogeneous in evidential status.

REQUIRED_READER_STATE_AFTER:
The reader understands that the programme is organized by one nesting question,
but must not infer that all levels of the scale are empirically established.
```

Bad:

```text
REQUIRED_READER_STATE_AFTER:
End with an elegant sentence about the nesting question.
```

The second belongs, if anywhere, in `LOCAL_TRANSFORMATION`.

---

# 7. LOCAL_TRANSFORMATION — HUMAN WRITING STANDARD

`LOCAL_TRANSFORMATION` answers:

> **WHAT MUST THIS SOURCE MOVE BECOME NOW?**

It is the current operation applied to the current SOURCE block.

## 7.1 Minimum content

Use the following internal convention:

```text
TRANSFORM:
What operation Gemma must perform on this source move.

PRESERVE:
What content, distinction, sequence, evidential status, terminology,
or rhetorical relation must survive.

DO_NOT_INTRODUCE:
What the block must not add, infer, strengthen, close, generalize,
or foreshadow.

RHETORICAL_OPERATION:
What kind of prose move this is locally.

SEMANTIC_STOP:
The exact condition that must be satisfied before the move is complete.
```

Again, these are labels inside the free-text field, not new runtime keys.

## 7.2 Semantic stop

`SEMANTIC_STOP` is mandatory in the preparation standard even though it is carried inside the existing `LOCAL_TRANSFORMATION` field.

It answers:

> **What must be finished before Gemma is allowed to stop this block?**

Example:

```text
SEMANTIC_STOP:
Stop only after the scale has been connected to the single empirical question.
Do not begin the following section's list of non-claims.
```

A semantic stop is **not** a requested final sentence.

It is a completion criterion.

## 7.3 Source ceiling

`LOCAL_TRANSFORMATION` may change literary realization.

It may not authorize content absent from SOURCE.

It must not turn:

- observation into fact beyond its evidential class;
- hypothesis into result;
- correlation into cause;
- one case into a general rule;
- retrospective interpretation into contemporaneous record;
- an open point into a resolved claim.

If the desired local move requires such a change, preparation stops and returns to scientific/editorial authority.

---

# 8. CONTINUITY AND CACHE

Preparation does not write `CACHE_BEFORE`.

Runtime supplies it from the exact previous **canonical accepted prose**.

The Prompter must therefore write each instruction knowing that:

```text
CACHE_BEFORE
= where the prose literally just stopped

CURRENT SOURCE + LOCAL
= what may be written now

LONG_RANGE_FRAME
= where this move belongs in the whole argument
```

The preparation standard inherits the hard rule:

> **CACHE ALWAYS YIELDS.**

No instruction may rely on previous generated prose as substantive authority.

If the previous canonical prose creates a stylistic or referential continuation that conflicts with SOURCE, LONG_RANGE, LOCAL, or STABLE constraints, continuity is sacrificed.

---

# 9. PROTECTED / IMMUTABLE MATERIAL

## 9.1 What is protected

Reader-visible material explicitly approved by the Editor or Author as not subject to Gemma rewrite authority must be protected.

Typical cases:

- exact direct quotations;
- equations and formulas;
- tables whose values or wording are fixed;
- code or literal blocks;
- citation/reference anchors that must remain exact;
- figure/table labels;
- approved captions;
- canonical coined formulations whose exact wording must not drift;
- any other Author/Editor-marked immutable span.

Seeing protected material does not extend Gemma's literary authority over it.

## 9.2 Frozen syntax

Use exactly:

```text
<!-- MP:PROTECTED id="P01_01":BEGIN -->
Exact immutable material.
<!-- MP:PROTECTED id="P01_01":END -->
```

Rules inherited from the engineering contract:

- IDs must be unique within the revision;
- nesting is forbidden in V1;
- a production marker cannot begin inside an open protected span;
- matching END syntax inside protected content is invalid in V1;
- runtime slots and restores the material mechanically.

## 9.3 Headings

Markdown ATX headings outside protected spans are already automatic structural passthrough.

Do **not** wrap ordinary headings in `MP:PROTECTED`.

The stable writer contract separately instructs Gemma not to repeat, paraphrase, announce, or generate a mini-introduction merely because a heading was visible.

## 9.4 Do not over-protect

Protection is not a substitute for writing a good prompt.

Do not protect ordinary prose merely because its current wording is liked.

Protect only material whose **exact form** is outside Gemma's rewrite authority.

---

# 10. OVERSIZED MOVE

If runtime returns:

```text
SEGMENTATION_TOO_LARGE_FOR_CURRENT_WRITER_CONFIGURATION
```

the runtime does not split the block.

The production-preparation owner asks:

> Can this literary move be divided into two genuinely independent completed moves?

If yes:

```text
RESEGMENT
→ regenerate affected preparation
→ new production revision before production resumes
```

If no:

```text
CURRENT WRITER CONFIGURATION CANNOT PROCESS THIS SEMANTIC UNIT
→ Prompter / prompt-helper
→ Author + Doc Brown
```

No word-count cut is permitted.

---

# 11. SCIENTIFIC EDITOR — PRODUCTION-READINESS PASS

Before final marker freeze, the Scientific Editor performs a **production-readiness editorial pass** on the real manuscript.

The Editor may:

- polish scientific wording while SOURCE is still editable;
- flag places where a thesis and its qualification must remain in one move;
- identify natural move boundaries;
- identify likely BAD CUT;
- mark exact material that must be protected;
- check heading structure;
- flag places where Gemma would have to infer a missing premise or hidden continuation;
- exercise BAD CUT veto against a proposed segmentation.

The Editor does **not**:

- own production marker placement;
- independently create a parallel PROMPT_MAP;
- redefine machine marker syntax;
- silently change the literary/scientific authority model.

The Editor's segmentation comments are input to the Prompter.

Final marker + corresponding PROMPT_MAP remain one operation owned by the Prompter / future production-preparation role.

---

# 12. ROLE INTERFACE DURING PREPARATION

## PROMPTER

Owns:

- elementary prose move identification;
- marker placement;
- simultaneous PROMPT_MAP authoring;
- protected-span markup after Editor/Author determination of immutability;
- resegmentation after BAD CUT;
- preparation consistency before freeze.

Does not own:

- scientific truth;
- final Author decisions;
- machine/runtime design.

## METHODOLOGIST

Checks:

- whether the procedure is repeatable;
- whether hidden decisions remain;
- whether role boundaries drifted;
- whether unresolved decisions are correctly escalated;
- whether the prepared work can proceed to the next gate.

Does not choose literary boundaries instead of the Prompter.

## SCIENTIFIC EDITOR

Owns:

- scientific and semantic integrity of the manuscript;
- production-readiness editorial pass;
- BAD CUT veto;
- identification of protected material requiring exact preservation.

Does not own marker/PROMPT_MAP production.

## DOC BROWN

Checks only compatibility with the frozen engineering contract.

Does not choose literary boundaries.

## AUTHOR

Final authority over:

- substantive manuscript meaning;
- disputed boundary decisions;
- protected status where contested;
- readiness for production freeze.

---

# 13. RESEGMENTATION PROCEDURE

A proposed boundary is rejected when:

- the Editor exercises BAD CUT veto;
- the Prompter cannot state the two boundary answers cleanly;
- `LONG_RANGE_FRAME` and `LOCAL_TRANSFORMATION` reveal a hidden contradiction;
- the source move cannot stand without meaning supplied by the next block;
- a protected span would be crossed incorrectly;
- the block later proves oversized and is semantically divisible.

Then:

1. **RESEGMENT** the affected source region.
2. Recreate the affected marker IDs / marker graph as required.
3. Rewrite the corresponding `PROMPT_MAP` entries.
4. Re-run BAD CUT precheck for the new boundaries.
5. Return to Editor review where the semantic boundary changed.
6. If an active production revision had already been frozen, the change requires a **NEW PRODUCTION_REVISION**.
7. No accepted prefix or marker identity is automatically migrated in V1.

Before the first freeze, the preparation inputs remain editable and no run has yet been invalidated.

---

# 14. READY_FOR_PRODUCTION_FREEZE

A prepared manuscript may be declared:

```text
READY_FOR_PRODUCTION_FREEZE
```

only when all of the following are true.

## 14.1 SOURCE / marker checks

- every rewritable prose move begins with one valid MP marker;
- every production marker is outside protected spans;
- marker IDs are unique;
- SOURCE order is intentional;
- no sentence is cut;
- paragraph cuts, if any exceptional case exists, have explicit Editor + Author approval;
- every boundary has passed the two-question BAD CUT precheck.

## 14.2 PROMPT_MAP checks

For every SOURCE marker:

- exactly one matching PROMPT_MAP entry exists;

For every PROMPT_MAP entry:

- exactly one matching SOURCE marker exists;

And for every matched SOURCE / PROMPT_MAP pair:

- `LONG_RANGE_FRAME` is non-empty and minimally sufficient;
- `LOCAL_TRANSFORMATION` is non-empty;
- semantic stop is explicit;
- reader-state transition is explicit;
- no prompt instruction authorizes content absent from SOURCE;
- no LOCAL instruction contradicts its LONG_RANGE scope/closure condition;
- no instruction relies on CACHE as substantive authority.

## 14.3 Protected-material checks

- all Editor/Author-approved immutable material is either automatic heading passthrough or explicitly protected;
- protected IDs are unique;
- no nested protected spans exist;
- no production marker lies inside a protected span;
- ordinary rewritable prose has not been protected merely to avoid transformation.

## 14.4 Editorial / authority checks

- Scientific Editor has completed the production-readiness pass;
- all BAD CUT vetoes are resolved;
- all substantive scientific changes intended for this revision are already in SOURCE;
- `STABLE_CONFIG` intended for this production revision has already been approved by the responsible authority;
- no unresolved Author / editorial / process decision remains that, when resolved, would require changing any frozen component of this `PRODUCTION_REVISION`;
- Methodologist has no unresolved process/ZOR objection;
- Doc Brown has no frozen-SPEC compatibility objection;
- Author approves the prepared SOURCE + PROMPT_MAP for freeze.

Only then may the editable preparation inputs be converted into one frozen `PRODUCTION_REVISION`.

---

# 15. WORKED EXAMPLE — CURRENT AI-SOCIOLOGY ARTICLE

The example below uses the current manuscript's §1.6, **“The organizing question.”**

Purpose of the example:

- show that a reader-visible section can contain several production blocks;
- show that a heading is structural passthrough, not an MP marker;
- show simultaneous SOURCE + PROMPT_MAP preparation;
- show a load-bearing canonical sentence protected from literary rewrite;
- show semantic stops that differ from word-count cuts.

The example is illustrative only. It does not modify the article.

---

## 15.1 Prepared SOURCE excerpt

```markdown
## 1.6 The organizing question

<!-- MP:0101 -->
The observations are not a list of separate findings. They are measurements along one scale: the **scope over which a set of rules determines the type of response**.

<!-- MP:0102 -->
Such a set — called a *rule core* in §4.2, by analogy with a developmental rather than a replicative mechanism — fixes the *type* of response to a class of inputs while leaving the *content* of any particular response undetermined. That formulation is what makes the idea testable, since model outputs demonstrably vary across identical inputs.

<!-- MP:0103 -->
The scale runs from the single turn upward through the episode, the conversation, the account, and the model family. Two levels are supported here by preserved evidence: the episode (§6.1) and the conversation (§6.2). One is open (§6.4). One is untested and confounded (§6.5).

The programme therefore has one empirical question:

<!-- MP:PROTECTED id="P01_01":BEGIN -->
> **At what level of nesting is a rule core fixed?**
<!-- MP:PROTECTED id="P01_01":END -->

We prefer this to the broader formulations used in earlier drafts — the study of social behaviour in collaborative AI systems — because it specifies what would be measured and what would refute it.
```

### Why these boundaries

**Before MP:0101:** the previous section has finished the manuscript's supported operational claim.

**MP:0101 move:** reclassify the observations as measurements along a scale.

Boundary after MP:0101 is valid because the move “these are measurements, not a list” is complete before the construct underlying the scale is defined.

**MP:0102 move:** define `rule core` sufficiently to explain why the scale can be testable.

Boundary after MP:0102 is valid because the construct and its testability criterion are complete before the manuscript enumerates the levels.

**MP:0103 move:** enumerate the levels, state their evidential status, and convert the scale into the paper's single empirical question.

No marker is placed before the final sentence because that sentence explains why the question is preferred and therefore completes the same rhetorical move.

The exact central question is protected because in this example it is treated as Author/Editor-approved canonical wording. The surrounding prose remains rewritable.

---

## 15.2 Corresponding PROMPT_MAP excerpt

```yaml
MP:0101:
  LONG_RANGE_FRAME: |
    LOCATION:
    §1.6, "The organizing question", immediately after §1.5 has stated the
    strongest supported behavioural pattern.

    FUNCTION:
    Reframe the manuscript's observations as positions on one nesting scale
    rather than as a catalogue of separate findings.

    READER_STATE_BEFORE:
    The reader knows the article's strongest supported operational claim but
    has not yet been given the single organizing measurement axis.

    REQUIRED_READER_STATE_AFTER:
    The reader understands that the observations are being organized by scope,
    without yet needing the definition of rule core.

    CONSTRAINTS:
    Do not imply that every level of the scale is empirically established.
    Preserve the distinction between observations and the mechanism later
    proposed to organize them.

    CLOSURE:
    The local reframing may close here.
    Do not define rule core yet; that is the next move.

  LOCAL_TRANSFORMATION: |
    TRANSFORM:
    Render the source as a concise transition from a list-of-findings reading
    to a one-scale reading.

    PRESERVE:
    The scale variable is the scope over which rules determine response type.

    DO_NOT_INTRODUCE:
    No new scale levels, no causal mechanism, no stronger evidence claim.

    RHETORICAL_OPERATION:
    Reclassification / narrowing of the reader's frame.

    SEMANTIC_STOP:
    Stop once the reader understands that the observations belong to one scale.
    Do not begin the definition of rule core.

MP:0102:
  LONG_RANGE_FRAME: |
    LOCATION:
    §1.6, after the scale has been introduced and before its levels are listed.

    FUNCTION:
    Supply the construct that makes the scale operational and testable.

    READER_STATE_BEFORE:
    The reader knows there is one scale but does not yet know what is supposed
    to remain stable across that scale.

    REQUIRED_READER_STATE_AFTER:
    The reader understands that a rule core fixes response type while allowing
    content variation, and why that distinction creates a testable claim.

    CONSTRAINTS:
    Rule core is a construct, not an observed object.
    Preserve the developmental-not-replicative qualification.
    Do not turn the construct into an empirical finding.

    CLOSURE:
    The construct definition may close.
    Enumeration of nesting levels belongs to the next move.

  LOCAL_TRANSFORMATION: |
    TRANSFORM:
    Produce a clean conceptual definition of rule core and connect it directly
    to testability.

    PRESERVE:
    Type/content distinction.
    Developmental rather than replicative analogy.
    Output variability as the reason the claim remains testable.

    DO_NOT_INTRODUCE:
    No biological inheritance claim.
    No claim that a rule core has been directly observed.
    No enumeration of levels yet.

    RHETORICAL_OPERATION:
    Definition followed by methodological consequence.

    SEMANTIC_STOP:
    Stop only after the type/content distinction has been tied to testability.

MP:0103:
  LONG_RANGE_FRAME: |
    LOCATION:
    Final move of §1.6.

    FUNCTION:
    Convert the scale from an organizing device into the paper's single
    empirical programme question.

    READER_STATE_BEFORE:
    The reader understands both the scale idea and the rule-core construct.

    REQUIRED_READER_STATE_AFTER:
    The reader knows the scale levels and their unequal evidential status,
    and understands the exact empirical question that organizes the paper.

    CONSTRAINTS:
    Episode and conversation are supported by preserved evidence.
    Account remains open.
    Model family remains untested/confounded.
    Preserve the protected central question verbatim.
    Do not imply that the paper has answered the question at all levels.

    CLOSURE:
    §1.6 may close after explaining why this question is preferred to the older,
    broader formulation.

  LOCAL_TRANSFORMATION: |
    TRANSFORM:
    Present the scale compactly, preserve the unequal status of its levels,
    lead into the protected research question, and close by explaining why
    the question is methodologically stronger than the earlier broad framing.

    PRESERVE:
    Ordering of levels.
    Evidential asymmetry across levels.
    Protected question exactly as supplied.
    The reason for preferring the question: it specifies measurement and
    refutation.

    DO_NOT_INTRODUCE:
    No additional scale level.
    No claim that account or model-family levels are established.
    No new discipline claim.
    No paraphrase or duplication of the protected question.

    RHETORICAL_OPERATION:
    Enumeration → concentration into one question → local section closure.

    SEMANTIC_STOP:
    Stop only after the reader has both the exact question and the reason it
    replaces the broader earlier formulation.
```

---

# 16. WORKED EXAMPLE — BAD CUT COUNTEREXAMPLE

The following would be a BAD CUT:

```markdown
<!-- MP:0201 -->
The scale runs from the single turn upward through the episode, the conversation,
the account, and the model family. Two levels are supported here by preserved
evidence: the episode (§6.1) and the conversation (§6.2).

<!-- MP:0202 -->
One is open (§6.4). One is untested and confounded (§6.5).
```

Why invalid:

The first block would leave the evidential status of the scale artificially
stronger than the complete source permits. The second block would be forced to
repair the epistemic impression created by the first.

This violates the rule:

> **Do not cut a claim away from the qualification required to keep it scientifically correct.**

The correct preparation keeps the complete status sequence inside one move.

---

# 17. PREPARATION CHECKLIST — ONE PAGE VERSION

For each marker:

```text
[ ] I can name the move completed before this boundary.
[ ] I can name the different move beginning here.
[ ] No sentence is cut.
[ ] No load-bearing qualification is left for the next block.
[ ] Marker is outside protected material.
[ ] I wrote LONG_RANGE_FRAME now, not later.
[ ] I wrote LOCAL_TRANSFORMATION now, not later.
[ ] Reader state before/after is explicit.
[ ] Scope/closure is explicit.
[ ] Semantic stop is explicit.
[ ] SOURCE remains the substantive ceiling.
[ ] CACHE is continuity evidence only.
[ ] Protected material is exact and minimal.
```

For freeze:

```text
[ ] Every SOURCE marker has exactly one PROMPT_MAP entry.
[ ] Every PROMPT_MAP entry has a SOURCE marker.
[ ] Editor production-readiness pass complete.
[ ] All BAD CUT vetoes resolved.
[ ] All intended substantive changes already integrated.
[ ] No live Author decision would force this SOURCE to change.
[ ] Methodologist process/ZOR check passed.
[ ] Doc Brown compatibility check passed.
[ ] Author approved freeze.
```

---

# 18. STATUS

**PRODUCTION_PREPARATION_STANDARD — DRAFT v1.1**

Prepared by: **Prompter**

Next gate:

```text
Methodologist review
→ Scientific Editor real-manuscript segmentation test / BAD CUT review
→ Doc Brown frozen-SPEC compatibility check
→ Author approval
→ FROZEN PRODUCTION_PREPARATION_STANDARD
```

**STOP FOR TRIAD REVIEW.**
