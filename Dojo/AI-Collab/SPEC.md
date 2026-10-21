# SPEC.md — BUILD 001 / STEP 3b — SEATS TEST BUTTON

```yaml
BUILD: 001
STEP: 3b
NAME: SEATS_TEST_BUTTON
VERSION: 2.0
STATUS: READY_FOR_SAMURAI
DATE: 2026-10-20
```

---

## OBJECTIVE

Добавить в `templates/index.html` **одну кнопку** «Тест кресел» в верхнем фрейме рядом с «Аудит». По клику — вставить в `#info-panel` два `iframe` с беседами `conv_a` и `conv_b`. Повторный клик — убрать iframe и вернуть прежний текст панели.

`index.html` **не переписывать как страницу**. `chat.js` не трогать. `chat-log` не трогать. Отдельную `test_seats.html` не делать.

---

## FILES

```
EDIT:    E:\Gemini\Dojo\AI-Collab\fixture_server.py
         (добавить ?format=html для /conv_a и /conv_b)

EDIT:    E:\Gemini\Dojo\AI-Collab\templates\index.html
         (только: одна кнопка + один script-блок)

CREATE:  E:\Gemini\Dojo\AI-Collab\static\seats_test.js
         (обработчик кнопки)

CREATE:  E:\Gemini\Dojo\AI-Collab\serve_interface.py
         (локальный HTTP-сервер для templates, chat.js, PNG)

DO NOT TOUCH:
  E:\Gemini\Dojo\AI-Collab\static\chat.js
  E:\Gemini\Dojo\AI-Collab\seats.json
  E:\Gemini\Dojo\AI-Collab\truth.json
  E:\Gemini\AI-Colab\
  E:\Gemini\Dojo\Manuscript_Press\
  профиль Автора
```

---

## DO NOT

```
❌ Не переписывать index.html как страницу.
❌ Не трогать chat.js.
❌ Не трогать chat-log.
❌ Не делать test_seats.html.
❌ Не вставлять iframe в chat-log.
❌ Не менять вёрстку, кнопки, панели, цвета, меню.
❌ Не запускать Edge.
❌ Не запускать Playwright / Selenium.
❌ Не трогать E:\Gemini\AI-Colab\.
❌ Не создавать profiles/.
```

---

## PART 1 — fixture_server.py: HTML-вид беседы

**Добавить** обработку query-параметра `format=html` для `/conv_a` и `/conv_b`.

**Логика:**

- `GET /conv_a` → JSON (как сейчас, без изменений).
- `GET /conv_a?format=html` → HTML-страница с сообщениями.
- `GET /conv_b` → JSON (как сейчас).
- `GET /conv_b?format=html` → HTML-страница с сообщениями.

**HTML-вид:**

```html
<!doctype html>
<html lang="ru">
<head>
  <meta charset="UTF-8">
  <title>conv_a</title>
  <style>
    body { font-family: sans-serif; padding: 12px; font-size: 13px; background: #fff; }
    .conv-header { font-weight: bold; margin-bottom: 10px; color: #2c3e50; }
    .msg { margin-bottom: 8px; padding: 6px 8px; border-radius: 4px; }
    .msg.user { background: #e3f2fd; }
    .msg.assistant { background: #f5f5f5; }
    .msg .role { font-size: 11px; color: #7f8c8d; margin-bottom: 2px; }
    .msg .content { white-space: pre-wrap; }
  </style>
</head>
<body>
  <div class="conv-header">conv_a</div>
  <div class="msg user">
    <div class="role">user</div>
    <div class="content">A-user-1</div>
  </div>
  ...
</body>
</html>
```

**Требования:**

- Сообщения читаемы.
- При `switch_conv_a_to_b == true` `/conv_a?format=html` показывает `conv_b`.
- JSON-версия **не меняется**.
- `--self-test` продолжает проходить.

---

## PART 2 — index.html: одна кнопка + один script

### 2a. В верхнем фрейме, рядом с «Аудит»

**Было** (фрагмент):

```html
<div class="top-left-group">
  <button class="role-btn-top gemini-top">></button>
  <button class="role-btn-top gemini-top">Аудит</button>
  <button class="role-btn-top chief-top">ШЕФ</button>
</div>
```

**Стало:**

```html
<div class="top-left-group">
  <button class="role-btn-top gemini-top">></button>
  <button class="role-btn-top gemini-top">Аудит</button>
  <button class="role-btn-top" id="seatsTestBtn">Тест кресел</button>
  <button class="role-btn-top chief-top">ШЕФ</button>
</div>
```

**Требование:** только эта одна строка `button` добавлена. Ничего больше в верхнем фрейме не менять.

### 2b. В конце `index.html`, перед `</body>`

**Было:**

```html
    <script src="chat.js"></script>
  </body>
</html>
```

**Стало:**

```html
    <script src="chat.js"></script>
    <script src="seats_test.js"></script>
  </body>
</html>
```

**Требование:** только одна строка `<script src="seats_test.js"></script>` добавлена. `chat.js` остаётся.

---

## PART 3 — static/seats_test.js

**Создать** `E:\Gemini\Dojo\AI-Collab\static\seats_test.js`.

**Логика:**

```javascript
(function () {
  var active = false;
  var originalHTML = null;

  function toggleSeats() {
    var panel = document.getElementById('info-panel');
    if (!panel) return;

    if (!active) {
      originalHTML = panel.innerHTML;
      panel.innerHTML =
        '<div style="display:flex;gap:6px;height:100%;">' +
          '<iframe src="http://127.0.0.1:5999/conv_a?format=html" ' +
            'style="flex:1;border:1px solid #ddd;border-radius:3px;"></iframe>' +
          '<iframe src="http://127.0.0.1:5999/conv_b?format=html" ' +
            'style="flex:1;border:1px solid #ddd;border-radius:3px;"></iframe>' +
        '</div>';
      active = true;
    } else {
      if (originalHTML !== null) {
        panel.innerHTML = originalHTML;
      }
      active = false;
    }
  }

  window.addEventListener('DOMContentLoaded', function () {
    var btn = document.getElementById('seatsTestBtn');
    if (btn) btn.addEventListener('click', toggleSeats);
  });
})();
```

**Требования:**

- При клике — вставить два iframe в `#info-panel`.
- Сохранить исходное содержимое `#info-panel` при первом клике.
- Повторный клик — вернуть исходное содержимое.
- Не трогать другие элементы страницы.
- Не трогать `chat.js`.

---

## PART 4 — serve_interface.py

**Создать** `E:\Gemini\Dojo\AI-Collab\serve_interface.py`.

**Логика:**

- Python 3, stdlib only.
- Bind `127.0.0.1:8000`.
- Отдавать файлы из `E:\Gemini\Dojo\AI-Collab\`.

**Маршруты:**

```
GET /              → templates/index.html
GET /chat.js       → static/chat.js
GET /seats_test.js → static/seats_test.js
GET /A.png         → templates/A.png
GET /B.png         → templates/B.png
GET /C.png         → templates/C.png
GET /D.png         → templates/D.png
Прочее             → 404
```

**Порт 8000:** если занят — STOP, не подбирать другой.

---

## LOCAL VERIFY

**Шаг 1.** Fixture на 5999 (из STEP 1). Если нет — запустить.

**Шаг 2.** Проверить HTML-вид:

```
GET http://127.0.0.1:5999/conv_a?format=html → HTML, не JSON
GET http://127.0.0.1:5999/conv_b?format=html → HTML, не JSON
```

**Шаг 3.** Запустить `serve_interface.py`:

```powershell
cd E:\Gemini\Dojo\AI-Collab
python serve_interface.py
```

**Шаг 4.** Проверить маршруты через встроенный `urllib.request` (curl может быть недоступен в среде Самурая):

```python
python -c "import urllib.request; print(urllib.request.urlopen('http://127.0.0.1:8000/').read()[:100])"
python -c "import urllib.request; print(urllib.request.urlopen('http://127.0.0.1:8000/chat.js').read()[:50])"
python -c "import urllib.request; print(urllib.request.urlopen('http://127.0.0.1:8000/seats_test.js').read()[:50])"
python -c "import urllib.request; print(urllib.request.urlopen('http://127.0.0.1:8000/A.png').read()[:10])"
```

**Шаг 5.** Автор открывает `http://127.0.0.1:8000/`:

- видит свой интерфейс **без изменений**,
- жмёт «Тест кресел» — в `#info-panel` появляются два iframe с беседами,
- жмёт повторно — iframe исчезают, текст панели возвращается.

---

## REPORT

```yaml
BUILD_001_STEP_3B_REPORT:
  files_modified:
    - E:\Gemini\Dojo\AI-Collab\fixture_server.py
    - E:\Gemini\Dojo\AI-Collab\templates\index.html
  files_created:
    - E:\Gemini\Dojo\AI-Collab\static\seats_test.js
    - E:\Gemini\Dojo\AI-Collab\serve_interface.py

  fixture_server:
    html_format_added: yes/no
    json_unchanged: yes/no
    self_test_still_passes: yes/no

  index_html:
    one_button_added: yes/no
    one_script_tag_added: yes/no
    chat_js_untouched: yes/no
    chat_log_untouched: yes/no
    layout_untouched: yes/no
    only_those_two_changes: yes/no

  seats_test_js:
    path: E:\Gemini\Dojo\AI-Collab\static\seats_test.js
    toggles_iframes: yes/no
    restores_original: yes/no

  serve_interface:
    path: E:\Gemini\Dojo\AI-Collab\serve_interface.py
    port: 8000
    serves_index: yes/no
    serves_chat_js: yes/no
    serves_seats_test_js: yes/no
    serves_png: yes/no

  author_verify:
    url: http://127.0.0.1:8000/
    visible: yes/no
    button_present: yes/no
    click_shows_two_conversations: yes/no
    second_click_restores: yes/no

  verification_method: urllib.request (curl may be unavailable)

  forbidden_checks:
    no_chat_js_edit: yes
    no_chat_log_edit: yes
    no_test_seats_html: yes
    no_index_rewrite: yes
    no_edge: yes
    no_playwright: yes
    no_old_ai_colab: yes
    no_profiles: yes

  next: STOP → WAIT_FOR_SENSEI
```

---

## NON-GOALS

```
❌ переписывание index.html как страницы
❌ изменение chat.js
❌ изменение chat-log
❌ test_seats.html
❌ iframe в chat-log
❌ Edge
❌ Playwright / Selenium
❌ E:\Gemini\AI-Colab\
❌ profiles/
```

---

## STOP CONDITIONS

```
Если порт 8000 занят → STOP.
Если fixture на 5999 не отвечает → STOP.
Если chat.js изменён → STOP.
Если в index.html добавлено больше одной кнопки и одного script → STOP.
Если test_seats.html создан → STOP.
```

---

## END PROTOCOL

```
EDIT fixture_server.py (?format=html)
→ EDIT index.html (one button + one script tag)
→ CREATE static/seats_test.js
→ CREATE serve_interface.py
→ VERIFY via urllib.request
→ AUTHOR OPENS http://127.0.0.1:8000/ and clicks button
→ REPORT → STOP
```

---

```yaml
BRIGADIER_STATUS:
  build: 001
  step: 3b
  version: 2.0
  route: option_3 (Grok approved)
  index_html: preserved, only one button + one script tag
  chat_js: untouched
  next: SHOGUN_DELIVERS_TO_SAMURAI
  stop: true
```

---
STOP.