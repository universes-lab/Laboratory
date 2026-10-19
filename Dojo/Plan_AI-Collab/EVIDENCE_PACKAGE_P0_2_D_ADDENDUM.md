# EVIDENCE_PACKAGE_P0_2_D_ADDENDUM

STATUS: DOCUMENT/CODE_READ, RUNTIME_UNVERIFIED · 2026-10-19 · Developer Claude
ПОВОД: независимая проверка Grok (раздел 4) не нашла дословных фрагментов для F-1 и F-11 в пакетах A/B/C и не нашла F-7/F-27 там, где искала. Ниже — дословные строки и указатели на уже существующие фрагменты.
REVISION HF: UNKNOWN (не изменилось). Паспорта файлов — из P0.1 (SHA-256 по HF-чтению).

## Указатели на уже имеющиеся фрагменты (новые данные не добавляются)
- **F-7** `create_subprocess_shell`: `EVIDENCE_PACKAGE_P0_2_A.md`, файл `core/llm_integrations/gcb_engine.py`, строка 87 файла (в пакете A это строка 481 документа). Поиск был в пакете B, где этого файла нет.
- **F-27** `stop=['<|end|>', '<|user|>', '\n\n']`, `max_tokens` 512: `EVIDENCE_PACKAGE_P0_2_B.md`, файл `integrations/gptoss_adapter.py`, строки 105–114 (в документе — около строки 1240–1249). Не в пакете C. Файл читался выборочно (skim), в паспорте пакета B это отмечено.

## Новые дословные фрагменты

### app3.py — паспорт: 36063 B, 757 строк, SHA-256 659977fe9847bc81… (P0.1: STATIC_ANALYZED)
Импорт (F-1), строки 18–26:
```
  18|     from core.prompt_registry import PromptRegistry
  19|     from core.model_management import ModelManager
  20|     from core.role_binding_manager import RoleBindingManager
  21|     from core.gemini_cli_executor import execute
  22|     from core.project_context import ProjectContext, get_current_project_path
  23|     from core.chat_storage import get_chat_storage
  24|     from doctor_ws_module import register_doctor_ws
  25|     # from core.agent_orchestrator import launch_agents, terminate_agents
  26| 
```
Запуск (F-2), строки 725–736:
```
 725|         #     logger.warning("⚠️ Some agents failed to start — system may be partially functional")
 726| 
 727|         # 2. Запуск сервера
 728|         try:
 729|             import uvicorn
 730|             uvicorn.run(
 731|                 "app2:app",
 732|                 host=host,
 733|                 port=port,
 734|                 log_level="info"
 735|             )
 736|         except KeyboardInterrupt:
```

Источник хоста и порта (используется в ответе Grok и DeepSeek), строки 709–720:
```
 709|         import sys
 710|         import logging
 711|         from core.config_loader import load_gemini_sockets
 712| 
 713|         logger = logging.getLogger(__name__)
 714| 
 715|         # 1. Загрузка конфигурации и запуск агентов
 716|         config = load_gemini_sockets()
 717|         main_cfg = config.get("main_server", {})
 718|         host = main_cfg.get("host", "127.0.0.1")
 719|         port = main_cfg.get("port", 5005)
 720| 
```

### app.py — паспорт: 30238 B, 646 строк (по `wc -l`; последняя строка без завершающего перевода), SHA-256 81a2e0342eba7bbb… (P0.1: STATIC_ANALYZED)
Запуск (F-11), строки 644–647:
```
 644| # ============================================================================
 645| 
 646| if __name__ == '__main__':
 647|     app.run(debug=True, host='0.0.0.0', port=5000)
```

### core/project_context.py (для F-1)
Уже в пакете A: `def get_current_project_path(self):` на строке 48 — метод класса; функции уровня модуля в прочитанном файле нет.

## Что это подтверждает и что нет
- F-1: `app3.py` L22 импортирует имя `get_current_project_path` из `core.project_context`; в файле project_context.py оно определено только как метод класса (L48). Вывод «ожидается ImportError» — **статический**; рантайм не проверялся.
- F-2: `uvicorn.run("app2:app", …)` в app3.py — подтверждено строками выше.
- F-11: `app.run(debug=True, host='0.0.0.0', port=5000)` — подтверждено строкой выше.
- Ограничение: фрагменты взяты из моих рабочих копий (`src/`), полученных чтением HF; совпадение размера и хэша с паспортами P0.1 проверено для app.py и app3.py.
