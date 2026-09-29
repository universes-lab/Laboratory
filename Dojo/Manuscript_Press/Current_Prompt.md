# CURRENT PROMPT — MANUSCRIPT_PRESS

PROJECT: `MANUSCRIPT_PRESS`

ROOT: `E:\Gemini\Dojo\Manuscript_Press`

ACTIVE_MODE: `IMPLEMENTER`

ACTIVE_OPERATION: `MATERIALIZE_CLEAN_ROOT`

---

## CURRENT TASK

Выполнить текущий физический:

`STEP.md — MANUSCRIPT_PRESS / RECONSTRUCT CLEAN ROOT`

точно в его границах.

Цель операции:

восстановить чистый рабочий `MANUSCRIPT_PRESS` на новом диске после потери старого `D:`.

Это:

`RECONSTRUCTION ONLY`

Это НЕ:

- production inference;
- hardening;
- full production run;
- продолжение старого run;
- реализация полного SPEC v3.2.2.

---

## AUTHORITY

Текущая техническая authority:

```text
SPEC.md
→ IMPLEMENTATION_MAP_APPROVED.yaml
→ IMPLEMENTATION_PLAN.md
→ DEEPSEEK_STEP_HANDOFF.md
→ current physical STEP.md
```

`STEP.md` — непосредственная техническая инструкция Coding Sensei DeepSeek для этой операции.

Не реконструируй задание из старых файлов, output, run history или предыдущих сессий.

Не создавай SUBSTEP или собственный workflow.

---

## WORK PERMIT

Разрешено всё, что прямо необходимо для выполнения текущего STEP, включая:

- материализацию GitHub snapshot в новый ROOT;
- создание и перемещение файлов внутри ROOT согласно STEP;
- изменение файлов, явно разрешённых STEP;
- архивирование файлов, явно перечисленных STEP;
- проверку фактического дерева проекта;
- `py_compile`;
- `--preflight-only`;
- необходимые read-only проверки Evidence.

Разрешён внешний источник реконструкции:

`https://github.com/universes-lab/Laboratory/tree/main/Dojo/Manuscript_Press`

Разрешена read-only проверка существования указанного STEP пути модели:

`E:\Gemini\models\Gemma-The-Writer-9B-D_AU-q5_k_m.gguf`

---

## FORBIDDEN

Без отдельного нового разрешения запрещено:

- model inference;
- обычный запуск `python -m src.production_runner` без `--preflight-only`;
- full production run;
- использование alternative GGUF;
- GPU tuning;
- изменение `src/loader.py`;
- перенос или исследование AI-Colab loader / `app.py`;
- изменение production inputs;
- изменение `Gemma.md`;
- самостоятельное изменение технического route;
- самостоятельная реализация hardening;
- возобновление старого `MP:0170` run;
- Git operations сверх действий, прямо разрешённых STEP;
- переход к следующему STEP.

---

## HISTORICAL STATE

Старые:

- `Current_Prompt.md`;
- `STEP.md`;
- `GEMINI.md`;
- launchers;
- Output/run artifacts

из GitHub snapshot являются материалом реконструкции, а не автоматически действующей authority.

Текущий `Current_Prompt.md` и текущий reconstruction `STEP.md` имеют приоритет как активный operational frame.

Не путай историческое состояние проекта с текущим заданием.

---

## EVIDENCE

Не сообщай ожидаемое состояние как фактическое.

После изменений проверяй физический результат.

Особенно подтвердить Evidence для:

- созданного ROOT;
- установленных/архивированных файлов;
- нового model path;
- clean launcher;
- отсутствия старых `D:` operational paths;
- отсутствия default `--start-marker`;
- `py_compile`;
- фактического `--preflight-only`;
- фактического exit code;
- marker count;
- validator result;
- отсутствия model load / inference.

Если факт не проверен:

`EVIDENCE: INCOMPLETE`

---

## STOP

Немедленно STOP, если:

- возникает условие STOP из текущего STEP;
- preflight FAIL;
- возникает model load или inference;
- требуется изменить technical route;
- требуется действие вне разрешённого STEP;
- обнаруживается существенное противоречие между authority documents.

При STOP:

```text
PRESERVE STATE
→ REPORT FACTS + EVIDENCE
→ QUERY SENSEI
```

Не придумывай обходной путь самостоятельно.

---

## COMPLETION

После выполнения текущего STEP:

```text
VERIFY
→ REPORT USING STEP REPORT FORMAT
→ STOP
→ WAIT
```

Не начинай hardening.

Не запускай production inference.

Не выбирай следующий STEP.

FINAL AUTHORITY: `Author / Shogun`

END OF CURRENT PROMPT