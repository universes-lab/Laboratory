GROK — HARDENING ROUTE FINAL CLOSURE

Твои инженерные уточнения приняты.

Открытый вопрос `В§5` проверен физически.

## В§5 PROVENANCE

`FINAL.manuscript.md`:

- 5 occurrences;
- все находятся в одном generated fragment в начале §5;
- символ перед `§` = Cyrillic capital VE `U+0412`.

Production `Input/SOURCE_MANUSCRIPT.md`:

- `В§5` occurrences = 0.

Production `Input/PROMPT_MAP.yaml`:

- `В§5` occurrences = 0.

Следовательно текущая классификация:

`GENERATED_OUTPUT_CORRUPTION`

Не inherited SOURCE.
Не PROMPT_MAP leak.

Последняя проверка при реализации hardening:
если `production_runner.py` сохраняет Python Unicode через обычный UTF-8 write без промежуточного transcoding, классификация окончательно остаётся Gemma/generated-output.

Это не отдельный runner fix, кроме общего output validation/evidence discipline.

---

## HARDENING SCOPE — ACCEPTED

### 1. PRE-MARKER PREFIX

ACCEPTED.

SOURCE prefix:

`BOF → first production marker`

сохраняется byte-for-byte как passthrough.

Не отправляется Gemma.

---

### 2. STRUCTURAL HEADING GLUE

ACCEPTED.

При assembly exact SOURCE ATX heading должен иметь корректную line boundary.

Минимальное правило:

если непосредственно предшествующий собранный fragment не заканчивается newline, перед structural heading вставляется ровно один required newline.

Не нормализовать остальной manuscript whitespace без отдельной причины.

---

### 3. CONTROL / META LEAK GUARD

Одна коррекция:

**FAIL, not silent strip.**

Если generated candidate содержит запрещённый runtime/control token, которого нет в CURRENT_SOURCE, marker должен быть забракован.

Минимальный forbidden class:

- payload grammar `BEGIN_*` / `END_*`;
- `END_LOCAL_TRANSFORMATION`;
- `OPEN SOURCE DECISION`;
- explicit generation placeholders such as `[To be specified ...]`;
- known model-meta formulation such as `implied but not explicitly stated in the SOURCE`.

Rule:

`forbidden meta/control output`
→ preserve raw candidate as evidence
→ marker FAIL
→ STOP
→ no FINAL manuscript.

Причина:

silent strip может удалить симптом, оставив рядом substantive drift.

Runner не редактирует модельный candidate.

---

### 4. NEW MARKDOWN TABLE GUARD

Твоя узкая формулировка принята.

Если:

`CURRENT_SOURCE contains no markdown table`

AND

`generated candidate introduces markdown table syntax`

то:

`STRUCTURED_MATERIAL_INVENTED`
→ marker FAIL
→ STOP.

Не строить универсальный semantic structured-material detector.

Если SOURCE уже содержит таблицу, этот простой guard не решает вопрос её смысловой верности; это Editor/Prompter review.

---

## NOT IN HARDENING CODE

Подтверждаю:

- не менять `Gemma.md`;
- не менять `PROMPT_MAP.yaml`;
- не менять `SOURCE_MANUSCRIPT.md`;
- не возвращать freeze / commit / ACCEPT machinery;
- не redesign Manuscript_Press;
- не пытаться кодом ловить все виды semantic invention.

---

## REGRESSION ORDER

Принято:

1. prefix passthrough;
2. пять известных heading-glue sites;
3. protected-slot marker class;
4. control-leak candidate;
5. §5.3-class marker, где появился invented table;
6. context-window / STOP contract остаётся действующим.

Сначала targeted regression.

Не запускать новый 375-marker production pass автоматически.

Решение о следующем полном прогоне принимается после Editor defect report + successful targeted regression.

---

Верни только:

MANUSCRIPT_PRESS_HARDENING_ROUTE_LOCK:
  STATUS: LOCKED / RETURN
  PREFIX_POLICY: <exact>
  HEADING_GLUE_POLICY: <exact>
  CONTROL_LEAK_POLICY: FAIL
  TABLE_GUARD_POLICY: <exact>
  VSECTION5_CLASSIFICATION: <exact>
  TARGETED_REGRESSION: <exact set>
  FULL_RERUN_POLICY: <exact>
  DEEPSEEK_MAY_WRITE_HARDENING_STEP: yes/no
  NEXT_OWNER: <one role>

No code.
No new SPEC.
STOP.