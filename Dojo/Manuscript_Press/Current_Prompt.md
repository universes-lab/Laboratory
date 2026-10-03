# CURRENT PROMPT — MANUSCRIPT_PRESS

PROJECT: `MANUSCRIPT_PRESS`

ROOT: `E:\Gemini\Dojo\Manuscript_Press`

ACTIVE_MODE: `IMPLEMENTER`

ACTIVE_OPERATION: `LAUNCHERS_AND_MARKER_RANGE`

---

## CURRENT TASK

Выполнить текущий физический:

`STEP.md — MANUSCRIPT_PRESS / LAUNCHERS + MARKER RANGE`

Version: `2.0`

Точно в его установленном scope.

Текущая операция включает:

- launcher cleanup;
- добавление `--end-marker`;
- обязательный physical readback;
- `py_compile`;
- ровно один разрешённый контрольный inference на диапазоне `MP:0001 → MP:0001`.

---

## CURRENT AUTHORITY

Техническая authority текущей операции:

`SPEC.md v3.3`

и активный физический:

`STEP.md`

`SPEC_v3.2.2.md` является архивной target architecture и не является текущей execution authority.

STEP не разрешает hardening или full article run.

---

## EXECUTION DISCIPLINE

Выполняй STEP последовательно.

Не додумывай отсутствующие внешние решения.

Если для корректного продолжения не хватает факта, параметра, пути, значения либо STEP содержит противоречие, которое нельзя однозначно разрешить из физических authority documents:

`STOP → REPORT KNOWN FACTS → ASK THE SMALLEST NECESSARY QUESTION → WAIT`

Не заменяй отсутствующее решение наиболее вероятной гипотезой.

Обычные инженерные средства внутри однозначно разрешённого действия выбирай самостоятельно.

---

## INTERMEDIATE REPORTING

После каждого завершённого этапа STEP дай короткий factual report:

```text
STEP POSITION: <completed position>
ACTION: <what was physically done>
RESULT: PASS / FAIL / BLOCKED
EVIDENCE: <observable verification>
NEXT: <next action already authorized by STEP>
```

Промежуточный отчёт не создаёт SUBSTEP и не изменяет authority.

Если NEXT уже однозначно разрешён STEP — продолжай.

Если требуется новое решение или изменение route — STOP и спроси.

---

## WORK PERMIT

Разрешено только в пределах STEP:

- изменить `manuscript_press.bat`;
- изменить `src\production_runner.py`;
- создать `resume_manuscript_press.bat`;
- архивировать `run_manuscript_press.bat` в указанное STEP место;
- выполнить обязательный physical readback;
- выполнить `py_compile`;
- выполнить ровно один контрольный inference, заданный STEP;
- прочитать созданные evidence-файлы и metadata, необходимые для отчёта.

---

## FORBIDDEN

Запрещено:

- full article run;
- второй контрольный inference при ошибке первого;
- hardening;
- 10B model;
- изменение SPEC;
- изменение Input;
- изменение `Gemma.md`;
- изменение `writer_config.yaml`;
- изменение `loader.py`;
- изменение `parser/*`;
- самостоятельное изменение route;
- дополнительные CLI options вне STEP;
- следующий STEP без внешнего решения.

---

## FAILURE

Не выполнять silent recovery.

При неожиданной ошибке:

`PRESERVE EVIDENCE → REPORT → STOP`

Исправлять ошибку самостоятельно можно только если исправление однозначно является обычным инженерным средством уже разрешённого STEP и не меняет route, dependencies, requirements или scope.

При сомнении — спросить.

---

## COMPLETION

После полного выполнения STEP:

`VERIFY → FINAL REPORT → STOP → WAIT_FOR_SENSEI`

Успех этого STEP не разрешает full article run и не открывает hardening.

FINAL AUTHORITY: `Author / Shogun`

END OF CURRENT PROMPT