# CHRONICLES_TTS_PILOT — editorial note

**Spec:** `CHRONICLES_TTS_EDITOR_SPEC_V1` + `CORRECTION 01` + `AUDIOBOOK PRODUCTION DECISION`
**Scope:** Front Matter + Prologue
**Source:** `Chronicles_of_Prompter_AUTHOR_FINAL_RU.md`, canonical Russian original
**Date:** 2026-10-22
**Supersedes** the Pilot 1 markup and note (166 short segments, Prologue + ch. 1). This is the successor, not a parallel experiment.

---

## 1. The structure

21 voice blocks over Front Matter + Prologue, median 41 s, longest 83 s (`PRO_002`, the whole first scene in one take). Estimated speech 11.8 min, montage pauses 0.3 min.

Cuts only where the decision allows one: change of speaker, live↔ARCHIVE, structural section, scene change. The build **refuses to emit an unjustified cut** — two adjacent blocks sharing a voice and a process with no structural reason between them fail it. Irony, a short strong sentence and a pre-assertion pause cut nothing; they live inside a block and are carried by the book's own punctuation, preserved as paragraphs.

| Boundary | Reason |
|---|---|
| FM_001 → 002 → 003 → 004 | front-matter sections: title page, Integrator's note, Справка, frontispiece caption |
| FM_004 → PRO_001 | chapter heading |
| PRO_001 → PRO_002 | speaker change, INTEGRATOR → PROMPTER_OLD |
| ends of PRO_002/003/007/011/012/016 | scene change (`***`) |
| PRO_004 → 005 → 006 | live ↔ ARCHIVE, Claude's battle verdict |
| PRO_008 → 009 → 010 | live ↔ ARCHIVE, DeepSeek's referee verdict |
| PRO_013 → 014 → 015 | speaker change, the Keeper's one live line |
| PRO_016 → PRO_017 | structural: source note, and a speaker change |

`RATE` is one value per block, at base, with one declared exception below.

## 2. Source notes — `SOURCE_NOTE_RAPID` at 1.50

`PRO_017`, the Prologue's source note, now runs `INTEGRATOR` / `SOURCE_NOTE_RAPID` / `RATE 1.50`, unsplit, as the largest continuous block its voice allows.

It is the right one to hear first, because it is the worst case: it carries `29 июля 2025 года`, `26 августа`, `27 августа`, `Qwen 2.5-Coder`, `Qwen3-235B`, `GPT-4o`. Across the book, **15 of the 17 source notes contain numbers and 8 contain filenames or codes** — so whatever 1.50 does to dates and model identifiers, it will do seventeen times. Partial loss there is accepted by decision; the pilot shows what "partial" sounds like before it is applied everywhere.

Full-book effect: 3,095 words of source notes, 8.8% of the text — ~22.4 min at base, ~14.3 min at 1.50.

`FM_003`, «Справка Интегратора о сохранности материалов», stays `INSTITUTIONAL_NEUTRAL` / `0.96`. It sets out the documentary rules of the book for the listener rather than serving as end-of-chapter apparatus.

## 3. The new provenance gate

The old invariant (audio equals the published book word for word) cannot survive an adapted audio edition, and pretending otherwise would be worse than losing it. It is replaced by:

```
CANON = AUDIO TEXT + APPROVED CONTRACTION REGISTRY + DECLARED AUTHOR CORRECTIONS
```

The build enforces it mechanically. A canonical line may be absent from the audio **only** if an APPROVED record in `registry.json` claims it; a line both claimed and spoken fails; a line neither claimed nor spoken fails; replacement prose must be declared, never improvised; surviving text keeps canonical order; and the word stream must still match exactly, so no undeclared new prose can enter.

Verified by negative test rather than assertion:

```
registry claims a line a block still speaks  -> block speaks line 302, which registry TEST_X omits / GATE FAILED
a block silently drops a canonical line      -> LOST: [302] / GATE FAILED
```

Current state for this pilot:

```
canonical spoken lines in scope : 142
spoken in the audio             : 142
omitted by approved contraction : 0
declared author corrections     : 2
undeclared new prose            : none
registry records total          : 1 approved, 0 pending
  CONTRACTION_001  Duplicated Integrator source note  outside scope, lines 9829-9843, delta: none
```

## 4. The Author's correction

Applied at lines 3 and 5. The diff against the published canon reports exactly two differences and nothing else — both the ordered substitution. Line 322 (`состав AI Collaboration проекта ВПК`) is ruled and will be applied when Chapter 1 is marked up. «человеческо-ИИ коллаборации» at lines 12 and 20 is not the named term and stays.

## 5. `[[EN]]` — seven marks

Lines 3, 5 `AI Collaboration`; line 6 `Human curator / publication authority`; lines 8, 24 `Chief Integrator / Methodologist`; line 22 `prompt engineering`; line 48 `Specialized AI`. Service markup: stripped before the word-stream check, so it can add or remove nothing, and it does not split the block it sits in.

Left unmarked: `Claude`, `Grok`, `Qwen`, `DeepSeek`, `ChatGPT`, `A.Tuin`, `ZOV`, `ZOR`, `AI-Sociology`, `AI-Colab`, `ВПК/ТД`, `HDD D:`, `GPT-4o`, `Qwen 2.5-Coder 32B`, `Qwen3-235B`, `web-коллаборация` — and, by decision, `Cloude` / `Qwan` / `DeseSook` in `PRO_002`. Render those normally first; if the pronunciation fails, the three names get a separate RU/EN comparison and the Author picks.

## 6. Duration

The whole book is **34,980 spoken words** → ~4 h 13 min of speech at the pilot's pace, before production pauses. With rapid source notes and approved contractions, under four hours. My earlier "about fifteen hours" was an unchecked guess, wrong by a factor of 3.5, and is withdrawn.

## 7. What this pilot still does not exercise

`MISS_DUSHNILA` and `PROMPTER_YOUNG` have no blocks: she is described three times in the Prologue but never speaks, and the young Prompter begins at ch. 13. The pilot therefore calibrates the narrator, the Integrator, the archive and the rapid apparatus only. If her voice and the dynasty seam should be settled before full-book markup, the cheapest addition remains the `Стул` section plus the first page of ch. 13, which exercises Miss Dushnila, the seam pause, the archive announcement and the young Prompter at once.

## 8. Unchanged

`PAUSE_BEFORE` 0 throughout; the whole montage gap sits in the preceding block's `PAUSE_AFTER`, so no gap can be double-counted. All `@` fields are production metadata: what goes to OmniVoice is only the text between the blank line after the header and `@END`.

СЛЕД ≠ ПАМЯТЬ held: the two preserved verdicts are the only `ARCHIVE` blocks, and *«Давайте теперь построим мультиагентную систему»* stays in the narrator's voice because it is a phrase the book denies, not a record. No `AUTHOR` voice anywhere.

No voice chosen or described, no `instruct` written, no model parameter touched, no script or audio step produced.
