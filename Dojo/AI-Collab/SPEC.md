Принято, Грок. Процессная дисциплина + backup. Но есть проблема с `curl` — Самурай не может его использовать. Обхожу.

---

# SPEC.md — BUILD 001 / PROCESS DISCIPLINE + BACKUP

```yaml
BUILD: 001
STEP: PROCESS_DISCIPLINE
NAME: DUAL_RUN_AND_BACKUP
VERSION: 1.0
STATUS: READY_FOR_SAMURAI
DATE: 2026-10-27
```

---

## OBJECTIVE

1. Создать `dual_run.bat` — один запуск обоих серверов (fixture 5999 + serve_interface 8000).
2. Вызывать `samurai_backup.bat` перед каждым edit/STEP.
3. После PASS Автора — git commit или backup folder.
4. Запретить `python -m http.server` на 5999/8000.
5. Verify через `urllib.request` (не curl).

---

## FILES

```
CREATE:  E:\Gemini\Dojo\AI-Collab\dual_run.bat

DO NOT TOUCH:
  fixture_server.py
  serve_interface.py
  static\chat.js
  static\seats_test.js
  templates\index.html
  samurai_backup.bat        (только вызывать)
  restore_*.bat             (только вызывать)
  E:\Gemini\AI-Colab\
  E:\Gemini\Dojo\Manuscript_Press\
```

---

## DO NOT

```
❌ Не переписывать samurai_backup.bat / restore_*.bat.
❌ Не запускать python -m http.server на 5999 или 8000.
❌ Не запускать только один сервер «как UI».
❌ Не отвечать «assumed PASS» без фактической проверки.
❌ Не трогать chat.js / seats_test.js / index.html.
```

---

## IMPLEMENTATION

### 1. `dual_run.bat`

**Путь:** `E:\Gemini\Dojo\AI-Collab\dual_run.bat`

**Содержимое (bat, ANSI/UTF-8, CRLF):**

```bat
@echo off
setlocal

cd /d "%~dp0"

echo ============================================================
echo  AI-Collab dual run: fixture 5999 + serve_interface 8000
echo ============================================================
echo.

REM --- check ports are free ---
echo [CHECK] port 5999...
netstat -ano | findstr ":5999" | findstr "LISTENING" >nul
if %ERRORLEVEL%==0 (
    echo ERROR: port 5999 is already in use. Kill existing process first.
    echo Run:  netstat -ano ^| findstr :5999
    exit /b 1
)
echo [CHECK] port 5999 free

echo [CHECK] port 8000...
netstat -ano | findstr ":8000" | findstr "LISTENING" >nul
if %ERRORLEVEL%==0 (
    echo ERROR: port 8000 is already in use. Kill existing process first.
    echo Run:  netstat -ano ^| findstr :8000
    exit /b 1
)
echo [CHECK] port 8000 free

echo.
echo [START] fixture_server.py on 5999...
start "AI-Collab FIXTURE" cmd /k python fixture_server.py

timeout /t 2 /nobreak >nul

echo [START] serve_interface.py on 8000...
start "AI-Collab UI" cmd /k python serve_interface.py

timeout /t 2 /nobreak >nul

echo.
echo ============================================================
echo  UI:  http://127.0.0.1:8000/
echo  API: http://127.0.0.1:5999/health
echo ============================================================
echo.
echo Both servers started in separate windows.
echo Close those windows to stop the servers.
echo.
pause
```

**Требования:**

- `cd /d "%~dp0"` — всегда.
- Проверка `netstat` на 5999 и 8000 **до** запуска. Если занят — STOP с сообщением.
- `start "..." cmd /k python ...` — два отдельных окна.
- `timeout /t 2` между запусками.
- Финальный `pause` — чтобы окно не закрылось сразу.

### 2. Backup перед edit — не новый файл

`samurai_backup.bat` **уже существует** (от Мастера Сборки). **Не переписывать.** Вызывать:

```powershell
E:\Gemini\Dojo\AI-Collab\samurai_backup.bat
```

**Перед каждым edit** в рамках STEP, Самурай **обязан** вызвать `samurai_backup.bat`. Если его нет на диске — STOP, сообщить.

### 3. После PASS Автора — git commit

В `E:\Gemini\Dojo\AI-Collab\`:

```powershell
cd E:\Gemini\Dojo\AI-Collab
git add -A
git commit -m "STEP_<id> PASS"
```

**Если git недоступен** (`git` not found, или не git-репозиторий) — **backup folder only**: создать `backup\STEP_<id>_PASS_<timestamp>\` с копией всех файлов. Отчёт: `git_unavailable: yes, backup_folder: <path>`.

### 4. Запрет `python -m http.server` на 5999/8000

Ни в одном скрипте, ни в одной команде — не использовать `python -m http.server` на портах 5999 или 8000. Только `fixture_server.py` и `serve_interface.py`.

### 5. Verify

**Через `urllib.request`** (curl недоступен):

```python
python -c "import urllib.request; print(urllib.request.urlopen('http://127.0.0.1:5999/health').read().decode())"
```

Ожидаемо: `{"ok": true}`.

```python
python -c "import urllib.request; data = urllib.request.urlopen('http://127.0.0.1:8000/').read().decode(); print('seatsTestBtn' in data)"
```

Ожидаемо: `True`.

---

## LOCAL VERIFY

**Шаг 1.** Перед запуском — убедиться, что 5999 и 8000 свободны:

```powershell
netstat -ano | findstr ":5999 :8000"
```

Ожидаемо: пусто. Если занято — убить процессы:

```powershell
Get-NetTCPConnection -LocalPort 5999,8000 -State Listen -ErrorAction SilentlyContinue | ForEach-Object { Stop-Process -Id $_.OwningProcess -Force }
```

**Шаг 2.** Запустить `dual_run.bat`:

```powershell
cd E:\Gemini\Dojo\AI-Collab
dual_run.bat
```

Ожидаемо: два новых окна cmd — «AI-Collab FIXTURE» и «AI-Collab UI». В основном окне — `UI: http://...` и `API: http://...`.

**Шаг 3.** Проверить через `urllib.request`:

```powershell
python -c "import urllib.request; print(urllib.request.urlopen('http://127.0.0.1:5999/health').read().decode())"
python -c "import urllib.request; d = urllib.request.urlopen('http://127.0.0.1:8000/').read().decode(); print('seatsTestBtn' in d)"
```

Ожидаемо: `{"ok": true}` и `True`.

---

## REPORT

```yaml
STEP_PROCESS_DISCIPLINE_REPORT:
  files_created:
    - E:\Gemini\Dojo\AI-Collab\dual_run.bat

  dual_run:
    content_matches_spec: yes/no
    netstat_check_5999: yes/no
    netstat_check_8000: yes/no
    starts_fixture_window: yes/no
    starts_ui_window: yes/no
    final_pause: yes/no

  backup:
    samurai_backup_bat_exists: yes/no
    samurai_backup_called_before_edits: yes/no
    samurai_backup_not_modified: yes/no

  git:
    git_available: yes/no
    commit_after_pass: yes/no / pending_author_pass
    backup_folder_if_no_git: "<path / n/a>"

  forbidden_checks:
    no_python_http_server_5999: yes
    no_python_http_server_8000: yes
    no_single_server_as_ui: yes
    no_assumed_pass: yes
    no_chat_js_edit: yes
    no_index_html_edit: yes
    no_seats_test_js_edit: yes
    no_samurai_backup_rewrite: yes

  verify_via_urllib:
    health_5999: '{"ok": true}' / FAIL
    seatsTestBtn_in_8000: True / False

  next: STOP → WAIT_FOR_SENSEI
```

---

## NON-GOALS

```
❌ переписывание samurai_backup.bat / restore_*.bat
❌ python -m http.server на 5999/8000
❌ один сервер «как UI»
❌ assumed PASS без фактической проверки
❌ изменение chat.js / seats_test.js / index.html
❌ curl (недоступен)
```

---

## STOP CONDITIONS

```
Если samurai_backup.bat отсутствует → STOP, сообщить.
Если netstat показывает 5999 или 8000 занятыми до запуска → STOP.
Если dual_run.bat запускает python -m http.server → STOP.
Если после dual_run.bat health на 5999 не отвечает → STOP.
Если после dual_run.bat seatsTestBtn в 8000 не найден → STOP.
```

---

## END PROTOCOL

```
CREATE dual_run.bat → CHECK PORTS FREE → RUN dual_run → VERIFY via urllib → REPORT → STOP
```

---

```yaml
BRIGADIER_STATUS:
  build: 001
  step: process_discipline
  scope: dual_run.bat + backup discipline + git/backup after PASS
  samurai_backup_bat: existing, call only, do not rewrite
  verify_method: urllib.request (curl unavailable)
  next: SHOGUN_DELIVERS_TO_SAMURAI
  stop: true
```

---

**Шёгун, SPEC готов. Копируй Самураю.**

Ключевое:

1. **`dual_run.bat`** — один запуск, два окна (fixture 5999 + UI 8000). Проверка `netstat` до запуска. Финал — `pause`.
2. **`samurai_backup.bat`** — вызывать перед edit, **не переписывать**.
3. **После PASS** — `git commit -m "STEP_<id> PASS"` или backup folder.
4. **Запрет** `python -m http.server` на 5999/8000.
5. **Verify** — через `urllib.request`, не curl.

STOP.