# AI-Sociology — arXiv Publication Integration Preflight

**Date:** 2026-10-11  
**Role:** Chief Integrator / Methodologist  
**Scope:** publication integration only; scientific/editorial text is frozen.

## Frozen source objects

- English master: `AI-Sociology/01_Theory/BEYOND_PROMPT_ENGINEERING_CHIEF_EDITOR_FINAL_CANDIDATE.md`
  - Git blob SHA: `7b380cb41659e1570c0194b0a2b4963f6388c259`
- Russian approved translation:
  `AI-Sociology/01_Theory/BEYOND_PROMPT_ENGINEERING_CHIEF_EDITOR_FINAL_RU.md`
  - Git blob SHA: `897157b7017c371582eefa24fdf1559d89b69020`

No prose change is authorized by this preflight.

---

## Publication decision

### arXiv placement

**Primary category:** `cs.MA — Multiagent Systems`  
**Cross-list:** `cs.HC — Human-Computer Interaction`

Reason: the paper's organizing object is role-structured interaction/coordination among language-model participants and long-lived agent-like conversations, while the human-mediated collaboration and interface context also make `cs.HC` materially relevant. `cs.CL` is not recommended as a default category because the paper is not primarily an NLP-method paper.

### Submission format

Use **LaTeX source, compiled with XeLaTeX**, rather than a PDF-only submission.

Planned source layout:

```text
main.tex
article_en.tex
appendix_a.tex
article_ru.tex
references.bib
```

If a Dutch edition is later included in the same arXiv item:

```text
article_nl.tex
```

No figures are present in the frozen Markdown masters. The English source contains many tables; these require technical LaTeX table conversion and compilation checks.

### Russian version

**Recommended treatment: one multilingual arXiv item, not a second arXiv submission and not an ancillary file.**

Order:

```text
English complete version
→ Russian complete version
```

arXiv's current multilingual policy explicitly permits this and requires the English version first. Full-text translations should not be placed in `anc/`, because full text there is not indexed.

### Dutch version

The Dutch edition is useful as a public sibling edition, but **must not block the first arXiv release**.

Recommended workflow:
1. freeze the approved English source;
2. give it to a dedicated, narrow **Edition Translator — EN→NL**;
3. translator has no authority to improve, correct, or reinterpret the article;
4. perform a separate fidelity/terminology QA pass;
5. publish the Dutch edition in the repository;
6. include it in the same arXiv multilingual item only if ready before submission and Author explicitly wants a three-language PDF; otherwise link it later as a public sibling edition.

Recommended occupant for the translation task: **a fresh dedicated ChatGPT translation chat**, not Claude/Grok/Keeper/Prompter in their scientific/governance roles.

---

## Proposed metadata — Author approval required

**TITLE**  
Beyond Prompt Engineering: Role Reconfiguration in Long-Lived AI Conversations

**AUTHOR metadata**  
V. Krasnianskyi

The printed manuscript currently contains `V. Krasnianskyi (A'Tuin)`. arXiv metadata should use the accurate registered author identity. Whether `(A'Tuin)` remains only in the printed manuscript or also appears in metadata must match the Author's arXiv account/identity and should not be improvised.

**ABSTRACT** — 1462 characters, below arXiv's 1920-character limit

This paper reports a field study of long-lived, persistently specialized language-model conversations used in a human-directed research collaboration, with one designed role-reconfiguration intervention embedded in the record. Two dormant conversations from different model families were each subjected to three sequential attempts to change professional function. The preserved responses support a narrow pattern: resistance tracked prompts that required the recipient to affirm unverifiable propositions about its own identity, history, or institutional relationships, rather than the magnitude of role or domain change. A rewritten prompt that removed such self-claims was accepted without negotiation. Ancillary observations suggest persistent effects at the episode and conversation levels, while account-level effects remain open and model-family effects are untested because family and trajectory were confounded. We distinguish represented social position and represented social source from implemented multi-agent interaction, propose a count of unverifiable self-claims as an operational prompt variable, and describe conversational branch reset as a control procedure. The evidence is limited to one project, one human operator, one observation per condition, no blinding, and no replication. The paper therefore presents a testable research programme and design rules rather than evidence that any collaborative architecture outperforms alternatives.

**CATEGORIES**  
Primary: `cs.MA`  
Cross-list: `cs.HC`

**COMMENTS — draft**  
English and Russian versions included. AI language tools contributed to manuscript development, scientific editing, methodological review, and ontology review; all final decisions and responsibility for the paper remain with the human author.

If Dutch is included in v1, change first sentence to:  
`English, Russian, and Dutch versions included.`

**LICENSE — proposed**  
`CC BY 4.0`

Reason: open reuse with attribution and good fit with the project's open-research intent. The choice is irrevocable on arXiv; if a specific target journal is already planned, its preprint/license policy should be checked before final selection.

**AI CONTRIBUTION DISCLOSURE**  
Retain the existing front-matter disclosure in the frozen manuscript. arXiv currently states that generative AI tools must not be authors and that significant use should be reported. Metadata Authors therefore contain only the human author.

---

## Additional repository materials — what is needed

### REQUIRED FOR THE PAPER

**1. Appendix A / primary evidence package — HARD BLOCKER**

The frozen article explicitly states that Appendix A contains:
- the full protocol;
- exact intervention texts;
- complete unedited responses.

`AI-Sociology/02_Protocols/Protocol_001_Role_Reconfiguration_v1.0.md` is useful and should be part of the construction basis, but it is not enough by itself: it explicitly says that complete responses should be preserved as unedited appendices or linked source transcripts.

The complete primary transcripts/responses have not been located in the currently inspected `AI-Sociology` tree.

Required action:
`PUBLICATION_BLOCKER → Author / Prompter: locate/supply the primary transcripts used to construct Appendix A.`

No reconstruction from prose summaries is allowed.

**2. Bibliography**

A preflight `references_preflight.bib` accompanies this report. It is assembled from:
- the final article's live citations;
- the completed source-forensics registry;
- current primary bibliographic pages for the remaining cited works.

It still requires final citation-key insertion during Markdown→LaTeX conversion and a compile/cross-reference check.

### USEFUL INTERNALLY, NOT PART OF THE arXiv ARTICLE BY DEFAULT

- `AI_SOCIOLOGY_SOURCE_FORENSICS_CURRENT_WARNING_REGISTRY.md` — provenance for bibliography/source validation; do not publish as article content by default.
- `PRODUCTION_PREPARATION_STANDARD_DRAFT_v1.1.md` — production/process document, not paper supplement.
- `GEMMA-Press.md`, `Metsuku_Topic.md` — protocol/history material; do not dump into arXiv unless a specific Appendix-A evidence item requires them.
- `Three-Point Context Principle.md` and `Triadic Execution Context.md` — separate research material; not part of this article.
- `03_Replication/` — do not include merely because it exists; the current paper describes proposed future experiments and must not imply completed replication that the frozen text does not claim.

---

## Current arXiv blockers

### B1 — HARD: Appendix A is missing
The manuscript points to primary material that is not present in the final publication object.

### B2 — AUTHOR APPROVAL: title and abstract
The frozen Markdown has neither a title heading nor an abstract section. A publication-safe title and abstract are proposed above. They must be approved before they are inserted.

### B3 — AUTHOR METADATA
Confirm the exact arXiv author identity and treatment of the pseudonym `A'Tuin`.

### B4 — ACCOUNT-SIDE / SUBMISSION-TIME
arXiv may require endorsement for a first submission or a new category. This can only be checked from the Author's arXiv account during the submission workflow.

### B5 — NOT BLOCKING: Dutch translation
Recommended, but it should not delay the English/Russian arXiv item unless the Author explicitly chooses a three-language v1.

---

## Validation state

**Scientific/editing:** CLOSED by upstream authority.  
**Source audit:** final text reports no provisional citations.  
**Markdown source provenance:** anchored by Git blob SHAs above.  
**Title:** DRAFT — Author approval required.  
**Abstract:** DRAFT — Author approval required.  
**Bibliography:** PREFLIGHT PREPARED.  
**Appendix A:** MISSING — HARD BLOCKER.  
**LaTeX source:** NOT FINALIZABLE until B1/B2 are resolved.  
**Compiled PDF:** NOT FINALIZABLE until B1/B2 are resolved.  
**arXiv source bundle:** NOT FINALIZABLE until B1/B2 are resolved.  
**Submission:** NOT AUTHORIZED / not technically ready.

---

## Publication card — current

`TITLE`  
Beyond Prompt Engineering: Role Reconfiguration in Long-Lived AI Conversations

`AUTHOR`  
V. Krasnianskyi

`ABSTRACT`  
This paper reports a field study of long-lived, persistently specialized language-model conversations used in a human-directed research collaboration, with one designed role-reconfiguration intervention embedded in the record. Two dormant conversations from different model families were each subjected to three sequential attempts to change professional function. The preserved responses support a narrow pattern: resistance tracked prompts that required the recipient to affirm unverifiable propositions about its own identity, history, or institutional relationships, rather than the magnitude of role or domain change. A rewritten prompt that removed such self-claims was accepted without negotiation. Ancillary observations suggest persistent effects at the episode and conversation levels, while account-level effects remain open and model-family effects are untested because family and trajectory were confounded. We distinguish represented social position and represented social source from implemented multi-agent interaction, propose a count of unverifiable self-claims as an operational prompt variable, and describe conversational branch reset as a control procedure. The evidence is limited to one project, one human operator, one observation per condition, no blinding, and no replication. The paper therefore presents a testable research programme and design rules rather than evidence that any collaborative architecture outperforms alternatives.

`CATEGORIES`  
cs.MA (primary); cs.HC (cross-list)

`COMMENTS`  
English and Russian versions included. AI contributions disclosed in the manuscript.

`LICENSE`  
Proposed: CC BY 4.0

`FILES`  
Planned: `main.tex`, `article_en.tex`, `appendix_a.tex`, `article_ru.tex`, `references.bib`; optional `article_nl.tex`

`RUSSIAN_VERSION_TREATMENT`  
Same multilingual arXiv item, after the English version; not ancillary and not a separate arXiv item.

`AI_CONTRIBUTION_DISCLOSURE`  
Existing functional contributor block retained; AI systems are not metadata authors; human author bears final responsibility.

`BLOCKERS`  
B1 Appendix A primary materials missing; B2 title/abstract approval; B3 exact author metadata; B4 possible arXiv endorsement at submission time.

---

## Next gate

Once the Author supplies/locates Appendix A primary traces and approves title/abstract:

1. technical Markdown→XeLaTeX conversion without prose rewriting;
2. bibliography keying and reference normalization;
3. assemble English → Appendix A → Russian;
4. compile;
5. inspect tables/page breaks/cross-references;
6. produce PDF and source archive;
7. final arXiv metadata card;
8. Author approval;
9. submission.
