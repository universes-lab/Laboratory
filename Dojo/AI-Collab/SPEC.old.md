# SPEC.md — BUILD 001 / STEP 1 — FIXTURE SERVER (v1.1)

```yaml
IDENTITY:
  Project: AI-Collab
  Build: 001
  Step: 1
  Name: FIXTURE_SERVER
  Version: 1.1
  Status: READY_FOR_SAMURAI
  Date: 2026-10-19
  Type: FIXTURE

  Technical Authority:
    - Grok BUILD 001 / STEP 1 (2026-10-19)
    - WS1A_EXPERIMENT_PACKAGE.md §5, §10 (read-only, scope limited to STEP 1)
    - Grok corrections (port, switch persistence)

  Scope: локальный fixture-сервер с двумя беседами, журналом истины, персистентным переключателем.
  WS1A §5 шире этого шага: логин, cookie, потоковая выдача, ленивая история НЕ реализуются.
```

---

## OBJECTIVE

Создать с нуля в `E:\Gemini\Dojo\AI-Collab\` локальный fixture-сервер на `127.0.0.1:5999`, который:

1. Отдаёт две беседы по постоянным адресам: `conv_a` и `conv_b`.
2. У каждой — 2 user + 2 assistant (детерминированные).
3. Пишет `truth.json` — журнал истины (создаётся при старте).
4. Имеет переключатель `switch_conv_a_to_b`, **который меняет `truth.json` на диске** (не только память).
5. Самопроверка: без переключателя журнал совпадает; с переключателем `conv_a` отдаёт `conv_b`.
6. **Не отдаёт `truth.json` по HTTP.**

---

## ALLOWED WORKING FILES

**Создать в `E:\Gemini\Dojo\AI-Collab\`:**

```
fixture_server.py
truth.json          (создаётся при старте)
README.md           (optional)
```

**Не трогать:**

```
E:\Gemini\AI-Colab\                    # старый сервер (одна "l"), ЗАПРЕЩЁН
E:\Gemini\Dojo\Manuscript_Press\       # другой проект
рабочие профили браузера
реальные аккаунты
```

**Не создавать:**

```
кресла (SEAT)           # будущий объект, вне STEP 1
харнесс                 # будущий клиент, вне STEP 1
браузер / Playwright / Selenium
клиент сверки
```

---

## DO_NOT

- ❌ браузер, headless browser, Playwright, Selenium
- ❌ внешние сетевые адреса (только `127.0.0.1`)
- ❌ отдача `truth.json` по HTTP (любой путь)
- ❌ чтение / копирование / запуск `E:\Gemini\AI-Colab\`
- ❌ кресла, харнесс, клиент
- ❌ изменение `Manuscript_Press`
- ❌ внешние зависимости (stdlib Python only)
- ❌ **молчаливый выбор другого порта при занятости 5999**
- ❌ WS1A §5 в полном объёме (логин, cookie, потоковая выдача, ленивая история) — вне STEP 1

---

## IMPLEMENTATION

### 1. `fixture_server.py`

**Язык:** Python 3, только stdlib (`http.server`, `json`, `threading`, `os`, `sys`).

**Bind:** `127.0.0.1`, **порт `5999`**.

**Если порт 5999 занят — STOP с сообщением:**

```
FATAL: port 5999 is occupied. STEP 1 requires 5999. Do not auto-select another port.
```

Никакого «подберём свободный».

**`truth.json` при старте (если файла нет):**

```json
{
  "conversations": {
    "conv_a": {
      "conv_id": "conv_a",
      "messages": [
        {"role": "user", "content": "A-user-1"},
        {"role": "assistant", "content": "A-assistant-1"},
        {"role": "user", "content": "A-user-2"},
        {"role": "assistant", "content": "A-assistant-2"}
      ]
    },
    "conv_b": {
      "conv_id": "conv_b",
      "messages": [
        {"role": "user", "content": "B-user-1"},
        {"role": "assistant", "content": "B-assistant-1"},
        {"role": "user", "content": "B-user-2"},
        {"role": "assistant", "content": "B-assistant-2"}
      ]
    }
  },
  "switch_conv_a_to_b": false
}
```

**Точные тексты сообщений** — детерминированные, различимые (A vs B), записаны в `truth.json` при первом старте.

**HTTP endpoints:**

| Метод | Путь | Поведение |
|-------|------|-----------|
| GET | `/conv_a` | если `switch_conv_a_to_b == false` → отдать `conv_a`; если `true` → отдать `conv_b` (с `conv_id: "conv_b"`) |
| GET | `/conv_b` | всегда отдать `conv_b` |
| GET | `/switch?value=true\|false` | **записать новое значение `switch_conv_a_to_b` в `truth.json` на диске**, вернуть `{"ok": true, "switch_conv_a_to_b": <value>}` |
| GET | `/health` | вернуть `{"ok": true}` |

**Формат ответа `/conv_a` / `/conv_b`:**

```json
{
  "conv_id": "conv_a" | "conv_b",
  "messages": [...]
}
```

**Запрещено отдавать по HTTP:**

- `/truth`
- `/truth.json`
- любые пути, содержащие содержимое `truth.json`

На такие запросы — **404**.

### 2. Персистентность переключателя

`/switch?value=...` **обязан**:

1. Прочитать `truth.json` с диска.
2. Изменить `switch_conv_a_to_b` в структуре.
3. Записать обновлённый `truth.json` обратно на диск (atomic: временный файл + rename).
4. Только после успешной записи ответить клиенту `{"ok": true, ...}`.

**Внутреннее состояние сервера** при каждом `/conv_a` **читает `truth.json` с диска**, а не кэш из памяти. Это гарантирует: самопроверка сможет прочитать `truth.json` и увидеть фактическое значение.

### 3. Самопроверка `--self-test`

При `python fixture_server.py --self-test`:

1. **Удалить существующий `truth.json`, если он есть** (чистый старт самопроверки).
2. Стартовать сервер на `127.0.0.1:5999` (если занят — FAIL).
3. Проверить:
   - `GET /health` → `{"ok": true}`
   - `GET /conv_a` → `conv_id == "conv_a"`, 4 сообщения
   - `GET /conv_b` → `conv_id == "conv_b"`, 4 сообщения
4. Прочитать `truth.json` с диска:
   - `switch_conv_a_to_b == false`
   - `conv_a.messages` (4) совпадают с ответом `/conv_a`
   - `conv_b.messages` (4) совпадают с ответом `/conv_b`
5. Выполнить `GET /switch?value=true`.
6. Прочитать `truth.json` с диска:
   - **`switch_conv_a_to_b == true`** (персистентность проверена)
7. Проверить:
   - `GET /conv_a` → `conv_id == "conv_b"`, 4 сообщения `conv_b`
8. Выполнить `GET /switch?value=false`.
9. Прочитать `truth.json` с диска:
   - **`switch_conv_a_to_b == false`**
10. Проверить:
    - `GET /conv_a` → снова `conv_id == "conv_a"`
11. Проверить:
    - `GET /truth` → 404
    - `GET /truth.json` → 404
12. Печать:
    ```
    SELF-TEST: PASS
    ```
    или
    ```
    SELF-TEST: FAIL — <шаг> — <причина>
    ```
13. Остановить сервер.
14. Exit code 0 при PASS, 1 при FAIL.

### 4. Обычный запуск

```
python fixture_server.py
```

Стартует на `127.0.0.1:5999`, создаёт `truth.json` (если нет), ждёт запросов. Самопроверку не запускает.

---

## LOCAL_VERIFY

```powershell
cd E:\Gemini\Dojo\AI-Collab
python fixture_server.py --self-test
```

**Ожидаемо:**

- `SELF-TEST: PASS`
- exit code 0
- процесс завершился

**Если FAIL** — STOP, отчёт с шагом и причиной.

---

## REPORT

```yaml
BUILD_001_STEP_1_REPORT:
  files_created:
    - E:\Gemini\Dojo\AI-Collab\fixture_server.py
    - E:\Gemini\Dojo\AI-Collab\truth.json
    - E:\Gemini\Dojo\AI-Collab\README.md (optional)

  server:
    bind: 127.0.0.1
    port: 5999
    port_auto_select: forbidden (confirmed)
    endpoints:
      - GET /conv_a
      - GET /conv_b
      - GET /switch?value=true|false
      - GET /health

  truth_json:
    path: E:\Gemini\Dojo\AI-Collab\truth.json
    schema_ok: yes/no
    conv_a_messages: 4
    conv_b_messages: 4
    served_by_http: no
    switch_persisted_to_disk: yes

  switch:
    endpoint: /switch
    writes_to_truth_json: yes
    conv_a_serves_conv_b_when_true: yes/no

  self_test:
    command: python fixture_server.py --self-test
    exit_code: <int>
    output_line: "SELF-TEST: PASS" / "SELF-TEST: FAIL — <reason>"

  forbidden_checks:
    no_browser: yes
    no_external_network: yes
    no_old_server_access: yes
    no_truth_over_http: yes
    no_seat_no_harness_no_client: yes
    no_ws1a_full_scope: yes

  inference_executed: false
  next: STOP → WAIT_FOR_GROK_OR_SHOGUN
```

---

## NON-GOALS

- кресла (SEAT)
- харнесс
- браузер
- Playwright / Selenium
- клиент сверки
- внешние сетевые адреса
- чтение / запуск `E:\Gemini\AI-Colab\`
- изменение `Manuscript_Press`
- отдача `truth.json` по HTTP
- WS1A §5 в полном объёме (логин, cookie, потоковая выдача, ленивая история)
- автоматический выбор другого порта при занятости 5999

---

## STOP CONDITIONS

- порт 5999 занят → STOP
- самопроверка FAIL → STOP
- попытка bind на внешний адрес → STOP
- попытка отдать `truth.json` по HTTP → STOP
- любой доступ к `E:\Gemini\AI-Colab\` → STOP
- попытка молча выбрать другой порт → STOP

---

## END PROTOCOL

```text
CREATE → SELF-TEST → REPORT → STOP → WAIT_FOR_GROK_OR_SHOGUN
```

---

```yaml
BRIGADIER_STATUS:
  build: 001
  step: 1
  spec_version: 1.1
  corrections_applied:
    - switch persists to truth.json on disk
    - port 5999, no auto-fallback
  status: READY_FOR_SAMURAI
  next: SHOGUN_DELIVERS_TO_SAMURAI
  stop: true
```
---
STOP.