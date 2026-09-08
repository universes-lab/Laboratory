# PROMPTER NOTE — Manuscript_Press paired generation v2

## Status

Revised after Editor-in-Chief review.

## Core runtime rule

> **KEEP MODEL — RESET SESSION — INJECT ONLY DECLARED CONTINUITY**

Keep Gemma weights resident in memory.

Do **not** preserve conversational/KV state between paired generation operations.

Part 1 and Part 2 remain separate controlled inference contexts.

---

# 1. ZOR split

## DOCTOR

Owns:

- `Gemma.md`;
- runtime/model configuration;
- model loading;
- session/KV reset;
- actual context delivery;
- delivery diagnostics;
- logging of the exact input manifest received by each run.

## EDITOR-IN-CHIEF

Owns the **semantic content** of continuity capsules:

- which terms have already been introduced;
- which claims have already been covered;
- evidential status `[P] / [P-A] / [R] / [H]`;
- which material must not be reintroduced or repeated;
- chapter-level continuity facts that are canonically safe to expose.

## PROMPTER

Owns the **executable projection** of those capsules into Gemma-facing instruction form:

- negative wording;
- prohibition structure;
- operational placement;
- model-readable constraints;
- transformation of Editor content into non-source control text.

Formula:

> **Editor says WHAT must be carried across.  
> Prompter decides HOW Gemma may receive it.**

Prompter must not alter evidential status or add semantic content.

---

# 2. PART_HANDOFF — negative form only

The Editor's objection is accepted.

Part 2 must not receive a positive summary of what the reader already knows.

That would recreate the very premise from which Gemma can invent a bridge.

Therefore `PART_HANDOFF` is **negative-only**.

Canonical form:

```text
PART_HANDOFF — CONTEXT ONLY — NOT A CONTENT SOURCE

Do not introduce as new:
- [term A]
- [term B]
- [term C]

These terms have appeared earlier in the chapter.
Use them without definition or first-mention framing.

Do not restate:
- [claim IDs already covered]

Do not refer to what precedes this text.
It exists, you have not been given it, and no sentence in your output
may point at it, summarize it, explain it, or construct a transition to it.

Begin with the content of:
- C-[first claim of this package]

Nothing in this capsule may be quoted, expanded, paraphrased into a claim,
or used to construct a causal or rhetorical bridge.
```

## Important distinction

### Allowed
Negative continuity:
- do not redefine X;
- do not restate C1–C4;
- do not frame Y as newly introduced.

### Forbidden
Positive continuity:
- "the reader already knows that A caused B";
- "the previous section established...";
- summaries of Part 1;
- narrative state descriptions from which a transition can be inferred.

The purpose of `PART_HANDOFF` is only to prevent duplication.

It must not help Gemma understand the seam.

The seam belongs to the Editor.

---

# 3. CHAPTER_CONTEXT

A new chapter is different.

A chapter may legitimately open with awareness of established book context.

Therefore limited positive continuity is allowed.

Maximum recommended size:

> **120 words**

No narrative recap.

No prose such as:

> "In the previous chapter we showed..."

Allowed contents only:

- already introduced terms;
- already established claims that must not be reintroduced;
- evidential status of those claims;
- facts whose repetition would create false first-mention framing.

Header:

```text
CHAPTER_CONTEXT — CONTEXT ONLY — NOT A CONTENT SOURCE

Use this only to avoid repetition and false first-introduction framing.

Do not quote or summarize this context.

No claim from this capsule may appear in the manuscript unless it is also
supported by the current Concept Package.

Do not refer to previous chapters merely because this context exists.
```

---

# 4. Capsule authorship workflow

Preferred workflow:

1. Editor creates semantic capsule content.
2. Prompter checks that no item expands Gemma's semantic freedom beyond the current package.
3. Prompter converts it into the executable negative/control form.
4. Doctor ensures the exact capsule is physically delivered.
5. Runtime log records delivery.

Gemma does not author its own continuity state.

If a Gemma-generated summary is ever tested:

`UNTRUSTED_GENERATED_STATE`

It must be externally verified before reuse.

---

# 5. Paired run

For one chapter:

```text
LOAD GEMMA ONCE

RUN PART 1
  Syst_Prompt
  → CHAPTER_CONTEXT
  → 01.CONCEPT_PACKAGE
  → 01.CONCEPT_PACKAGE_Prompt
  → CONSTANTS_CHECK
  → OUTPUT

SAVE OUTPUT
RESET SESSION / KV CONTEXT

RUN PART 2
  Syst_Prompt
  → CHAPTER_CONTEXT
  → PART_HANDOFF
  → 02.CONCEPT_PACKAGE
  → 02.CONCEPT_PACKAGE_Prompt
  → CONSTANTS_CHECK
  → OUTPUT

SAVE OUTPUT
ASSEMBLE
EDITOR WRITES / ADJUSTS SEAM
```

Model remains loaded.

Conversation does not.

---

# 6. Constants check

Constants check runs separately for every generation operation.

Add explicit delivery verification.

For all runs:

```text
chapter context capsule expected / received ........ YES / NO / N-A
```

For even / second-half packages:

```text
part handoff capsule expected / received ........... YES / NO
```

A run with an expected capsule marked `NO` is invalid.

This is necessary because continuity capsules are deliberately non-quotable;
their absence may otherwise leave no visible trace in manuscript output.

---

# 7. First action before any paired-run engineering

No new architecture is accepted until this is complete:

> **R2 becomes the only standard `01.CONCEPT_PACKAGE_Prompt.md`.**

The obsolete 108-line version is physically removed from `Input`.

The current build must not have two competing prompt versions.

Only after that correction is verified should Grok prepare engineering requirements
for the paired-run workflow.

---

# 8. Final Prompter ruling

Accepted:

> **negative-only `PART_HANDOFF`**

Accepted:

> **Editor owns capsule semantics; Prompter owns executable projection**

Accepted:

> **per-run delivery check in CONSTANTS_CHECK**

Retained:

> **KEEP MODEL — RESET SESSION**

Rejected:

> continuous hidden Gemma conversation between paired runs

Rejected:

> Gemma-generated authoritative continuity cache

The target architecture is therefore:

> **one loaded model  
> + two clean inference contexts  
> + Editor-authored semantic continuity  
> + Prompter-controlled projection  
> + Doctor-verified delivery  
> + Editor-owned seam**
