# CHRONICLES TTS — full-book markup

**Spec:** `CHRONICLES_TTS_EDITOR_SPEC_V1` + CORRECTIONS 01–03 + PILOT ACCEPTED
**Scope:** the whole book, lines 1–11538
**Source:** `Chronicles_of_Prompter_AUTHOR_FINAL_RU.md`
**Date:** 2026-10-22

---

## 1. What came out

| | |
|---|---|
| Voice blocks | 467 |
| Generation takes | 691 |
| Block length | median 46 s, max 237 s |
| Take length | median 31 s, max 51 s |
| Takes over the 50 s ceiling | 1, unavoidable (see §6) |
| Speech | 5 h 23 min |
| Pauses | 6 min |
| **Total** | **≈ 5 h 29 min** |

Voices: `PROMPTER_OLD` 212, `PROMPTER_YOUNG` 132, `ARCHIVE` 55, `INTEGRATOR` 44, `MISS_DUSHNILA` 22, `KEEPER` 2.

Front Matter and the Prologue are carried over **unchanged** from the accepted pilot. Everything from line 305 is new.

## 2. The cutting rule, calibrated rather than asserted

`***` could not be used mechanically as a scene break. Its density varies by a factor of ten across the book:

| | seconds per `***` segment |
|---|---|
| Prologue | 75 |
| ch. 1–3 | 65–95 |
| ch. 10–13 | 20–35 |
| ch. 14–15 | 16 |
| **ch. 16** | **7** |

In ch. 16 a `***` falls every three lines — there it is a rhythmic beat, not a scene change, and breaking on each would restore exactly the short-fragment policy CORRECTION 01 abolished.

So one rule applies everywhere: **mandatory boundaries always cut — voice change, live↔ARCHIVE, heading, source note, the dynasty seam — and between them a `***` opens a new block only once the accumulated block reaches 40 s.** Nothing is ever cut anywhere other than at a `***` or a mandatory boundary.

The 40 s threshold is not a guess: it is the value at which the rule reproduces the Prologue you already approved by ear. Run on the Prologue the same rule yields 14 blocks against my hand-made 17 — the three it merges are all short scenes adjacent to an archive insert. The Prologue is accepted, so it stays as accepted; the rule governs only from line 305.

## 3. Who speaks

**The dynasty seam is line 7017**, the first line of ch. 13: *«Промптер уже ушёл. Это важно.»* — the narrator speaks of the Old Prompter in the third person and recaps what he did, including the `Стул` scene. So:

- Prologue → `Стул` (lines 40–7016): `PROMPTER_OLD`
- ch. 13 → ch. 16 (7017–11497): `PROMPTER_YOUNG`
- «Документальный шлейф» and «На выходе. От Интегратора» (11498–): `INTEGRATOR`
- all 17 end-of-chapter source notes: `INTEGRATOR` / `SOURCE_NOTE_RAPID` / 1.50

`Стул` stays with the Old Prompter: it precedes ch. 13 and ch. 13 describes its events as something he did.

**Miss Dushnila speaks 22 times** — from «— Только не пишите, что в „Коде 42“ уже всё было» (ch. 9) through the `Стул` scene, ch. 14, ch. 15 and the last exchange of the book, «— Только источник подпишите». **The Keeper speaks twice**: «— Ты уже упростил» in the Prologue and «— Нас четверо, — сказал Хранитель» opening ch. 9.

The Author still has no voice. His lines — «— Трое, Qwen. Нас трое», «— Ты — это он, только позже», «— Продолжай „Хроники“», «— Автор — ты» — are read by whichever Prompter is narrating.

## 4. СЛЕД ≠ ПАМЯТЬ, applied to 144 quotations

Every blockquote in the book was classified individually. **56 are `ARCHIVE`**, 88 stay with the living voice.

`ARCHIVE` requires the introducer to assert that the text *existed as a record*: «записал», «документ говорит», «в сохранившейся формулировке», «отчитывается», «В Хартии», «В контракте», «Наставник написал», «По финальному отчёту», «Тест A.1 дал». Everything else stays live — invented examples, contrast pairs («Не: … А: …»), counterfactuals, labels, and documents quoted for what they did *not* say («Никто не прислал приказ:», «System prompt не говорил:»).

**The default in a doubtful case is the living voice,** because the archive voice is a claim that a trace exists. Promoting a paraphrase into a record is a worse error in a documentary book than reading a record in the narrator's voice.

**15 borderline calls are listed for you** in `quotes.py` under `FLAGGED`. The one worth your eye: ch. 16, *«You are a writer, not … a scientific co-author»*, introduced as having surfaced *«где-то внутри моей профессиональной памяти»*. The contract is a real document, but the introducer names **memory**, not a trace — so the canon itself requires the living voice there. Two others, «Grok написал: — Следующий шаг: Doctor» (ch. 11 and ch. 14), assert a record but are typeset as dialogue; I followed the introducer, not the typography.

**One case has no voice at all.** Ch. 16: *«Автор спросил: — Ты ожил?» / «Главред ответил: — Жив. Вернулся туда, где остановились.»* The Chief Editor — Claude — speaks live, and the SPEC has no `VOICE_ID` for him. I read it as `ARCHIVE`, since it is a preserved exchange, but if you want Claude audible as himself the roster needs a voice he does not currently have.

## 5. The gate

```
CANON = AUDIO TEXT + APPROVED CONTRACTION REGISTRY + DECLARED AUTHOR CORRECTIONS

canonical spoken lines  : 5104
spoken in the audio     : 5096
omitted by contraction  : 8   (CONTRACTION_001)
declared corrections    : 3, all applied
undeclared new prose    : none
canonical words 34680   block words 34680   WORD STREAM IDENTICAL
```

The three corrections are the Author's, and nothing else differs from the published book:

```
'ИИ-коллаборации' -> 'AI Collaboration'   x3   (lines 3, 5, 322)
```

Line 322 now reads «состав AI Collaboration проекта ВПК», per your ruling. «человеческо-ИИ коллаборации» at lines 12 and 20 is untouched. The eight omitted lines are the duplicated ch. 15 source note, and they are the only omission in the book. U+0301 is invisible to the gate, so a stress mark can never enter as an undeclared correction.

## 6. Generation takes

691 takes, median 31 s, split only at paragraph boundaries, balanced so no take is needlessly long or stubby.

**Two paragraphs exceeded 50 s with no paragraph boundary inside them** — a ch. 14 source note (51 s) and a ch. 16 source note (57 s). I split those at their own sentence ends, which is the only natural boundary left inside a paragraph, and both are reported by the build rather than cut silently.

**One take remains at 51 s and cannot be helped**: ch. 5's source note contains a single 543-character sentence built on semicolons, with no internal boundary of any kind. §2 permits this — the ceiling applies "when a natural earlier boundary exists", and here none does.

## 7. Pronunciation jobs — 667

`CHRONICLES_TTS_PRONUNCIATION_JOBS.txt` covers **510 unique expressions across 1,481 occurrences**, as one clip per expression-and-voice, so the §6 reuse rule is already applied and no job duplicates another.

By kind: 222 English phrases, 216 Latin names, 105 mixed identifiers, 74 acronyms, 36 model IDs, 14 all-caps words. Sorted by frequency, so the top of the file is where rendering pays off first: `Grok` 102, `DeepSeek` 55, `prompt` 45, `AI-Colab` 41, `Doctor` 41, `SPEC` 38, `ZOR` 37, `Claude` 36, `Qwen` 31, `ZOV` 27.

`Cloude`, `Qwan` and `DeseSook` each carry `@NOTE КАНОНИЧЕСКАЯ ОПЕЧАТКА. Не исправлять` and are prepared as `LANG RU`, the reading you accepted.

`CAPS_WORD` is still a proposed `@KIND`: 14 expressions are ordinary Russian words in capitals, such as `ПОЛНАЯ КАПИТУЛЯЦИЯ`, where the risk is the engine spelling them out letter by letter rather than mispronouncing them. None of the five kinds in §4 fits.

## 8. Stress overrides — four

Deliberately four, not four hundred. `начал` (33), `потом` (112), `правило` (16), `уже` (209). For each I checked the whole book for the opposite reading and it does not occur, so a word-level override is safe everywhere.

**`стоит` is deliberately excluded** although it occurs 13 times: the book genuinely uses both stresses — «Один участник стои́т у доски» against «мысль ещё сто́ит переделать» — so a word-level override would break one of them. Per-occurrence scoping is exactly the polishing the accepted decision says not to spend effort on; replace an individual spot by ear if it distracts.

## 9. Still open for you

- **`STUL_` and `TRAIL_`** are prefixes the SPEC does not define, for `Стул` and «Документальный шлейф». `FM_`, `PRO_`, `CH01_`–`CH16_` and `FIN_` are as specified.
- **`ARCHIVE` 1.28 and `KEEPER` 1.30, `MISS_DUSHNILA` 1.28** — provisional, chosen to keep the relation these voices had to the narrator before the rates rose. None has been heard yet.
- **A second contraction candidate**: the Author's message «Ой, Док, моя ошибка…» is read twice in full — ch. 13's source note (line 7779) and ch. 15's narrative (line 8891). The third occurrence is already removed by `CONTRACTION_001`. These two sit in different functions — apparatus and narrative — so I flag rather than propose. No other verbatim repetition exists in the book: the shingle sweep over all 135 substantial paragraphs found only the ch. 13/15 pair.
- **Dialogue scenes produce short blocks** by necessity. A speaker change is a mandatory boundary, so the exchange in ch. 15 («— Вы же теперь психолог?» / «— Формально нет.» / «— Философ?» …) is seven blocks of two or three words. That is what alternating voices costs; the alternative is letting the narrator read both sides, which would lose Miss Dushnila exactly where she is sharpest.

No voice was chosen or described, no `instruct` written, no model parameter touched, no script or audio step produced. Beyond the three words you ordered and the eight lines you approved for omission, not one word of the book was changed.
