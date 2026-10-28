# SPEC.md — BUILD 001 / STEP 4 — API STUB A

```yaml
BUILD: 001
STEP: 4
NAME: API_STUB_A
VERSION: 1.0
STATUS: READY_FOR_SAMURAI
DATE: 2026-10-27
```

---

## OBJECTIVE

Создать тонкую заглушку `/api/*` на порту `8001`. Любой запрос под `/api/*` → **HTTP 501** с JSON `{"status": "NOT_IMPLEMENTED", ...}`. Логировать каждый hit в `logs/stub_not_implemented.jsonl`.

**Без живых LLM. Без FastAPI старого проекта. Без GCBEngine. Без shell.**

---

## FILES

```
CREATE:  E:\Gemini\Dojo\AI-Collab\stub_api.py
CREATE:  E:\Gemini\Dojo\AI-Collab\run_stub_api.bat    (опционально)
CREATE:  E:\Gemini\Dojo\AI-Collab\logs\               (каталог, если нет)

DO NOT TOUCH:
  fixture_server.py
  serve_interface.py
  static\chat.js
  static\seats_test.js
  templates\index.html
  E:\Gemini\AI-Colab\
  E:\Gemini\Dojo\Manuscript_Press\
```

---

## DO NOT

```
❌ Не импортировать app.py, gcb_engine, gateway, openrouter, любые live LLM.
❌ Не использовать subprocess / shell.
❌ Не открывать WebSocket MCP.
❌ Не отвечать 200 с фейковым успехом.
❌ Не менять chat.js (кроме отдельного решения Автора).
❌ Не менять порты 5999 (fixture) и 8000 (serve_interface).
❌ Не вшивать stub в serve_interface.
```

---

## IMPLEMENTATION

### 1. `stub_api.py` — единственный файл

**Язык:** Python 3.

**Зависимости:** допускается `fastapi` + `uvicorn` (если они установлены в окружении). Если нет — использовать **stdlib** (`http.server`) — предпочтительнее, чтобы не тянуть зависимости.

**Рекомендация:** stdlib. Проще, без установки пакетов.

### 2. Порт

- default: `8001`
- `--port <N>` — переопределение
- **не** 5999, **не** 8000
- **не** брать из `load_gemini_sockets()` или иных источников

### 3. Поведение

Любой путь под `/api/*` (и `/api` без слэша) → **HTTP 501**.

**JSON-ответ:**

```json
{
  "status": "NOT_IMPLEMENTED",
  "route": "<полный path>",
  "method": "<GET|POST|PUT|DELETE|...>"
}
```

**Обязательный минимум покрытия (то, что дёргает chat.js):**

```
GET  /api/project/current
GET  /api/model_mapping
GET  /api/info/{info_type}
POST /api/secretary
POST /api/session/{session_id}/analyze/{pair_id}
GET  /api/gcb/queue
POST /api/gcb/execute/{id}
```

**Catch-all:** `/api/{path:path}` и `/api` — тот же 501 для любого не перечисленного метода/пути под `/api/*`.

**Вне `/api/*`:** любой путь → 404 (обычный). Никаких 200-успехов.

### 4. Лог

Каждый hit → append в `logs/stub_not_implemented.jsonl`.

**Формат строки (JSONL, одна запись на строку):**

```json
{"timestamp": "<ISO 8601>", "method": "GET", "route": "/api/secretary", "client": "127.0.0.1"}
```

**Требования:**

- каталог `logs/` создаётся автоматически, если нет,
- файл append-only, не перезаписывается,
- кодировка UTF-8.

### 5. CORS (опционально, если не раздувает)

Для запросов с `Origin: http://127.0.0.1:8000` — отвечать заголовком:

```
Access-Control-Allow-Origin: http://127.0.0.1:8000
```

И для `OPTIONS` — 204 с разрешёнными методами:

```
Access-Control-Allow-Methods: GET, POST, OPTIONS
Access-Control-Allow-Headers: Content-Type
```

**Если это раздувает код** — пропустить. Тогда fetch с UI будет падать на CORS, но 501 будет виден в Network-панели.

### 6. Обычный запуск

```
python stub_api.py
python stub_api.py --port 8001
```

Ожидаемо в stdout/stderr:

```
stub_api listening on http://127.0.0.1:8001
```

Если порт занят — STOP, не подбирать другой.

---

## LOCAL VERIFY

**Шаг 1.** Запустить:

```powershell
cd E:\Gemini\Dojo\AI-Collab
python stub_api.py --port 8001
```

**Шаг 2.** Проверить через `urllib.request` (без curl):

```python
python -c "import urllib.request, urllib.error; \
  req = urllib.request.Request('http://127.0.0.1:8001/api/secretary', method='POST'); \
  try: urllib.request.urlopen(req) \
  except urllib.error.HTTPError as e: \
    print(e.code, e.read().decode()[:200])"
```

Ожидаемо: `501 {"status": "NOT_IMPLEMENTED", "route": "/api/secretary", "method": "POST"}`.

**Шаг 3.** Проверить `/api/project/current`:

```python
python -c "import urllib.request, urllib.error; \
  try: urllib.request.urlopen('http://127.0.0.1:8001/api/project/current') \
  except urllib.error.HTTPError as e: \
    print(e.code, e.read().decode()[:200])"
```

Ожидаемо: `501 {...}`.

**Шаг 4.** Проверить лог:

```powershell
Get-Content E:\Gemini\Dojo\AI-Collab\logs\stub_not_implemented.jsonl | Select-Object -Last 5
```

Ожидаемо: строки с `"route": "/api/secretary"`, `"route": "/api/project/current"`.

**Шаг 5.** Проверить, что `serve_interface` и `fixture` не затронуты:

```powershell
python verify_routes.py
```

Ожидаемо: `VERIFY: PASS` (как раньше).

---

## REPORT

```yaml
BUILD_001_STEP_4_REPORT:
  files_created:
    - E:\Gemini\Dojo\AI-Collab\stub_api.py
    - E:\Gemini\Dojo\AI-Collab\run_stub_api.bat (optional)
    - E:\Gemini\Dojo\AI-Collab\logs\stub_not_implemented.jsonl

  port: 8001
  framework: stdlib / fastapi

  behavior:
    all_api_returns_501: yes/no
    json_shape_correct: yes/no
    catches_minimum_routes: yes/no
    catch_all_api_path: yes/no

  cors:
    enabled: yes/no

  logging:
    jsonl_path: E:\Gemini\Dojo\AI-Collab\logs\stub_not_implemented.jsonl
    appended_on_hit: yes/no
    sample_lines:
      - "<first line>"
      - "<second line>"

  sample_501_body:
    route: /api/secretary
    method: POST
    body: '{"status": "NOT_IMPLEMENTED", ...}'

  forbidden_checks:
    no_legacy_app: yes
    no_gcb_engine: yes
    no_openrouter: yes
    no_subprocess: yes
    no_shell: yes
    no_websocket: yes
    no_200_fake_success: yes
    no_chat_js_edit: yes
    no_port_change_5999: yes
    no_port_change_8000: yes

  unaffected_services:
    fixture_5999: OK / FAIL
    serve_interface_8000: OK / FAIL
    verify_routes: PASS / FAIL

  next: STOP → WAIT_FOR_SENSEI
```

---

## NON-GOALS

```
❌ живые LLM
❌ FastAPI старого проекта
❌ GCBEngine
❌ shell / subprocess
❌ WebSocket MCP
❌ 200 с фейковым успехом
❌ правка chat.js
❌ смена портов 5999 / 8000
```

---

## STOP CONDITIONS

```
Если порт 8001 занят → STOP.
Если запрос под /api/* возвращает не 501 → STOP.
Если запрос вне /api/* возвращает не 404 → STOP.
Если в лог не пишется → STOP.
Если fixture или serve_interface затронуты → STOP.
Если импортирован app.py / gcb_engine → STOP.
```

---

## END PROTOCOL

```
CREATE stub_api.py → RUN → VERIFY 501 via urllib.request → CHECK logs → REPORT → STOP
```

---

```yaml
BRIGADIER_STATUS:
  build: 001
  step: 4
  step_3b: CLOSED (author visual check PASS)
  scope: API stub A — 501 for all /api/*
  next: SHOGUN_DELIVERS_TO_SAMURAI
  stop: true
```

---



Ключевое:

1. **`stub_api.py`** — порт 8001, любой `/api/*` → 501 с `{"status": "NOT_IMPLEMENTED", ...}`.
2. **Лог** — `logs/stub_not_implemented.jsonl`, append-only.
3. **Не трогать** `chat.js`, `fixture_server.py` (5999), `serve_interface.py` (8000).
4. **Без live LLM**, без GCB, без shell, без subprocess.
5. **Проверка** — через `urllib.request`, не curl.

STOP.