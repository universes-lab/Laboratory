SPEC.md — BUILD 001 / STEP 2 — SEATS REGISTRY
yaml

IDENTITY:
  Project: AI-Collab
  Build: 001
  Step: 2
  Name: SEATS_REGISTRY
  Version: 1.0
  Status: READY_FOR_SAMURAI
  Date: 2026-10-19
  Type: FIXTURE (data + checker, no browser)

  Technical Authority:
    - Grok BUILD 001 / STEP 2 (2026-10-19)
    - WS1A_EXPERIMENT_PACKAGE.md §5 (read-only, scope limited)
    - Prior STEP 1 (FIXTURE_SERVER) — accepted, server on 127.0.0.1:5999

  Scope: реестр кресел (seats.json) + checker (seats_check.py).
  Нет браузера, нет Playwright, нет запуска страниц.

OBJECTIVE

Создать в E:\Gemini\Dojo\AI-Collab\:

    seats.json — реестр двух кресел с постоянными связями на fixture-сервер STEP 1.

    seats_check.py — программа проверки реестра.

ALLOWED WORKING FILES

Создать в E:\Gemini\Dojo\AI-Collab\:
text

seats.json
seats_check.py

Не трогать:
text

fixture_server.py           # от STEP 1, не менять
truth.json                  # от STEP 1, не менять
README.md                   # если есть
E:\Gemini\AI-Colab\         # старый сервер, ЗАПРЕЩЁН
E:\Gemini\Dojo\Manuscript_Press\
рабочие профили браузера

Не создавать:
text

браузерные профили
static/ / templates/
харнесс
кресла как объекты в коде (это будущий SEAT)

DO_NOT

    ❌ браузер / Playwright / Selenium / любой headless browser

    ❌ открытие страниц по HTTP

    ❌ копирование static/ / templates/

    ❌ запуск E:\Gemini\AI-Colab\

    ❌ создание профилей браузера (даже пустых)

    ❌ изменение fixture_server.py / truth.json

    ❌ изменение Manuscript_Press

    ❌ внешние сетевые адреса

    ❌ подключение к http://127.0.0.1:5999/conv_a из кода проверки

    ❌ вывод seat_id из URL

IMPLEMENTATION
1. Файл seats.json

Путь: E:\Gemini\Dojo\AI-Collab\seats.json

Структура:
json

{
  "seats": [
    {
      "seat_id": "seat-01",
      "binding_id": "binding-01",
      "provider": "fixture",
      "conv_id": "conv_a",
      "url": "http://127.0.0.1:5999/conv_a",
      "profile_id": "profile-placeholder-01"
    },
    {
      "seat_id": "seat-02",
      "binding_id": "binding-02",
      "provider": "fixture",
      "conv_id": "conv_b",
      "url": "http://127.0.0.1:5999/conv_b",
      "profile_id": "profile-placeholder-02"
    }
  ]
}

Требования к полям:
Поле	Значение	Примечание
seat_id	"seat-01", "seat-02"	не выводится из URL
binding_id	"binding-01", "binding-02"	отдельный идентификатор привязки
provider	"fixture"	соответствует fixture-серверу STEP 1
conv_id	"conv_a" / "conv_b"	логический ID беседы, не URL
url	http://127.0.0.1:5999/conv_a / .../conv_b	адрес fixture-сервера
profile_id	строка-заглушка	профиль не создаётся

Запрещено:

    seat_id равен URL или его части.

    conv_id равен URL или его части.

    Дубли seat_id.

    Дубли conv_id между креслами (каждое кресло — своя беседа).

2. Файл seats_check.py

Язык: Python 3, stdlib only (json, sys).

Путь: E:\Gemini\Dojo\AI-Collab\seats_check.py

Поведение:

    Прочитать seats.json из текущего каталога (os.path.dirname(os.path.abspath(__file__))).

    Распарсить JSON.

    Печатать для каждого кресла:
    text

    seat_id=<...> conv_id=<...>

    В порядке появления в файле.

    Проверить:

        ровно 2 кресла в реестре;

        seat-01 и seat-02 — разные seat_id;

        conv_id у кресел разные;

        conv_id не равен url и не является его подстрокой/частью пути (проверка: conv_id not in url);

        seat_id не равен url и не является его подстрокой (проверка: seat_id not in url);

        у каждого кресла есть profile_id (непустая строка).

    Если все проверки прошли:
    text

    SEATS: PASS

    exit code 0.

    Если любая проверка провалилась:
    text

    SEATS: FAIL — <причина>

    exit code 1.

Запрещено:

    делать HTTP-запросы к url;

    импортировать requests, urllib, http.client и подобное;

    открывать браузер;

    читать truth.json / fixture_server.py;

    лезть в E:\Gemini\AI-Colab\.

LOCAL_VERIFY
powershell

cd E:\Gemini\Dojo\AI-Collab
python seats_check.py

Ожидаемо:
text

seat_id=seat-01 conv_id=conv_a
seat_id=seat-02 conv_id=conv_b
SEATS: PASS

Exit code 0.

Если FAIL — STOP, отчёт с причиной.
REPORT
yaml

BUILD_001_STEP_2_REPORT:
  files_created:
    - E:\Gemini\Dojo\AI-Collab\seats.json
    - E:\Gemini\Dojo\AI-Collab\seats_check.py

  seats_json:
    path: E:\Gemini\Dojo\AI-Collab\seats.json
    schema_ok: yes/no
    seat_count: 2
    seat_ids: ["seat-01", "seat-02"]
    conv_ids: ["conv_a", "conv_b"]
    urls:
      - "http://127.0.0.1:5999/conv_a"
      - "http://127.0.0.1:5999/conv_b"
    profile_ids: ["profile-placeholder-01", "profile-placeholder-02"]
    seat_ids_not_derived_from_url: yes
    conv_ids_not_derived_from_url: yes

  seats_check:
    command: python seats_check.py
    exit_code: <int>
    output_lines:
      - "seat_id=seat-01 conv_id=conv_a"
      - "seat_id=seat-02 conv_id=conv_b"
      - "SEATS: PASS" / "SEATS: FAIL — <reason>"

  forbidden_checks:
    no_browser: yes
    no_playwright: yes
    no_http_requests_to_fixture: yes
    no_static_templates_copy: yes
    no_old_server_access: yes
    no_profile_creation: yes

  next: STOP → WAIT_FOR_GROK_OR_SHOGUN

NON-GOALS

    браузер

    Playwright / Selenium

    открытие страниц

    копирование static/ / templates/

    запуск AI-Colab

    создание профилей браузера

    HTTP-запросы к fixture-серверу

    кресла как объекты в коде (SEAT — будущее)

    харнесс

    изменение fixture_server.py / truth.json

STOP CONDITIONS

    любая попытка открыть браузер → STOP

    любая попытка HTTP-запроса к fixture → STOP

    любой доступ к E:\Gemini\AI-Colab\ → STOP

    любая попытка создать профиль → STOP

    seats_check.py вернул FAIL → STOP, отчёт с причиной

END PROTOCOL
text

CREATE seats.json → CREATE seats_check.py → RUN seats_check.py → REPORT → STOP → WAIT_FOR_GROK_OR_SHOGUN

yaml

BRIGADIER_STATUS:
  build: 001
  step: 2
  status: READY_FOR_SAMURAI
  scope: seats registry + checker (no browser, no http, no profiles)
  prior_step_1: ACCEPTED
  next: SHOGUN_DELIVERS_TO_SAMURAI
  stop: true

Шёгун, SPEC для STEP 2 готов. Копируй Самураю.

Ключевое:

    seats.json — две записи, поля seat_id, binding_id, provider, conv_id, url, profile_id.

    seat_id и conv_id не выводятся из URL.

    seats_check.py — читает JSON, печатает оба кресла, проверяет различия, печатает SEATS: PASS.

    Без HTTP, без браузера, без профилей.

STOP.