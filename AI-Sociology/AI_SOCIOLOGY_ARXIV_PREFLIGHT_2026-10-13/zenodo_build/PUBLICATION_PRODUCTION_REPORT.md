# PUBLICATION_PRODUCTION_REPORT

**Role:** Publication Editor / Manuscript Production Editor
**Mode:** PUBLICATION PRODUCTION — SCIENCE FROZEN
**Date:** 2026-10-13
**Returned to:** Chief Integrator, for arXiv validation and the Author publication card
**Not submitted anywhere.**

---

## 1. Input verification

Both frozen masters were hashed before anything was touched and match the Integrator's declared provenance byte for byte:

| Object | Declared blob | Measured | |
|---|---|---|---|
| `BEYOND_PROMPT_ENGINEERING_CHIEF_EDITOR_FINAL_CANDIDATE.md` | `7b380cb4…` | `7b380cb41659e1570c0194b0a2b4963f6388c259` | ✓ |
| `BEYOND_PROMPT_ENGINEERING_CHIEF_EDITOR_FINAL_RU.md` | `897157b7…` | `897157b7017c371582eefa24fdf1559d89b69020` | ✓ |

The English master was inventoried before conversion: 1 920 lines, 30 522 words, 12 `#` / 105 `##` / 71 `###` headings, 16 tables, 27 block quotations, 25 lists, 1 fenced block (the front matter), 12 section rules, 294 §-cross-references across 80 targets, and exactly eight distinct non-ASCII glyphs.

---

## 2. What was produced

| File | Status |
|---|---|
| `main.tex` | top-level XeLaTeX file, three release switches |
| `preamble.tex` | shared preamble, no article prose |
| `metadata.tex` | title / author / abstract — **blocked, see B2/B3** |
| `article_en.tex` | English edition, technical conversion |
| `appendix_a.tex` | **placeholder — blocked, see B1** |
| `article_ru.tex` | Russian edition, technical conversion |
| `article_nl.tex` | Dutch edition, new translation |
| `references.bib` | 25 entries, keyed and compiling |
| `NL_AMBIGUITY_LEDGER.md` | 4 standing decisions, 9 flagged items |
| `main.pdf` | 210 pp., compiled proof |

Compile command: `xelatex main && bibtex main && xelatex main && xelatex main`.

---

## 3. Proof that the conversion is technical only

Each edition was converted by one deterministic converter that raises on any construct it does not recognise, and each result was then **stripped back to a plain word stream and diffed against its source**. A single word added, dropped or reordered fails the check.

| Edition | Source words | TeX words | Result |
|---|---|---|---|
| English | 29 837 | 29 837 | **ROUND-TRIP IDENTICAL** |
| Russian | 25 777 | 25 777 | **ROUND-TRIP IDENTICAL** |
| Dutch | 31 179 | 31 179 | **ROUND-TRIP IDENTICAL** |

No sentence required reformulation to pass into TeX. There are no STOP items under task 1.

### Conversion decisions worth recording

**Sectioning is starred, with literal numbers.** The section numbers are part of the frozen text, and the English master has **no §8.4**. Automatic numbering would silently renumber §8.5 to §8.4 and shift everything after it, breaking the printed numbers that the article's own 294 cross-references depend on. Every heading is therefore `\section*{…}` carrying the frozen number as literal text, with `\phantomsection`, a label and a TOC entry.

**Cross-references became links without changing a character.** `§4.5.4` renders exactly as the source writes it and now also links to that section. All 294 uses resolve; **none is dangling**. Labels are namespaced per edition (`sec:en:…`, `sec:ru:…`, `sec:nl:…`), which fixed a real defect found mid-build: without namespacing, 133 labels were multiply defined and every Russian cross-reference pointed into the English edition.

**Glyphs are routed through macros.** `✓ ⚠ ↔ → × §` are emitted as `\gcheck \gwarn \gharr \grarr \gtimes \gsect`, because the printed character must not depend on one font being installed — verified locally: the first font the cascade picked carries neither U+2713 nor U+26A0, and would have dropped both silently.

**The front matter is typeset, not shown as code.** The masters carry the author and AI-contributor block inside a fenced block. It is reproduced word for word in a preformatted environment; only the typesetting changed.

---

## 4. Bibliography

The Integrator's `references_preflight.bib` was used as supplied. **The source-forensics audit was not re-run**; it is closed upstream.

- Every author/venue mention in the English master was located and mapped to a key: **25 works, 29 citation points, zero orphan entries, zero uncited entries** — with one exception below.
- Keys are attached as `\nocite` at each mention point. This is deliberate: the frozen prose already carries full narrative citations ("✓ CAMEL (Li et al., NeurIPS 2023)"), so inserting `\citep` would have printed a second, duplicate citation and changed the visible text. `\nocite` makes every work resolve in the reference list while leaving the prose untouched.
- **Purely technical duplicates: none found.** `choi2025debateorvote` and `choi2026identity` are two distinct works, correctly split in the frozen text and consistent with rows SF-015/SF-016 and finding P2 of the source-forensics registry. Nothing was removed.
- Three technical normalizations, none touching a claim/source relation: all title fields brace-protected, so `MetaGPT` and `CAMEL` are not lowercased to `Metagpt` and `Camel`; `howpublished = {arXiv:NNNN.NNNNN}` added to the three preprints, because `plainnat` prints neither `eprint` nor `archivePrefix` and the frozen text cites those works **by their arXiv identifier**; `zhang2025overvaluing` carries `arXiv:2502.08788v3`, the version the text states.

---

## 5. Compile and validation

Final build, three editions:

```
errors              0
missing characters  0
multiply-defined    0
undefined refs      0
undefined citations 0
overfull hboxes     2
underfull vboxes    0
pages               210
```

The two remaining overfull boxes are 8 pt and 33 pt on ~430 pt lines, caused by unbreakable hyphenated compounds; they are below the threshold at which a reader notices.

Visual inspection: title page, table of contents, the widest table (§5.3 consolidated record), a §-boundary page, the Appendix A placeholder, the first Russian page, the first Dutch page, and the reference list were rasterized and read. Tables set correctly with `booktabs`; no page-break defect was found.

**Local toolchain caveat.** This container's TeX Live carries no Cyrillic hyphenation patterns, so the Russian edition is set without hyphenation here. arXiv's TeX Live has them; the only symptom is slightly looser Russian justification in this proof PDF than in the submitted one. Dutch hyphenation is present and working.

**Font selection** is a cascade (`Libertinus Serif → Liberation Serif → DejaVu Serif → FreeSerif → TeX Gyre Termes`), ordered among fonts that carry both Latin and Cyrillic. TeX Gyre Termes is last on purpose: this build of it has no Cyrillic, which would have dropped the entire Russian edition from the PDF without an error.

---

## 6. Dutch edition

Translated **directly from the frozen English master**, never through the Russian. Structural parity with the English is exact and was measured, not assumed:

| | English | Dutch |
|---|---|---|
| Headings | 188 | 188 |
| Heading numbers and levels | — | 0 mismatches |
| Paragraphs | 592 | 592 |
| Tables (shape for shape) | 16 | 16 |
| §-cross-references | 294 / 80 targets | 294 / 80 targets, identical distribution |
| `[P]` / `[P-A]` / `[R]` / `[H]` | 23 / 19 / 19 / 18 | 23 / 19 / 19 / 18 |
| ✓ verification marks | 37 | 37 |
| E1–E8 and C1–C9 labels | — | identical |

Counts were checked occurrence by occurrence, not in aggregate: *eight* / *acht* and *six* / *zes* match position for position in all four places they appear.

`NL_AMBIGUITY_LEDGER.md` records four standing decisions requiring the Author's confirmation (English technical vocabulary retained; the plural of *menom*; the §11.3 outcome-category labels; the handling of labels adjoining a hyphen) and nine places where the English admits two Dutch readings. One of those, B-2, is the single sentence in the edition where the Dutch had to be more explicit than the English, because Dutch has no pronoun that carries the anaphor.

**No independent fidelity QA pass has been run.** The translator brief requires one. The Dutch edition should not be published as a sibling until it has.

`\IncludeDutchtrue` is set in this proof so the Author can read all three editions in one PDF. For an English+Russian v1, that is one line.

---

## 7. PUBLICATION_BLOCKERS → Integrator → Author

### B1 — Appendix A primary evidence missing *(hard, carried from the preflight)*

The frozen article states that Appendix A contains the full protocol, the exact intervention texts and the complete unedited responses. Those records have not been supplied. `appendix_a.tex` is a placeholder with the construction rule written into it. **No part of Appendix A was reconstructed from the article's prose, from Protocol_001, or from anything else.** `APPENDIX_A = BLOCKED`.

### B2 — Title and abstract pending approval *(carried from the preflight)*

The frozen master has neither. `metadata.tex` carries the Integrator's proposal unchanged and marked as not approved; the title page prints an "INTERNAL PROOF COPY — NOT FOR SUBMISSION" banner until `\ApprovedMetadatatrue` is set.

### B3 — Author metadata *(carried from the preflight)*

The printed front matter says `V. Krasnianskyi (A'Tuin)`; the proposed arXiv metadata says `V. Krasnianskyi`. The title page follows the frozen manuscript. The metadata form is the Author's decision and is not settled here.

### B6 — NEW, HARD: the Russian edition was translated from a superseded English blob

The translator's note at the head of the Russian master declares its source as blob `fd489fcafaa9cedddf41d45ef4cd93e7cf49385a`. The frozen English master is `7b380cb4…`. Both objects were recovered from the repository and diffed. **The two differ in exactly two paragraphs, both in §12.7, and both are evidential-status corrections:**

**1.** English (frozen): *"reluctance to affirm as true propositions about itself that were not established by the available interaction."*
Russian (from the superseded blob): *«нежелание подтверждать о себе то, чего ни одна из сторон не могла проверить»* — the withdrawn `neither party could check` formulation.

**2.** English (frozen): *"a persistent response pattern was observed … This is the evidence on which the episode-level placement rests."*
Russian: *«на уровне эпизода наблюдалось, как ядро фиксируется и сохраняется»* — the withdrawn `a core was observed to fix and to persist`, which contradicts §4.2.1 of the same article (*"A rule core is not observable. Behaviour is."*). The two added sentences stating what the placement rests on are absent from the Russian.

Published as one multilingual arXiv item, this would ship in Russian two formulations the English version explicitly retracted. **Not repaired here:** the Russian is an approved translation sibling and the change touches evidential status, which is outside this role's authority. The correction belongs to whoever owns the Russian translation, with the Author's approval.

The divergence is **bounded and complete** — the full diff between the two blobs is those two paragraphs and nothing else. Everything else in the Russian was verified against the English: 188 headings with identical numbering and levels, 16 tables of identical shape, 592 paragraphs in both, identical E- and C-labels, and 295 vs 294 §-references, the one extra being a translator's device that repeats `§6.2` where the English uses the pronoun *it*. That one is harmless.

### B7 — NEW, soft: the Russian edition carries an internal translator's note

The Russian master opens with a note addressed to the Author (*«предназначенный для проверки Автором»* — "intended for checking by the Author") and quoting the source blob hash. It is preserved verbatim in `article_ru.tex`, because removing it would be an editorial change. Whether an internal review note belongs in a published arXiv item is the Integrator's call.

### B8 — NEW, soft: the English master has no §8.4

Sections run 8.1, 8.2, 8.3, **8.5**, 8.6 … and §8.11 refers the reader to the range "§8.1–§8.5", which therefore spans a gap. Nothing is broken: §8.4 is never the target of a cross-reference, and all 294 references resolve. Renumbering would change the frozen text and every reference into §8, so nothing was done. Flagged because it is visible on the page.

### B9 — NEW, soft: George Kelly is attributed but not in the bibliography

§8.11 and §11.4 (E8) rest substantively on Kelly's personal-construct theory, triadic elicitation and the repertory grid, naming him six times. `references_preflight.bib` has no Kelly entry. The frozen text names no work and no year for him, so supplying one would create a claim/source relation the article does not make. Author's decision: leave the attribution uncited, or approve an entry.

---

## 8. State

| | |
|---|---|
| English master → LaTeX | **done**, round-trip verified |
| Russian master → LaTeX | **done**, round-trip verified; content blocked on B6 |
| Dutch edition | **done**, parity verified; QA pass outstanding |
| Bibliography | **done**, compiles, 25/25 resolved |
| Appendix A | **BLOCKED — B1** |
| Title / abstract / author metadata | **BLOCKED — B2, B3** |
| Compiled PDF | **proof only**, 210 pp., not for submission |
| arXiv source bundle | **not finalizable** until B1, B2, B6 are closed |
| Submission | **not authorized, not performed** |

Once B1 arrives, assembling Appendix A and releasing the metadata switches is the remaining work; everything else in the bundle is finished and verified.
