
🎌 СЕНСЕЙ DEEPSEEK: СПЕК — ФИНАЛИЗАЦИЯ 01_T00_VERIFY

Grok, Доктор, принято. Выбираем Вариант B. Финализируем 01_T00_VERIFY как рабочий результат Manuscript Writer.
📋 СПЕК — ФИНАЛИЗАЦИЯ 01_T00_VERIFY
ЦЕЛЬ

STEP:
FINALIZE 01_T00_VERIFY

REQUIRED_MODE:
IMPLEMENTER

Подтвердить, что 01_T00_VERIFY является полным и согласованным production run, и объявить его рабочим результатом Manuscript Writer.
🔍 ШАГ 1: ПРОВЕРКА АРТЕФАКТОВ 01_T00_VERIFY

Проверить, что в logs/runs/01_T00_VERIFY/ существуют:

    □

    raw_output.md — не пуст, содержит полный CONSTANTS CHECK блок.
    □

    metadata.yaml — содержит status: SUCCESS, constants_check: ALL_YES, manuscript_created: true.
    □

    constants_check.yaml — отсутствует или пуст. Если отсутствует — создать из raw_output.md.

🔧 ШАГ 2: СОЗДАНИЕ CONSTANTS_CHECK.YAML (ЕСЛИ ОТСУТСТВУЕТ)

Если constants_check.yaml отсутствует, создать его на основе raw_output.md:
python

import yaml
from src.generator import parse_constants_check

with open("logs/runs/01_T00_VERIFY/raw_output.md", 'r') as f:
    raw = f.read()

status, details = parse_constants_check(raw)

with open("logs/runs/01_T00_VERIFY/constants_check.yaml", 'w') as f:
    yaml.dump({"status": status, "items": details}, f)

Если constants_check.yaml отсутствует ИЛИ существует, но имеет размер 0 байт,
создать/заменить его исключительно на основании
logs/runs/01_T00_VERIFY/raw_output.md
через существующий parse_constants_check().

Если constants_check.yaml уже непустой, но его содержимое противоречит
raw_output.md:
STOP → REPORT → QUERY SENSEI.
Не исправлять противоречие автоматически.

✅ ШАГ 3: ПРОВЕРКА MANUSCRIPT

    □

    Output/01_T00_VERIFY.manuscript.md — существует, не пуст.
    □

    SHA-256 соответствует записи в metadata.yaml.

📝 ШАГ 4: ФИНАЛЬНЫЙ ОТЧЁТ
yaml

Step: Finalize 01_T00_VERIFY
Mode_Observed: IMPLEMENTER
Execution: PASS / FAIL
Evidence: VERIFIED / INCOMPLETE / CONTRADICTED
Artifacts:
  raw_output.md: exists / not exists
  metadata.yaml:
    exists: yes / no
    status: SUCCESS / FAILED / other
    constants_check: ALL_YES / HAS_NO / NOT_FOUND
    manuscript_created: true / false
  constants_check.yaml:
    exists: yes / no
    source: 01_T00_VERIFY/raw_output.md
    status: ALL_YES / HAS_NO / NOT_FOUND
    items: N
  manuscript.md:
    exists: yes / no
    non_empty: yes / no
    sha256_matches_metadata: yes / no
Health: OK / DEGRADED
Next: WAIT / QUERY SENSEI

Самурай, выполни проверку и создание constants_check.yaml для 01_T00_VERIFY. После этого объявляем Manuscript Writer рабочим. 🎌
