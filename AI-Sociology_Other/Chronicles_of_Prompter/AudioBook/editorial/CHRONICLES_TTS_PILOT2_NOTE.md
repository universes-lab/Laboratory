# CHRONICLES_TTS_PILOT 2 — editorial note

**Spec:** `CHRONICLES_TTS_EDITOR_SPEC_V1` + `CORRECTION 01`
**Scope:** Front Matter + Prologue (per Correction §9)
**Source:** `Chronicles_of_Prompter_AUTHOR_FINAL_RU.md`, canonical Russian original
**Date:** 2026-10-22

---

## 1. The new cut

The short-segment policy is withdrawn. The same text is now **21 voice blocks** instead of 166 segments.

| | Pilot 1 | Pilot 2 |
|---|---|---|
| Units over Front Matter + Prologue | 73 | 21 |
| Median unit | 5 s | 41 s |
| Longest unit | 25 s | 83 s |
| Montage pauses | 1.3 min | 0.3 min |

Median 41 s, longest 83 s (`PRO_002`, the whole first scene of the Prologue in one take). Estimated speech 11.8 min.

The build now **refuses to emit an unjustified cut**: for every pair of adjacent blocks it checks that there is a reason from Correction §2 — a change of speaker, a live↔ARCHIVE crossing, a structural section, or a scene change. If two neighbouring blocks share a voice and a process with no such reason between them, the build fails. Irony, a short strong sentence and a pre-assertion pause no longer cut anything; they sit inside a block and are carried by the book's own punctuation, which is now preserved in the text handed to OmniVoice as paragraphs separated by a blank line.

## 2. Every cut in the pilot, and its reason

| Boundary | Reason |
|---|---|
| FM_001 → FM_002 → FM_003 → FM_004 | structural sections of the front matter: title page, the Integrator's signed note, the Справка, the frontispiece caption |
| FM_004 → PRO_001 | chapter heading |
| PRO_001 → PRO_002 | speaker change, INTEGRATOR → PROMPTER_OLD |
| PRO_002/003/007/011/012/016 ends | scene change (`***`) |
| PRO_004 → PRO_005 → PRO_006 | live ↔ ARCHIVE, Claude's battle verdict |
| PRO_008 → PRO_009 → PRO_010 | live ↔ ARCHIVE, DeepSeek's referee verdict |
| PRO_013 → PRO_014 → PRO_015 | speaker change, the Keeper's one live line |
| PRO_016 → PRO_017 | structural: source note, and a speaker change |

Nine scenes of the Prologue, two archive inserts, one live line from the Keeper. Nothing else is cut.

`DELIVERY` no longer splits anything. The long narrator blocks are `MEMOIR_RESTRAINED` throughout, and the dry irony lives inside them — `PRO_002` alone contains *«Мисс Душнила уже кашлянула»*, *«Нет.»* and *«Пока — просто картинка»* in one continuous take. `RATE` is now one value per block, every voice at its base: 0.94 / 0.96 / 0.98. No local variation at all.

## 3. The Author's correction — applied, with two findings

**In scope: 2 occurrences, both changed.**

| Line | Before | After |
|---|---|---|
| 3 | Документальная книга **ИИ-коллаборации** | Документальная книга **AI Collaboration** |
| 5 | …роль ChatGPT внутри **ИИ-коллаборации** | …роль ChatGPT внутри **AI Collaboration** |

The build diffs the block text against the published canon and reports every difference. It reports exactly these two and nothing else.

**Finding 1 — the correction harmonises Russian with the already-published English.** The English edition reads, at the same two lines:

> *Documentary book of the **AI Collaboration***
> …a dynastic ChatGPT role within the **AI Collaboration**

So this is not a new coinage; it aligns RU with EN. The Dutch edition, however, reads *AI-collaboratie* in both places — Dutch, not the English name. If the term is now a proper name, NL diverges and the Integrator may want it aligned too.

**Finding 2 — one more occurrence exists, and it may not be the same thing.** Line 322, in Chapter 1: *«За ним идёт состав ИИ-коллаборации проекта ВПК.»* It is outside this pilot's scope, so I have not touched it. But the English edition renders that line as *"the VPK project's AI collaboration"* — lower case, as a common noun — while using capitalised *AI Collaboration* on the title page. The English edition therefore already distinguishes the proper name from the common noun. Whether the Russian line 322 is the name or the common noun is the Author's call, and I will apply whichever he states when Chapter 1 is re-marked.

**Two look-alikes deliberately left alone.** Lines 12 and 20 contain *«человеческо-ИИ коллаборации»* — *human–AI collaboration*. Substituting there would produce *«длительной человеческо-AI Collaboration»*, which is not Russian. These are a different construction, not the term the correction names. If the Author wants them changed as well, the phrase needs his own wording; I will not invent one.

**Consequence that needs a decision.** The book is published on Zenodo as v1.0 with *ИИ-коллаборации*. The audiobook now says *AI Collaboration*. Either the book file is corrected and re-versioned so text and audio agree, or the divergence is accepted and recorded. That is a publication decision for the Author and the Integrator, not a production one — I have changed nothing in the canonical file.

## 4. `[[EN]]` marking — seven marks

Deliberately conservative, per Correction §5 (do not auto-mark every obvious name):

| Where | Marked |
|---|---|
| lines 3, 5 | `AI Collaboration` — the Author's new term, English by construction |
| line 6 | `Human curator / publication authority` |
| lines 8, 24 | `Chief Integrator / Methodologist` — credits line and signature |
| line 22 | `prompt engineering` |
| line 48 | `Specialized AI` — the label on the drawing |

Markers are service markup: the build strips them before the word-stream check, so they can add or remove nothing.

**Left unmarked and deferred to the pilot render**, as §5 directs: `Claude`, `Grok`, `Qwen`, `DeepSeek`, `ChatGPT`, `A.Tuin`, `ZOV`, `ZOR`, `AI-Sociology`, `AI-Colab`, `ВПК/ТД`, `HDD D:`, `GPT-4o`, `Qwen 2.5-Coder 32B`, `Qwen3-235B`, `web-коллаборация`.

## 5. The one listening test that matters most

Prologue, inside `PRO_002`: **Cloude**, **Qwan**, **DeseSook**. These are the misspelled names on the drawing and the entire point of the Prologue. I left them unmarked, because `[[EN]]` could push the engine toward repairing them into Claude / Qwen / DeepSeek — which would destroy the scene — whereas a Russian reading garbles them in a way that is at least recognisably wrong.

This is a decision I should not take silently, so here is the A/B: render `PRO_002` once as delivered, and once with the three names wrapped in `[[EN]]`. Whichever keeps them audibly wrong-but-related to the correct names is the right answer, and it then applies to the rest of the book. Everything else in the pilot can be judged on one pass; this needs two.

## 6. One new field, flagged not decided

Each block carries `@LANG RU`. Correction §2 makes a language switch a block boundary and the batch format has `language_id`, so the block should state its generation language. The SPEC does not define the field. If you would rather derive the language from `[[EN]]` alone, say so and I will drop it.

The `FM_###` prefix for the front matter is unchanged from Pilot 1 and still awaits confirmation: §20 defines `PRO_`, `CH<n>_` and `FIN_`, and the front matter is none of them.

## 7. Unchanged

`PAUSE_BEFORE` remains 0 on every block; the whole montage gap is carried by `PAUSE_AFTER` of the preceding block, so no gap can be counted twice.

Canon rules held: СЛЕД ≠ ПАМЯТЬ (the two preserved verdicts are the only `ARCHIVE` blocks, and the Prologue's *«Давайте теперь построим мультиагентную систему»* stays in the narrator's voice because it is a phrase the book denies, not a record); documents to `ARCHIVE`; live scenes to live voices; the Integrator institutionally calm; no `AUTHOR` voice anywhere, per the Author's earlier ruling.

No voice was chosen or described, no `instruct` written, no model parameter touched, no script or audio step produced. Beyond the two words the Author ordered, not one word of the book was changed — the word-stream diff is the evidence.

Awaiting the render of these 21 blocks before anything further is marked up.
