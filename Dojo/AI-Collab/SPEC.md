SPEC.md — BUILD 001 / STEP 3 — OPEN SEATS IN BROWSER
yaml

BUILD: 001
STEP: 3
NAME: OPEN_SEATS_IN_BROWSER
VERSION: 1.0
STATUS: READY_FOR_SAMURAI
DATE: 2026-10-19

OBJECTIVE

Открыть два кресла (seat-01 и seat-02) в двух независимых процессах Microsoft Edge, каждый в пустом профиле. Без драйвера, без Playwright, без Selenium, без вердиктов. Собрать PID в open_seats.json.
FILES
text

CREATE:  E:\Gemini\Dojo\AI-Collab\open_seats.py
CREATE:  E:\Gemini\Dojo\AI-Collab\open_seats.json     (создаётся при запуске)
CREATE:  E:\Gemini\Dojo\AI-Collab\profiles\seat-01\   (пустой каталог)
CREATE:  E:\Gemini\Dojo\AI-Collab\profiles\seat-02\   (пустой каталог)

DO NOT TOUCH:
  E:\Gemini\AI-Colab\
  E:\Gemini\Dojo\AI-Collab\fixture_server.py
  E:\Gemini\Dojo\AI-Collab\truth.json
  E:\Gemini\Dojo\AI-Collab\seats.json
  E:\Gemini\Dojo\AI-Collab\seats_check.py
  E:\Gemini\Dojo\Manuscript_Press\
  профиль Автора (любой существующий профиль Edge)

DO NOT
text

❌ Не запускать Playwright / Selenium / любой драйвер.
❌ Не использовать профиль Автора.
❌ Не обращаться к E:\Gemini\AI-Colab\.
❌ Не копировать static/ или templates/.
❌ Не выносить вердикт RECOVERED / MISMATCH / любой.
❌ Не менять conv_id (conv_a / conv_b).
❌ Не подменять порт 5999, если fixture не запущен.
❌ Не убивать браузеры после запуска.
❌ Не писать в truth.json.

WHAT TO CREATE
Файл open_seats.py

Один файл, Python 3, только stdlib (os, sys, json, subprocess, urllib.request, pathlib).
Файл open_seats.json (создаётся при запуске)
text

{
  "seat-01": {
    "pid": <int>,
    "url": "http://127.0.0.1:5999/conv_a",
    "profile_dir": "E:\\Gemini\\Dojo\\AI-Collab\\profiles\\seat-01"
  },
  "seat-02": {
    "pid": <int>,
    "url": "http://127.0.0.1:5999/conv_b",
    "profile_dir": "E:\\Gemini\\Dojo\\AI-Collab\\profiles\\seat-02"
  }
}

Каталоги профилей
text

E:\Gemini\Dojo\AI-Collab\profiles\seat-01\
E:\Gemini\Dojo\AI-Collab\profiles\seat-02\

Пустые. Если не существуют — создать. Если существуют — использовать как есть, не чистить.
EXECUTION FLOW OF open_seats.py

Шаг 1. Проверить, что fixture-сервер отвечает:
text

GET http://127.0.0.1:5999/health

Ожидаемый ответ: {"ok": true}.

Если не отвечает или ответ не {"ok": true}:
text

FATAL: fixture not running on 127.0.0.1:5999

STOP, exit 1. Не подменять порт.

Шаг 2. Проверить, что Edge доступен:
text

where msedge

или
text

where microsoft-edge

или эквивалент в PATH. Если не найден — попробовать стандартные пути Windows:
text

C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe
C:\Program Files\Microsoft\Edge\Application\msedge.exe

Если ни один не найден:
text

FATAL: Microsoft Edge not found

STOP, exit 1.

Шаг 3. Создать каталоги профилей (если нет):
text

E:\Gemini\Dojo\AI-Collab\profiles\seat-01\
E:\Gemini\Dojo\AI-Collab\profiles\seat-02\

Шаг 4. Запустить два процесса Edge:
text

msedge --user-data-dir=E:\Gemini\Dojo\AI-Collab\profiles\seat-01 http://127.0.0.1:5999/conv_a
msedge --user-data-dir=E:\Gemini\Dojo\AI-Collab\profiles\seat-02 http://127.0.0.1:5999/conv_b

Требования:
text

Запуск через subprocess.Popen.
Не ждать завершения (не subprocess.run, не wait).
Не убивать процессы после.
Сохранить PID каждого.

Шаг 5. Записать open_seats.json с двумя записями: pid, url, profile_dir.

Шаг 6. Напечатать:
text

OPEN: PASS

Exit 0.
LOCAL VERIFY
text

cd E:\Gemini\Dojo\AI-Collab
python open_seats.py

Ожидаемо:
text

exit code 0
stdout: OPEN: PASS
open_seats.json создан, два разных pid
два процесса Edge живы (не убивать)

Проверка PID после запуска:
text

type open_seats.json
tasklist | findstr msedge

Оба PID из open_seats.json должны присутствовать в tasklist.
STOP CONDITIONS
text

Если fixture не отвечает на 127.0.0.1:5999/health → STOP, exit 1.
Если Edge не найден → STOP, exit 1.
Если процесс Edge упал сразу после запуска (PID отсутствует в tasklist через 2 секунды) → STOP, exit 1.
Если попытка открыть не тот URL (не conv_a / conv_b) → STOP.
Если попытка использовать профиль Автора → STOP.
Если попытка запустить Playwright / Selenium → STOP.

REPORT
yaml

BUILD_001_STEP_3_REPORT:
  files_created:
    - E:\Gemini\Dojo\AI-Collab\open_seats.py
    - E:\Gemini\Dojo\AI-Collab\open_seats.json
    - E:\Gemini\Dojo\AI-Collab\profiles\seat-01\
    - E:\Gemini\Dojo\AI-Collab\profiles\seat-02\

  fixture_check:
    url: http://127.0.0.1:5999/health
    response: <actual>
    ok: yes/no

  edge_check:
    path: <actual msedge path>
    found: yes/no

  processes:
    seat-01:
      pid: <int>
      alive_after_start: yes/no
    seat-02:
      pid: <int>
      alive_after_start: yes/no
    pids_distinct: yes/no

  open_seats_json:
    path: E:\Gemini\Dojo\AI-Collab\open_seats.json
    schema_ok: yes/no
    two_entries: yes/no

  stdout_line: "OPEN: PASS"
  exit_code: <int>

  forbidden_checks:
    no_playwright: yes
    no_selenium: yes
    no_driver: yes
    no_author_profile: yes
    no_old_ai_colab: yes
    no_static_templates: yes
    no_verdict: yes
    no_conv_id_change: yes
    no_port_substitution: yes
    browsers_not_killed: yes

  next: STOP → WAIT_FOR_SENSEI

NON-GOALS
text

❌ вердикт RECOVERED / MISMATCH / любой
❌ закрытие браузеров
❌ смена conv_id
❌ Playwright / Selenium
❌ копирование static / templates
❌ работа с E:\Gemini\AI-Colab\
❌ изменение fixture_server.py / truth.json / seats.json / seats_check.py

END PROTOCOL
text

CHECK FIXTURE → CHECK EDGE → CREATE PROFILES → LAUNCH 2 EDGE PROCESSES → WRITE open_seats.json → PRINT "OPEN: PASS" → STOP → WAIT_FOR_SENSEI

