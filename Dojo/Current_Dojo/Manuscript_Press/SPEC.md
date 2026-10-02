# STEP.md — MANUSCRIPT_PRESS / LAUNCHERS + MARKER RANGE

```yaml
IDENTITY:
  Project: MANUSCRIPT_PRESS
  Phase: POST_RECONSTRUCT
  Step: LAUNCHERS_AND_MARKER_RANGE
  Version: 2.1
  Status: READY_FOR_SAMURAI
  Date: 2026-10-01
  Step Type: EDIT

  Technical Authority:
    - SPEC v3.3 (current execution contract)
    - SPEC_v3.2.2 (target, archived, not implemented)
    - Shogun route decision, 2026-10-01

  Scope: launcher cleanup + marker range (--start-marker / --end-marker).
  Not production run. Not hardening.
```

---

## OBJECTIVE

1. Привести launcher-набор в порядок: полный прогон + resume-латание — два разных BAT.
2. Удалить stale `run_manuscript_press.bat` из корня.
3. В `src/production_runner.py` добавить `--end-marker ID` рядом с существующим `--start-marker`.
4. Verify: py_compile + один контрольный inference на одну метку.

---

## ALLOWED WORKING FILES

**Изменить:**

```
E:\Gemini\dojo\Manuscript_Press\manuscript_press.bat
E:\Gemini\dojo\Manuscript_Press\src\production_runner.py
```

**Создать:**

```
E:\Gemini\dojo\Manuscript_Press\resume_manuscript_press.bat
```

**Переместить в `Archive\historical_launchers\`:**

```
E:\Gemini\dojo\Manuscript_Press\run_manuscript_press.bat
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
```

---

## DO_NOT

- Не добавлять `--max-markers`, `--limit`, `--single`, `--stop-after`.
- Не переписывать `run_manuscript_press.bat` в копию `manuscript_press.bat`.
- Не передавать аргументы в `manuscript_press.bat`.
- Не запускать full article run (375 маркеров).
- Не активировать 10B модель.
- Не открывать hardening.
- Не изменять существующую FINAL assembly logic. Разрешён только явно заданный range-mode bypass из EDIT 4e.

---

## EDIT 1 — `manuscript_press.bat`

Заменить тело целиком на:

```bat
@echo off
cd /d "%~dp0"
set PYTHONPATH=%CD%
.venv\Scripts\python.exe -m src.production_runner
```

Аргументов нет. Двойной щелчок = весь граф.

---

## EDIT 2 — создать `resume_manuscript_press.bat`

Тело файла:

```bat
@echo off
cd /d "%~dp0"
set PYTHONPATH=%CD%
if "%~1"=="" goto usage
if "%~2"=="" goto usage
if "%~3"=="" (
  .venv\Scripts\python.exe -m src.production_runner --start-marker %1 --prior-run-dir %2
  exit /b %ERRORLEVEL%
)
.venv\Scripts\python.exe -m src.production_runner --start-marker %1 --prior-run-dir %2 --end-marker %3
exit /b %ERRORLEVEL%
:usage
echo resume_manuscript_press.bat START_MARKER PRIOR_RUN_DIR [END_MARKER]
exit /b 2
```

---

## EDIT 3 — архивировать `run_manuscript_press.bat`

Переместить файл целиком:

```
E:\Gemini\dojo\Manuscript_Press\run_manuscript_press.bat
→
E:\Gemini\dojo\Manuscript_Press\Archive\historical_launchers\run_manuscript_press.bat
```

В рабочем корне файла быть не должно.

---

## EDIT 4 — `src/production_runner.py` — добавить `--end-marker ID`

### a) В argparse, сразу после аргумента `--prior-run-dir`:

```python
ap.add_argument(
    "--end-marker",
    default=None,
    help="Last marker id to process (inclusive). Requires --start-marker.",
)
```

### b) После `args = ap.parse_args()`:

```python
if args.end_marker and not args.start_marker:
    print("FATAL: --end-marker requires --start-marker", file=sys.stderr)
    return 2
```

### c) В блоке обработки `--start-marker` (там, где определяется `start_idx`) добавить `end_idx`:

```python
end_idx: Optional[int] = None
if args.start_marker:
    ids = [m.marker_id for m in marker_graph]
    if args.start_marker not in ids:
        raise ValueError(f"--start-marker not in graph: {args.start_marker}")
    start_idx = ids.index(args.start_marker)
    if not args.prior_run_dir:
        raise ValueError("--start-marker requires --prior-run-dir")
    if args.end_marker:
        if args.end_marker not in ids:
            raise ValueError(f"--end-marker not in graph: {args.end_marker}")
        end_idx = ids.index(args.end_marker)
        if end_idx < start_idx:
            raise ValueError(
                f"--end-marker {args.end_marker} precedes --start-marker {args.start_marker}"
            )
    log(f"RESUME from {args.start_marker} (index {start_idx}) prior={args.prior_run_dir}")
```

### d) В начале итерации цикла, после существующего `if idx < start_idx: continue`:

```python
if end_idx is not None and idx > end_idx:
    break
```

### e) После цикла, до блока `final_text = "".join(rebuilt_intervals)`:

```python
if end_idx is not None:
    log(f"END_MARKER_REACHED: end={args.end_marker} processed_upto_idx={end_idx}")
    log(f"completion_calls_total: {completion_calls}")
    log("status: SUCCESS_RANGE scope: PILOT_PRODUCTION")
    log("FINAL not written (range mode)")
    write_text(str(run_dir / "run.log"), "\n".join(log_lines) + "\n")
    write_text(str(run_dir / "summary.json"), json.dumps({
        "status": "SUCCESS_RANGE",
        "scope": "PILOT_PRODUCTION",
        "start_marker": args.start_marker,
        "end_marker": args.end_marker,
        "marker_count": len(marker_graph),
        "completion_calls_total": completion_calls,
        "final_written": False,
        "run_dir": str(run_dir),
    }, indent=2))
    return 0
```

### f) Инвариант поведения

- Без `--start-marker` и без `--end-marker` — весь граф, FINAL в конце. Поведение не меняется.
- С `--start-marker` без `--end-marker` — от START до конца графа.
- С `--start-marker` и `--end-marker` — от START до END включительно, FINAL не пишется.

---

## MANDATORY_PHYSICAL_READBACK

После edit — прочитать с диска и привести в отчёте:

```powershell
Get-Content E:\Gemini\dojo\Manuscript_Press\manuscript_press.bat
Get-Content E:\Gemini\dojo\Manuscript_Press\resume_manuscript_press.bat
Get-Content E:\Gemini\dojo\Manuscript_Press\src\production_runner.py | Select-String -Pattern "end-marker|end_marker|end_idx" -Context 2,2
Test-Path E:\Gemini\dojo\Manuscript_Press\run_manuscript_press.bat
Test-Path E:\Gemini\dojo\Manuscript_Press\Archive\historical_launchers\run_manuscript_press.bat
```

Привести фактические строки (номер + текст) для:

- `add_argument("--end-marker"`
- `if args.end_marker and not args.start_marker:`
- `end_idx = ids.index(args.end_marker)`
- `if end_idx is not None and idx > end_idx:`
- `if end_idx is not None:`

Подтвердить:

- `run_manuscript_press.bat` в корне — отсутствует
- `Archive\historical_launchers\run_manuscript_press.bat` — присутствует

---

## LOCAL_VERIFY

### 1. py_compile

```powershell
E:\Gemini\dojo\Manuscript_Press\.venv\Scripts\python.exe -m py_compile src\production_runner.py
```

Ожидаемо: exit 0, без вывода.

### 2. Preflight

Не выполнять. Preflight уже подтверждён в RUN_ID `20261001T095517Z` (exit 0, marker_count=375, validator PASS, completion=0).

### 3. Состояние FINAL до контрольного inference

```powershell
Test-Path E:\Gemini\dojo\Manuscript_Press\Output\FINAL.manuscript.md
```

Зафиксировать `True`/`False` до запуска.

### 4. Один контрольный inference

```powershell
E:\Gemini\dojo\Manuscript_Press\.venv\Scripts\python.exe -m src.production_runner --start-marker MP:0001 --prior-run-dir Output\runs\20261001T095517Z --end-marker MP:0001
```

Ожидаемо:

- `load_model: OK`
- один `create_chat_completion`
- обработан `MP:0001`
- `Output\runs\<new_id>\MP-0001\restored.md` непустой
- в `run.log` — `END_MARKER_REACHED`, `completion_calls_total: 1`
- в `summary.json` — `completion_calls_total: 1`, `final_written: false`
- exit 0

При ошибке — STOP, traceback в отчёт, второго прогона нет.

### 5. Состояние FINAL после контрольного inference

```powershell
Test-Path E:\Gemini\dojo\Manuscript_Press\Output\FINAL.manuscript.md
```

Сравнить с состоянием до inference. Если файл существовал до — подтвердить неизменность (размер и mtime). Если не существовал — подтвердить, что не появился.

---

## EVIDENCE

В отчёт включить:

- фактические строки из readback (EDIT 4: a–e + подтверждение archive)
- содержимое `manuscript_press.bat` и `resume_manuscript_press.bat` — полностью
- результаты `Test-Path` для обоих BAT
- вывод `py_compile` (пусто = PASS)
- состояние `Output\FINAL.manuscript.md` до контрольного inference
- вывод контрольного inference:
  - `load_model: OK`
  - `END_MARKER_REACHED`
  - `completion_calls_total: 1` — читается из `Output\runs\<new_id>\summary.json`
  - путь и размер `restored.md` для `MP-0001`
- состояние `Output\FINAL.manuscript.md` после контрольного inference

---

## REPORT

```yaml
STEP_LAUNCHERS_AND_MARKER_RANGE_REPORT:
  files_modified:
    - manuscript_press.bat
    - src/production_runner.py
  files_created:
    - resume_manuscript_press.bat
  files_archived:
    - run_manuscript_press.bat → Archive\historical_launchers\run_manuscript_press.bat

  physical_lines:
    arg_end_marker: "<num>: <text>"
    validation_end_requires_start: "<num>: <text>"
    end_idx_assignment: "<num>: <text>"
    loop_break: "<num>: <text>"
    post_loop_block: "<num>: <text>"

  bat_content:
    manuscript_press.bat: "<full physical content>"
    resume_manuscript_press.bat: "<full physical content>"

  run_manuscript_press_in_root: absent
  run_manuscript_press_in_archive: present

  py_compile: PASS / FAIL

  final_manuscript_state_before: present / absent
  final_manuscript_state_after: present / absent
  final_manuscript_unchanged: yes / no / n/a

  range_inference:
    executed: yes/no
    start_marker: MP:0001
    end_marker: MP:0001
    prior_run_dir: Output\runs\20261001T095517Z
    exit_code: <int>
    load_model_called: true
    completion_calls_total_from_summary_json: <int>
    processed_marker_id: "MP:0001"
    restored_md_path: "Output/runs/<new_id>/MP-0001/restored.md"
    restored_md_size: <bytes>
    error: none / "<traceback если был>"

  second_run: none

  next: STOP → WAIT_FOR_SENSEI
```

---

## NON-GOALS

- `--max-markers`
- full article run (375 маркеров)
- 10B модель
- hardening
- правки `SPEC.md`, `SPEC_v3.2.2.md`
- правки Input, `Gemma.md`, `writer_config.yaml`, `loader.py`, `parser/*`
- правки preflight / restore / cache логики
- второй прогон контрольного inference при ошибке

---

## END PROTOCOL

```text
EDIT → PY_COMPILE → ONE INFERENCE (MP:0001 → MP:0001) → REPORT → STOP → WAIT_FOR_SENSEI
```

Full article run остаётся закрытым.

---

```yaml
BRIGADIER_STATUS:
  step: LAUNCHERS_AND_MARKER_RANGE
  version: 2.1
  status: READY_FOR_SAMURAI
  route: LOCKED
  scope: launcher cleanup + --end-marker
  doctor_hold_resolved: yes (5 corrections integrated)
  full_run: RED
  ten_b: not activated
  hardening: closed
  spec_md: DO_NOT_TOUCH
  stop: true
```
---
STOP.