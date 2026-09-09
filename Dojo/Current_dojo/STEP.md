STEP — PHASE C2: TYPE FIX FOR GENERATION KNOBS

Статус: ACTIVE
PHASE C2 — READ-ONLY LOCALIZATION (ОБЯЗАТЕЛЬНА ПЕРВОЙ)
1. Найти точные значения и типы в момент вызова

В src/continuity_cache_bench.py найти:

    Где загружается writer_config.yaml

    Какие значения из него читаются для max_tokens, temperature, top_p

    Какие типы имеют эти значения после загрузки

    Какие значения передаются в create_chat_completion как именованные аргументы

    Если используется переменная/подстановка со значением "N/A" — где она возникает

2. Отчёт по READ-ONLY
yaml

C2_READONLY_REPORT:
  config_loaded_from: config/writer_config.yaml
  max_tokens:
    raw_value: <значение из YAML>
    raw_type: <str / int / float>
    passed_to_completion: <значение>
    passed_type: <str / int / float>
  temperature:
    raw_value: <значение из YAML>
    raw_type: <str / int / float>
    passed_to_completion: <значение>
    passed_type: <str / int / float>
  top_p:
    raw_value: <значение из YAML>
    raw_type: <str / int / float>
    passed_to_completion: <значение>
    passed_type: <str / int / float>
  origin_of_N/A_if_present: <откуда берётся>
  root_cause_hypothesis: <одно предложение>
  fix_required: <да / нет>

STOP после отчёта.
PHASE C2 — MINIMAL FIX (ТОЛЬКО ПОСЛЕ READ-ONLY)
Принцип исправления

    max_tokens → int(...)

    temperature → float(...)

    top_p → float(...)

Брать значения только из writer_config.yaml generation.* (уже known working pattern из smoke_bridge.py / generator.py).

Запрещено:

    Подстановка "N/A" или любых строк в kwargs create_chat_completion.

    Менять parsers, CACHE semantics, marker extraction, loader.py, encoding.

    Менять writer_config.yaml.

    Добавлять новую логику.

Файл для исправления

Только: src/continuity_cache_bench.py
Ожидаемый паттерн (пример)
python

# До (если так):
max_tokens = config["generation"].get("max_tokens", "N/A")
temperature = config["generation"].get("temperature", "N/A")
top_p = config["generation"].get("top_p", "N/A")

# После:
max_tokens = int(config["generation"].get("max_tokens", 2048))
temperature = float(config["generation"].get("temperature", 0.0))
top_p = float(config["generation"].get("top_p", 0.9))

Отчёт по FIX
yaml

C2_FIX_REPORT:
  files_modified:
    - src/continuity_cache_bench.py
  changes:
    - max_tokens: <было> → <стало>
    - temperature: <было> → <стало>
    - top_p: <было> → <стало>
  removal_of_N/A: <да / нет>
  preflight_after_fix: PASS / FAIL (read-only проверка синтаксиса)
  next: WAIT_FOR_GREEN_LIGHT_C3

STOP