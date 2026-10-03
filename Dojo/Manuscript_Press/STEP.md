# STEP.md — MANUSCRIPT_PRESS / HARDENING OUTPUT SANITATION

```yaml
IDENTITY:
  Project: MANUSCRIPT_PRESS
  Phase: POST_RECONSTRUCT
  Step: HARDENING_OUTPUT_SANITATION
  Version: 1.0
  Status: READY_FOR_SAMURAI
  Date: 2026-10-01
  Step Type: EDIT

  Technical Authority:
    - SPEC v3.3 (current execution contract)
    - SPEC_v3.2.2 (target, archived, not implemented)
    - Shogun decision 2026-10-01: four hardening items proven by prior FINAL

  Scope: hardening only. Not production run.
```

---

## OBJECTIVE

Внести в `src/production_runner.py` четыре обязательные правки:

1. SOURCE prefix до первого production marker сохраняется в FINAL как есть.
2. ATX heading возвращается на свою позицию в сборке без склейки с соседним абзацем.
3. В выход не попадают служебные строки: `END_LOCAL_TRANSFORMATION`, `OPEN SOURCE DECISION`, placeholder-классы, editorial meta.
4. Кандидат с новой таблицей или structured block, которых нет в SOURCE этого маркера, не принимается: STOP, без частичного FINAL.

---

## ALLOWED WORKING FILES

**Изменить:**

```
E:\Gemini\dojo\Manuscript_Press\src\production_runner.py
```

**Не трогать:**

```
SPEC.md
SPEC_v3.2.2.md
Input\SOURCE_MANUSCRIPT.md
Input\PROMPT_MAP.yaml
Gemma.md
config\writer_config.yaml
src\loader.py
src\parser\*
manuscript_press.bat
resume_manuscript_press.bat
```

---

## DO_NOT

- Не активировать 10B модель.
- Не запускать full article run (375 маркеров).
- Не менять preflight, парсеры, loader, restore, cache.
- Не менять существующую FINAL assembly логику за пределами четырёх правок ниже.
- Не добавлять новых CLI-аргументов.
- Не менять `run.log` / `summary.json` контракт.
- Не делать второй прогон при ошибке.

---

## EDIT 1 — SOURCE prefix в FINAL

**Где:** после успешного завершения маркер-цикла, перед записью `Output/FINAL.manuscript.md`.

**Что:**

До первого маркера в `slotted_source` может быть текст (SOURCE prefix). Он должен попасть в начало `FINAL.manuscript.md` как есть.

**Как:**

1. Найти позицию первого маркера в `slotted_source`:

```python
first_marker = marker_graph[0]
first_marker_line = f"<!-- {first_marker.marker_id} -->"
first_pos = slotted_source.find(first_marker_line)
if first_pos < 0:
    m = re.search(rf"<!--\s*{re.escape(first_marker.marker_id)}\s*-->", slotted_source)
    if not m:
        raise ValueError("First marker not found in slotted_source")
    first_pos = m.start()
prefix = slotted_source[:first_pos]
```

2. При сборке FINAL — поставить `prefix` перед `"".join(rebuilt_intervals)`:

```python
final_text = prefix + "".join(rebuilt_intervals)
```

3. Если prefix пустой — ничего не меняется.

**Инвариант:** при отсутствии prefix поведение не отличается от текущего.

---

## EDIT 2 — ATX heading на своей позиции без склейки

**Где:** функция `rebuild_interval`.

**Проблема:** если предыдущий restored chunk не заканчивается `\n`, а следующий сегмент — `STRUCTURAL_HEADING`, heading склеивается с предыдущим текстом.

**Как:**

Перед добавлением `STRUCTURAL_HEADING` убедиться, что предыдущий накопленный фрагмент заканчивается символом новой строки. Если нет — добавить `\n`.

```python
def rebuild_interval(structure_map, restored_rewritable):
    parts = []
    used = False
    for seg in structure_map:
        if seg["type"] == "STRUCTURAL_HEADING":
            if parts and not parts[-1].endswith("\n"):
                parts.append("\n")
            parts.append(seg["text"])
        else:
            if not used:
                parts.append(restored_rewritable)
                used = True
    if not used:
        parts.append(restored_rewritable)
    return "".join(parts)
```

**Инвариант:** если `restored_rewritable` уже заканчивается `\n` — лишний перевод строки не добавляется.

---

## EDIT 3 — Output sanitation

**Где:** после получения `generated` и до вызова `restore_protected` и `rebuild_interval`.

**Что запрещено оставлять в тексте, уходящем в FINAL:**

- строки, содержащие `END_LOCAL_TRANSFORMATION`
- строки, содержащие `BEGIN_*` / `END_*` runtime-грамматики (`BEGIN_CURRENT_SOURCE`, `END_CURRENT_SOURCE`, `BEGIN_CONTINUITY_CACHE`, `END_CONTINUITY_CACHE`, `BEGIN_LONG_RANGE_FRAME`, `END_LONG_RANGE_FRAME`, `BEGIN_GEMMA_KERNEL`, `END_GEMMA_KERNEL`, `BEGIN_RUNTIME_CONTRACT_OVERRIDE`, `END_RUNTIME_CONTRACT_OVERRIDE`)
- фразы класса `OPEN SOURCE DECISION`
- placeholder-классы вида `[To be specified based on SOURCE analysis]`, `[PENDING_INFERENCE]`, `[TBD]`, `[placeholder]` (регистронезависимо)
- editorial meta: строки, начинающиеся с `Note:`, `Editor's note:`, `Commentary:`, `Analysis:`, `Excerpt:`, `Comment:`, `Commentary on`

**Как:**

Функция проверки:

```python
FORBIDDEN_PATTERNS = [
    re.compile(r"END_LOCAL_TRANSFORMATION"),
    re.compile(r"\bBEGIN_[A-Z_]+\b"),
    re.compile(r"\bEND_[A-Z_]+\b"),
    re.compile(r"OPEN SOURCE DECISION"),
    re.compile(r"\[To be specified based on SOURCE analysis\]", re.IGNORECASE),
    re.compile(r"\[PENDING_INFERENCE\]", re.IGNORECASE),
    re.compile(r"\[TBD\]", re.IGNORECASE),
    re.compile(r"\[placeholder\]", re.IGNORECASE),
    re.compile(r"^\s*Note:", re.MULTILINE),
    re.compile(r"^\s*Editor'?s note:", re.MULTILINE | re.IGNORECASE),
    re.compile(r"^\s*Commentary:", re.MULTILINE | re.IGNORECASE),
    re.compile(r"^\s*Analysis:", re.MULTILINE),
    re.compile(r"^\s*Excerpt:", re.MULTILINE),
    re.compile(r"^\s*Comment:", re.MULTILINE),
    re.compile(r"^\s*Commentary on", re.MULTILINE | re.IGNORECASE),
]

def enforce_output_sanitation(generated: str, marker_id: str) -> None:
    for pat in FORBIDDEN_PATTERNS:
        m = pat.search(generated)
        if m:
            snippet = generated[max(0, m.start() - 40): m.end() + 40].replace("\n", "\\n")
            raise ValueError(
                f"OUTPUT_SANITATION_VIOLATION: {marker_id} matched {pat.pattern!r} "
                f"near: {snippet!r}"
            )
```

Вызвать `enforce_output_sanitation(generated, marker.marker_id)` **до** `normalize_slots`.

**Поведение:** любое совпадение → `ValueError` → STOP → FINAL не пишется.

---

## EDIT 4 — Reject new tables / structured blocks not in SOURCE

**Где:** после `enforce_output_sanitation`, до `normalize_slots`.

**Что:** если `current_source` (текст маркера до inference) **не содержит** markdown-таблицу (строку, содержащую `|` в начале или внутри строки, минимум два `|` в одной строке), а `generated` **содержит** такую таблицу — отклонить.

**Как:**

```python
TABLE_LINE_RE = re.compile(r"^\s*\|.*\|.*\|\s*$", re.MULTILINE)

def enforce_no_new_tables(current_source: str, generated: str, marker_id: str) -> None:
    source_has_table = bool(TABLE_LINE_RE.search(current_source))
    output_has_table = bool(TABLE_LINE_RE.search(generated))
    if not source_has_table and output_has_table:
        raise ValueError(
            f"OUTPUT_SANITATION_VIOLATION: {marker_id} introduced new table not present in SOURCE"
        )
```

Вызвать `enforce_no_new_tables(current_source, generated, marker.marker_id)` сразу после `enforce_output_sanitation`.

**Поведение:** новое появление таблицы → STOP, FINAL не пишется.

---

## MANDATORY_PHYSICAL_READBACK

После edit — прочитать с диска и привести в отчёте фактические строки (номер + текст) для:

```powershell
Get-Content E:\Gemini\dojo\Manuscript_Press\src\production_runner.py | Select-String -Pattern "prefix|FORBIDDEN_PATTERNS|enforce_output_sanitation|enforce_no_new_tables|parts\[-1\].endswith" -Context 2,2
```

Подтвердить наличие:

- блока вычисления `prefix`
- строки `final_text = prefix + "".join(rebuilt_intervals)`
- функции `enforce_output_sanitation`
- функции `enforce_no_new_tables`
- проверки `not parts[-1].endswith("\n")` внутри `rebuild_interval`
- вызовов `enforce_output_sanitation(...)` и `enforce_no_new_tables(...)` в маркер-цикле

---

## LOCAL_VERIFY

**Без полного прогона.** Допустимо:

### 1. py_compile

```powershell
E:\Gemini\dojo\Manuscript_Press\.venv\Scripts\python.exe -m py_compile src\production_runner.py
```

Ожидаемо: exit 0, без вывода.

### 2. Preflight

Не выполнять. Preflight подтверждён ранее в RUN_ID `20261001T095517Z`.

### 3. Точечная проверка на MP:0001

```powershell
E:\Gemini\dojo\Manuscript_Press\.venv\Scripts\python.exe -m src.production_runner --start-marker MP:0001 --prior-run-dir Output\runs\20261001T142835Z --end-marker MP:0001
```

**Примечание:** предыдущий `restored.md` для MP:0001 есть в `Output\runs\20261001T142835Z\MP-0001\restored.md`. Использовать этот prior-run-dir.

Ожидаемо:

- `load_model: OK`
- один `create_chat_completion`
- выход маркера проходит `enforce_output_sanitation` и `enforce_no_new_tables`
- `restored.md` для MP:0001 в новом run_dir непустой
- `FINAL.manuscript.md` не пишется (range mode)
- exit 0

**Если без нового inference доказать правки нельзя — допускается один inference MP:0001 (см. выше). Второго прогона нет.**

**При ошибке:** STOP, traceback в отчёт.

### 4. Состояние FINAL до и после

```powershell
Test-Path E:\Gemini\dojo\Manuscript_Press\Output\FINAL.manuscript.md
```

Зафиксировать до и после шага 3. Если файл существовал до — подтвердить неизменность (размер и mtime). Если не существовал — подтвердить, что не появился.

---

## EVIDENCE

В отчёт включить:

- фактические строки из readback (EDIT 1–4)
- вывод `py_compile`
- вывод точечной проверки на MP:0001:
  - `load_model: OK`
  - `completion_calls_total: 1` (из `summary.json`)
  - `END_MARKER_REACHED`
  - путь и размер `restored.md` для MP:0001
  - подтверждение, что `enforce_output_sanitation` и `enforce_no_new_tables` отработали без исключений
- состояние `Output\FINAL.manuscript.md` до и после

---

## REPORT

```yaml
STEP_HARDENING_OUTPUT_SANITATION_REPORT:
  files_modified:
    - src/production_runner.py

  physical_lines:
    prefix_block: "<num>: <text>"
    final_text_with_prefix: "<num>: <text>"
    rebuild_interval_newline_guard: "<num>: <text>"
    enforce_output_sanitation_def: "<num>: <text>"
    enforce_no_new_tables_def: "<num>: <text>"
    enforce_output_sanitation_call: "<num>: <text>"
    enforce_no_new_tables_call: "<num>: <text>"

  py_compile: PASS / FAIL

  spot_check_MP_0001:
    executed: yes/no
    prior_run_dir: Output\runs\20261001T142835Z
    exit_code: <int>
    load_model_called: true
    completion_calls_total_from_summary_json: <int>
    new_run_id: "<timestamp>Z"
    restored_md_path: "Output/runs/<new_id>/MP-0001/restored.md"
    restored_md_size: <bytes>
    enforce_output_sanitation_passed: yes/no
    enforce_no_new_tables_passed: yes/no
    error: none / "<traceback если был>"

  final_manuscript_state_before: present / absent
  final_manuscript_state_after: present / absent
  final_manuscript_unchanged: yes / no / n/a

  second_run: none
  next: STOP → WAIT_FOR_SENSEI
```

**Только фактически подтверждённое.**

---

## NON-GOALS

- full article run (375 маркеров)
- 10B модель
- правки `SPEC.md`, `SPEC_v3.2.2.md`
- правки Input, `Gemma.md`, `writer_config.yaml`, `loader.py`, `parser/*`
- правки `manuscript_press.bat`, `resume_manuscript_press.bat`
- правки preflight / restore / cache логики
- второй прогон при ошибке

---

## END PROTOCOL

```text
EDIT → PY_COMPILE → SPOT CHECK MP:0001 → REPORT → STOP → WAIT_FOR_SENSEI
```

Full article run остаётся закрытым.

---

```yaml
BRIGADIER_STATUS:
  step: HARDENING_OUTPUT_SANITATION
  version: 1.0
  status: READY_FOR_SAMURAI
  route: LOCKED
  scope: four hardening items only
  full_run: RED
  ten_b: not activated
  spec_md: DO_NOT_TOUCH
  stop: true
```

STOP.