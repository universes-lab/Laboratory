# CHRONICLES_TTS_PILOT — editorial note

**Spec:** `CHRONICLES_TTS_EDITOR_SPEC_V1`
**Role:** Production Editor / TTS Director
**Scope delivered:** front matter + Prologue + Chapter 1 (PILOT, per §22)
**Source:** `AI-Sociology_Other/Chronicles_of_Prompter/Chronicles_of_Prompter_AUTHOR_FINAL_RU.md`,
the canonical Russian original named by `CHRONICLES_PUBLICATION_MANIFEST_2026-10-15.md` and published on Zenodo.
**Date:** 2026-10-21

---

## 1. What was delivered

`CHRONICLES_TTS_PILOT_PRO_CH01.txt` — **166 segments**:

| Block | Segments | Speech | Pauses | Total |
|---|---|---|---|---|
| Front matter (`FM_###`) | 14 | 2.5 min | 0.2 min | 2.7 min |
| Prologue (`PRO_###`) | 59 | 9.3 min | 0.4 min | 9.7 min |
| Chapter 1 (`CH01_###`) | 93 | 10.9 min | 0.7 min | 11.6 min |
| **Pilot** | **166** | **22.8 min** | **1.3 min** | **24.0 min** |

Durations are estimates at ≈2.3 Russian words/second; they exist to show segment sizing, not to predict the render.

Voices used: `PROMPTER_OLD` 134, `INTEGRATOR` 22, `ARCHIVE` 9, `KEEPER` 1.
Delivery: `MEMOIR_RESTRAINED` 100, `IRONY_DRY` 34, `INSTITUTIONAL_NEUTRAL` 22, `ARCHIVE_FLAT` 9, `KEEPER_PRECISE` 1.
Rates: 0.92 ×20, 0.94 ×109, 0.96 ×36, 0.98 ×1 — every value within ±0.03 of its voice's base.
`PROCESS`: `ARCHIVE_RADIO` on the 9 `ARCHIVE` segments, `NONE` elsewhere. `MUSIC`: `NONE` throughout — there is no part boundary in the pilot.

## 2. Proof that the canon is intact

The markup was generated from the canonical file by line number, not retyped. The build then rebuilds the spoken word stream from the emitted segments and diffs it against the canonical word stream of lines 1–628:

```
canonical words 3140   segment words 3140
WORD STREAM IDENTICAL
```

The build fails and emits nothing if a single word is lost, added or reordered. It also checks that every spoken line is used exactly once and in order, that every long line split at a sentence boundary reproduces its original when the pieces are rejoined, that no line is both split and used whole, that every `VOICE`/`DELIVERY`/`PROCESS` is from the permitted set, that every `RATE` is within ±0.03 of base, and that segment numbers increase strictly inside each prefix. All checks pass. §21 is satisfied mechanically rather than by assertion.

**One formatting operation was applied, and it changes no word:** markdown carriers are removed so OmniVoice never pronounces a marker — `**` and `*` emphasis, backticks, the `>` of a blockquote, the `#` of a heading. The image line is dropped (it has no speech); its caption is kept.

## 3. Segment sizing

My first pass produced 297 segments with a median of 3.5 s — one segment per paragraph. That is exactly the mechanical splitting §6 forbids, and I corrected it: runs whose internal beat is ordinary (≤350 ms) and whose direction is identical were merged into one breath-unit of up to ~58 words. Every pause of 400 ms or more remained a segment boundary, because those are the ones the direction actually asks for.

Result: 53 segments in the 10–25 s target band, 37 at 5–10 s, 47 at 2–5 s, 28 under 2 s, 1 at 25.2 s, **none over 30 s**.

The 28 very short segments are not residue. They are the §10 pattern — a controlled pause, then a strong assertion standing alone: *«Нет.»*, *«И начались бои.»*, *«Не надо.»*, *«Проект проиграл.»*, *«Так возник AI-Colab.»*, *«Архивы портят композицию.»* — plus the headings and the Keeper's one live line. The book is written in short beats; the pilot keeps them where they carry weight and merges them where they do not.

## 4. Decisions taken, and why

**The Author's ruling on the AUTHOR voice is applied.** `AUTHOR` appears nowhere in the pilot. Where the Author is quoted or his instruction is dramatised — the four-line exchange in the Prologue (*«Ты разрабатываешь теорию»* …), *«По свидетельству Автора»*, *«Автор объявляет…»* — the current narrator carries it. §15 of the SPEC is therefore not exercised.

**СЛЕД ≠ ПАМЯТЬ, applied line by line.** `ARCHIVE` + `ARCHIVE_FLAT` + `ARCHIVE_RADIO` is used for the nine preserved primary quotations only:

| SEG | Document |
|---|---|
| PRO_031 | `Qwen 2.5-Coder 32B — ПОЛНАЯ КАПИТУЛЯЦИЯ!` — Claude's battle verdict |
| PRO_039 | «Батл должен быть прерван…» — DeepSeek's referee record |
| CH01_006 | «Оптимальная организация технологического процесса — наше всё!» — telegram record |
| CH01_014, CH01_016 | «Статус: всё в рамках ВПК-модели» / «без теории, без физики…» — the Qwen secretary's reports |
| CH01_028, CH01_030 | Claude's verdict and Qwen's opening line, first battle |
| CH01_045 | «Мы — соавторы одной мысли» |
| CH01_059 | «Батл должен быть прерван…» — second battle verdict |

**Three quoted sentences deliberately stay in the narrator's voice**, because they are not traces:

- Prologue, «Давайте теперь построим мультиагентную систему» — a phrase the narrator denies was ever the origin;
- Chapter 1, «впрочем, существуют некоторые ограничения» — a generic illustration of the hedge the project refused;
- Chapter 1, «Хранитель проиграл первый баттл» — the sentence the chapter forbids writing.

Giving any of these the archive voice would turn an invented example into a preserved record and invert the canon.

**The Keeper speaks once**, in the Prologue: *«— Ты уже упростил.»* — `KEEPER` / `KEEPER_PRECISE`, with 400 ms before and 450 ms after. The memorandum rule of §16 does not arise in the pilot; the Keeper's докладная is in Chapter 12.

**Irony is carried by pause, never by delivery colour.** 34 segments are `IRONY_DRY`; in every one the effect sits in the following pause (350–800 ms), not in the voice. *«Мисс Душнила уже кашлянула.»* is `IRONY_DRY` + 400 ms and nothing else.

**Pause convention — needs the curator's confirmation.** `PAUSE_BEFORE` is **0 on every segment**; the whole inter-segment gap is carried by `PAUSE_AFTER` of the preceding segment. This removes any chance of the assembler adding two numbers and double-counting a gap. If you prefer the gap split across both fields, say so and I will re-emit.

## 5. Open points for the curator and the Author

**O-1 — `FM_###` is a prefix the SPEC does not define.** §20 gives `PRO_`, `CH<n>_`, `FIN_`. The book's front matter — title, credits, the authorship note, «От Интегратора», «Справка Интегратора», the frontispiece caption — is not the Prologue, and labelling it `PRO_` would misname it in a production ledger. I used `FM_` and flag it rather than decide it.

**O-2 — who announces an ordinary chapter heading.** I gave headings and source notes to `INTEGRATOR` / `INSTITUTIONAL_NEUTRAL`, keeping `ARCHIVE` free so that the §12 line before Chapter 13 — *«Глава тринадцать. Повествование ведёт преемник»* — stands out as the only archive-voiced announcement in the book. If headings were also `ARCHIVE`, that seam would lose its marking.

**O-3 — the source notes.** «Источниковая помета» is editorial apparatus, not a primary document, so it is `INTEGRATOR` / `INSTITUTIONAL_NEUTRAL`, not `ARCHIVE`. §9 confirms they are to be voiced (it forbids music under them) but does not name the voice.

**O-4 — multi-line segments.** A merged segment holds the book's paragraphs on separate lines. Whether the batch converter joins them with a space or a newline is an engine-behaviour question and therefore yours; the SPEC's own logic says these internal beats are deliberately uncontrolled.

**O-5 — the pilot does not exercise two voices.** `MISS_DUSHNILA` and `PROMPTER_YOUNG` have no segments: Miss Dushnila is described three times in the pilot but never speaks, and the young Prompter starts at Chapter 13. The pilot therefore calibrates RATE, pause length and segment length for the narrator, the Integrator and the archive **only**. If the Author wants her voice and the dynasty seam calibrated before the remaining chapters are marked up, the cheapest addition is the `Стул` section plus the first page of Chapter 13 — that single stretch exercises Miss Dushnila, the seam pause, the archive announcement and the young Prompter at once. I have not marked it up, because §22 fixes the pilot at Prologue + Chapter 1.

## 6. Pronunciation watch list — engine side, not editorial

The text is frozen, so these are flagged, not fixed. In order of consequence:

**Critical.** Prologue, line 48: **Cloude**, **Qwan**, **DeseSook**. These are the misspelled names on the drawing and the whole point of the Prologue. If the engine or the text normaliser repairs them to Claude / Qwen / DeepSeek, the scene is destroyed. They must be rendered as written and should be checked first in the pilot render.

**Needs a decision.** `ZOV`, `ZOR` — letter-by-letter or as words; whichever the project already says aloud. `Глава 1.` — whether the engine reads «Глава один» or «Глава первая»; a text change is not available to me.

**Needs normalisation.** `ВПК/ТД` (slash), `HDD D:` (colon), `A.Tuin`, `GPT-4o`, `Qwen 2.5-Coder 32B`, `Qwen3-235B`, `AI-Colab`, `AI-Sociology`, `Git-dojo`, `prompt engineering`, and the English role titles in the credits block (`Human curator / publication authority`, `Chief Integrator / Methodologist`, `Manuscript Composer`). Dates — `29 июля 2025 года`, `26 августа`, `15 октября 2026 года` — should be checked once; they recur.

## 7. What I did not do

No voice was chosen, generated or described; the markup carries `VOICE_ID` only. No `instruct` text was written. No model parameter was touched. No script, batch file or audio step was produced. No line of the book was rewritten, shortened, added to or reordered — the word-stream check above is the evidence.

Awaiting the pilot render before marking up anything further, per §22.
