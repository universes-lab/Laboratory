# EVIDENCE PACKAGE P0.2-B (P1-файлы) для DEVELOPER DEEPSEEK
Источник: HF dataset lhc-lab/AI-Colab, REVISION UNKNOWN, MODE VERBATIM, TRUNCATED false для всех; size совпадает с HF stat. Нумерация строк добавлена, в хэш не входит. Ничего не запускалось: RUNTIME_UNVERIFIED. Секретов в файлах нет (api_key читается из env; значений нет).



## SOURCE_EVIDENCE: core/model_management.py
```
REPOSITORY: lhc-lab/AI-Colab
SOURCE: HF_DATASET
REVISION: UNKNOWN
FILE: core/model_management.py
CONTENT_SHA256: 7823dfba8d671b1e039d114e9cbd54c1d4124fefca00a3c979d03af9183d8bbb
BYTES: 6454
LINES: 131
MODE: VERBATIM
TRUNCATED: false
EVIDENCE_LEVEL: CODE_READ
```
```text
   1| import json
   2| import logging
   3| import asyncio
   4| from typing import Dict, Optional, Any
   5| import os
   6| from pathlib import Path
   7| 
   8| 
   9| logger = logging.getLogger() # Используем корневой логгер
  10| 
  11| class ModelManager:
  12|     _instance = None
  13|     _generate_lock = asyncio.Lock() # Глобальная блокировка генерации
  14|     
  15|     def __new__(cls):
  16|         if cls._instance is None:
  17|             cls._instance = super().__new__(cls)
  18|         return cls._instance
  19|     
  20|     def __init__(self, *args, **kwargs):
  21|         if not hasattr(self, '_initialized'):
  22|             self._initialized = False
  23|             self._models = {}
  24|             # Глобальный конфиг AIColab (Источник Истины)
  25|             # Путь: AIColab/core/ -> .. -> AIColab/config/models_config.json
  26|             self._config_path = Path(__file__).parent.parent.resolve() / "config" / "models_config.json"
  27|             self._config = None # Будет загружен в _ensure_initialized
  28|             self._current_model = None
  29|             logger.info("ModelManager создан. Целевой конфиг: %s", self._config_path)
  30|     
  31|     async def _ensure_initialized(self):
  32|         """Ленивая инициализация. Всегда перезагружает конфиг для актуальности."""
  33|         await self._load_config() # Всегда загружаем конфиг, чтобы быть актуальным
  34|         if not self._initialized:
  35|             self._initialized = True
  36|             logger.info("ModelManager инициализирован")
  37|     
  38|     async def _load_config(self):
  39|         """Загрузка конфигурации моделей (Источник Истины: AIColab/config)."""
  40|         config_path = self._config_path # Используем путь, заданный в __init__
  41| 
  42|         if config_path.exists():
  43|             try:
  44|                 with open(config_path, 'r', encoding='utf-8') as f:
  45|                     self._config = json.load(f)
  46|                 logger.info(f"Загружен конфиг с {len(self._config.get('active_models', {}))} моделями из {config_path}")
  47|             except Exception as e:
  48|                 logger.error(f"Ошибка парсинга JSON конфига: {e}")
  49|                 self._config = {"active_models": {}, "model_providers": {}}
  50|         else:
  51|             logger.error(f"Конфиг НЕ найден по пути: {config_path}")
  52|             self._config = {"active_models": {}, "model_providers": {}}
  53| 
  54|     async def _load_system_prompt(self, prompt_filename: str) -> str:
  55|         from core.shared_state import get_shared_state
  56|         
  57|         state = get_shared_state()
  58|         project_path = Path(state.get("current_project_path", "."))
  59|         
  60|         project_file = project_path / "prompts" / prompt_filename
  61|         if project_file.exists():
  62|             logger.info(f"Prompt loaded from project: {project_file}")
  63|             return project_file.read_text(encoding="utf-8")
  64|         
  65|         repo_root = Path(__file__).parent.parent
  66|         global_file = repo_root / "docs" / "prompts" / prompt_filename
  67|         if global_file.exists():
  68|             logger.info(f"Prompt loaded from global: {global_file}")
  69|             return global_file.read_text(encoding="utf-8")
  70|         
  71|         logger.warning(f"Prompt file NOT FOUND: {prompt_filename}")
  72|         return ""
  73| 
  74| 
  75|     async def _load_local_model(self, model_config: Dict, provider_config: Dict):
  76|         from integrations.gptoss_adapter import GptOssModel
  77|         model = GptOssModel(model_config)
  78|         return model
  79| 
  80|     async def _load_openrouter_adapter(self, model_config: Dict, provider_config: Dict):
  81|         from integrations.openrouter_adapter import OpenRouterModel
  82|         model = OpenRouterModel(model_config)
  83|         return model
  84| 
  85|     async def get_model(self, key: str) -> Any:
  86|         """Получить экземпляр модели по ключу или полному ID."""
  87|         if not self._config:
  88|             await self._load_config()
  89| 
  90|         # 1. Сначала ищем в active_models (по ключу: flick, ceo и т.д.)
  91|         for model_cfg in self._config.get('active_models', []):
  92|             if isinstance(model_cfg, dict) and model_cfg.get('key') == key:
  93|                 if model_cfg.get('provider') == 'gptoss':
  94|                     return await self._load_local_model(model_cfg, {})
  95|                 else:
  96|                     return await self._load_openrouter_adapter(model_cfg, {})
  97| 
  98|         # 2. Затем ищем в available_openrouter_models (по полному ID)
  99|         pool = self._config.get('available_openrouter_models', [])
 100|         if key in pool:
 101|             return await self._load_openrouter_adapter({"key": key, "model_id": key}, {})
 102|         
 103|         # 3. Крайний случай: если это Staff-модель (полный ID), но её нет в пуле
 104|         # Мы всё равно пытаемся её вызвать, чтобы не блокировать работу
 105|         if "/" in key:
 106|             logger.warning(f"[MODEL_MANAGER] Model {key} not in pool, but looks like ID. Attempting direct call.")
 107|             return await self._load_openrouter_adapter({"key": key, "model_id": key}, {})
 108| 
 109|         raise ValueError(f"Модель '{key}' не найдена в конфигурации")
 110|     def set_binding_manager(self, role_binding_manager):
 111|         """Устанавливает менеджер привязок для возможности инвалидации кэша."""
 112|         self.role_binding_manager = role_binding_manager
 113|         logger.info("ModelManager: BindingManager установлен")
 114| 
 115|     async def unload_current_model(self):
 116|         """Очистить кэш всех моделей (ручной сброс)"""
 117|         for key, model in self._models.items():
 118|             if hasattr(model, 'unload_model'):
 119|                 if asyncio.iscoroutinefunction(model.unload_model):
 120|                     await model.unload_model()
 121|                 else:
 122|                     model.unload_model()
 123|         self._models.clear()
 124|         import gc
 125|         gc.collect()
 126| 
 127|     def invalidate_model(self, key: str):
 128|         """Удалить модель из кэша по ключу роли"""
 129|         if key in self._models:
 130|             logger.info(f"Инвалидация модели для роли: {key}")
 131|             del self._models[key]
```


## SOURCE_EVIDENCE: core/prompt_registry.py
```
REPOSITORY: lhc-lab/AI-Colab
SOURCE: HF_DATASET
REVISION: UNKNOWN
FILE: core/prompt_registry.py
CONTENT_SHA256: 3efc9937ab937de87d7e0d4166f70febbd0b623d1fb866b52dd09a93983f9c7f
BYTES: 3992
LINES: 83
MODE: VERBATIM
TRUNCATED: false
EVIDENCE_LEVEL: CODE_READ
```
```text
   1| from pathlib import Path
   2| from core.shared_state import get_shared_state
   3| import logging
   4| 
   5| logger = logging.getLogger(__name__)
   6| 
   7| class PromptRegistry:
   8|     """
   9|     Реестр системных промптов для всех ролей.
  10|     Реализует иерархическую загрузку: PROJECT -> GLOBAL.
  11|     """
  12|     def __init__(self):
  13|         state = get_shared_state()
  14|         self.project_path = Path(state.get("current_project_path", "."))
  15|         # Корень репозитория относительно AIColab/core/
  16|         self.repo_root = Path(__file__).parent.parent.parent # Относительно D:\gemini\AIColab
  17|         
  18|         # Маппер ролей к путям (относительно папки prompts/)
  19|         self.role_map = {
  20|             "flick": "department_A/flick.txt",
  21|             "flock": "department_A/flock.txt",
  22|             "click": "department_B/click.txt",
  23|             "clack": "department_B/clack.txt",
  24|             "check": "department_C/check.txt",
  25|             "chock": "department_C/chock.txt",
  26|             "link": "department_D/link.txt",
  27|             "sync": "department_D/sync.txt",
  28|             "ceo": "core/ceo.txt",
  29|             "chief": "core/chief.txt",
  30|             "gemini_console": "Gemini/gemini_console.txt",
  31|             "secretary_chief": "Gemini/gemini_secretary_chief.txt",
  32|             "secretary_ceo": "Gemini/gemini_secretary_ceo.txt",
  33|             "strategic_orchestrator": "Gemini/gemini_strategic_orchestrator.txt",
  34|             "audit_orchestrator": "Gemini/gemini_audit_orchestrator.txt",
  35|             "admin_console": "Gemini/gemini_console.txt",
  36|             "admin_secretary": "Gemini/gemini_secretary_chief.txt",
  37|             "admin_auditor": "Gemini/gemini_audit_orchestrator.txt",
  38|             "secretary": "Gemini/gemini_secretary_chief.txt", # Default for generic 'secretary' requests
  39|             "consultant_strategic": "department_E/consultant_strategic.txt",
  40|             "consultant_medical": "department_F/consultant_medical.txt",
  41|         }
  42|         self.cache = {}
  43|         logger.info(f"PromptRegistry initialized. Project path: {self.project_path}. Repo root: {self.repo_root}")
  44| 
  45|     def get_prompt(self, role_key: str) -> str:
  46|         """Возвращает системный промпт для указанной роли."""
  47|         if role_key in self.cache:
  48|             return self.cache[role_key]
  49|         
  50|         rel_path = self.role_map.get(role_key)
  51|         if not rel_path:
  52|             logger.error(f"Unknown role: {role_key}")
  53|             return ""
  54|         
  55|         # 1. Попытка загрузить из проекта
  56|         project_file = self.project_path / "prompts" / rel_path
  57|         if project_file.exists():
  58|             try:
  59|                 content = project_file.read_text(encoding="utf-8")
  60|                 self.cache[role_key] = content
  61|                 logger.info(f"PROMPT LOAD: {role_key} -> {project_file} (PROJECT) FOUND: YES")
  62|                 return content
  63|             except Exception as e:
  64|                 logger.error(f"Error reading project prompt {project_file}: {e}")
  65|         
  66|         # 2. Fallback на глобальный репозиторий (docs/prompts/)
  67|         global_file = self.repo_root / "docs" / "prompts" / rel_path
  68|         if global_file.exists():
  69|             try:
  70|                 content = global_file.read_text(encoding="utf-8")
  71|                 self.cache[role_key] = content
  72|                 logger.info(f"PROMPT LOAD: {role_key} -> {global_file} (GLOBAL) FOUND: YES")
  73|                 return content
  74|             except Exception as e:
  75|                 logger.error(f"Error reading global prompt {global_file}: {e}")
  76|         
  77|         logger.error(f"PROMPT NOT FOUND: {role_key} (checked project and global)")
  78|         return ""
  79| 
  80|     def clear_cache(self):
  81|         """Сброс кэша для горячей перезагрузки промптов."""
  82|         self.cache.clear()
  83|         logger.info("PromptRegistry cache cleared")
```


## SOURCE_EVIDENCE: core/shared_state.py
```
REPOSITORY: lhc-lab/AI-Colab
SOURCE: HF_DATASET
REVISION: UNKNOWN
FILE: core/shared_state.py
CONTENT_SHA256: 6369696f228dba650970f00b0579bbed7161418d4466d9ba0ef4066145cd877b
BYTES: 7757
LINES: 191
MODE: VERBATIM
TRUNCATED: false
EVIDENCE_LEVEL: CODE_READ
```
```text
   1| from __future__ import annotations
   2| 
   3| import json
   4| import os
   5| import time
   6| from pathlib import Path
   7| from typing import Any, Dict, Optional
   8| import platform
   9| import logging
  10| 
  11| logger = logging.getLogger(__name__)
  12| 
  13| # Межпроцессная блокировка в зависимости от ОС
  14| if platform.system() == 'Windows':
  15|     import msvcrt
  16| else:
  17|     import fcntl
  18| 
  19| class SharedState:
  20|     """
  21|     Класс для управления общим состоянием приложения между процессами (Uvicorn workers).
  22|     Использует файл JSON и файловые блокировки для синхронизации.
  23|     """
  24|     def __init__(self, file_path: str = "shared_state.json"):
  25|         # Путь относительно корня проекта (D:\gemini\AIColab)
  26|         # Если запускается из корня, то просто shared_state.json
  27|         self.file_path = Path(file_path)
  28|         self._state: Dict[str, Any] = {}
  29|         self._file_mtime: float = 0
  30|         self._lock_file = None
  31|         
  32|         # Инициализируем файл, если его нет
  33|         if not self.file_path.exists():
  34|             self._save_init_state()
  35|         
  36|         self._load_state()
  37| 
  38|     def _save_init_state(self):
  39|         """Создает начальный пустой файл состояния."""
  40|         try:
  41|             with open(self.file_path, 'w', encoding='utf-8') as f:
  42|                 json.dump({}, f)
  43|         except Exception as e:
  44|             logger.error(f"Failed to initialize shared_state.json: {e}")
  45| 
  46|     def _load_state(self, external_file=None):
  47|         """Загружает состояние из файла. Если передан external_file, использует его."""
  48|         try:
  49|             if external_file:
  50|                 external_file.seek(0)
  51|                 content = external_file.read()
  52|                 if content:
  53|                     self._state = json.loads(content)
  54|                 return
  55| 
  56|             if self.file_path.exists():
  57|                 current_mtime = self.file_path.stat().st_mtime
  58|                 if current_mtime > self._file_mtime:
  59|                     with open(self.file_path, 'r', encoding='utf-8') as f:
  60|                         content = f.read()
  61|                         if content:
  62|                             self._state = json.loads(content)
  63|                         else:
  64|                             self._state = {}
  65|                     self._file_mtime = current_mtime
  66|         except Exception as e:
  67|             logger.warning(f"Error loading shared state: {e}")
  68| 
  69|     def _save_state(self, external_file=None):
  70|         """Сохраняет состояние в файл. Если передан external_file, использует его."""
  71|         try:
  72|             if external_file:
  73|                 external_file.seek(0)
  74|                 external_file.truncate()
  75|                 json.dump(self._state, external_file, indent=2, ensure_ascii=False)
  76|                 external_file.flush()
  77|                 return
  78| 
  79|             with open(self.file_path, 'w', encoding='utf-8') as f:
  80|                 json.dump(self._state, f, indent=2, ensure_ascii=False)
  81|             self._file_mtime = self.file_path.stat().st_mtime
  82|         except Exception as e:
  83|             logger.error(f"Error saving shared state: {e}")
  84| 
  85|     def get(self, key: str, default: Any = None) -> Any:
  86|         """Получает значение по ключу, предварительно обновляя состояние из файла."""
  87|         self._load_state()
  88|         return self._state.get(key, default)
  89| 
  90|     def get_all(self) -> Dict[str, Any]:
  91|         """Возвращает всё состояние."""
  92|         self._load_state()
  93|         return self._state.copy()
  94| 
  95|     def set(self, key: str, value: Any) -> bool:
  96|         """Устанавливает значение и сохраняет в файл с блокировкой. Поддерживает вложенность через точку."""
  97|         self.lock() # lock() opens self._lock_file
  98|         try:
  99|             self._load_state(external_file=self._lock_file)
 100|             
 101|             if "." in key:
 102|                 parts = key.split(".")
 103|                 current = self._state
 104|                 for part in parts[:-1]:
 105|                     if part not in current or not isinstance(current[part], dict):
 106|                         current[part] = {}
 107|                     current = current[part]
 108|                 current[parts[-1]] = value
 109|             else:
 110|                 self._state[key] = value
 111|                 
 112|             self._save_state(external_file=self._lock_file)
 113|             return True
 114|         except Exception as e:
 115|             logger.error(f"Error in SharedState.set: {e}")
 116|             return False
 117|         finally:
 118|             self.unlock()
 119| 
 120|     def update(self, data: Dict[str, Any]):
 121|         """Обновляет несколько значений сразу."""
 122|         self.lock()
 123|         try:
 124|             self._load_state(external_file=self._lock_file)
 125|             self._state.update(data)
 126|             self._save_state(external_file=self._lock_file)
 127|         finally:
 128|             self.unlock()
 129| 
 130|     def lock(self):
 131|         """Блокирует файл для исключительного доступа."""
 132|         try:
 133|             if platform.system() == 'Windows':
 134|                 # На Windows открываем файл для чтения/записи
 135|                 self._lock_file = open(self.file_path, 'r+')
 136|                 # Блокируем первый байт файла
 137|                 msvcrt.locking(self._lock_file.fileno(), msvcrt.LK_LOCK, 1)
 138|             else:
 139|                 # Unix
 140|                 self._lock_file = open(self.file_path, 'r+')
 141|                 fcntl.flock(self._lock_file.fileno(), fcntl.LOCK_EX)
 142|         except Exception as e:
 143|             logger.error(f"Locking failed: {e}")
 144| 
 145|     def unlock(self):
 146|         """Разблокирует файл."""
 147|         try:
 148|             if self._lock_file:
 149|                 if platform.system() == 'Windows':
 150|                     self._lock_file.seek(0)
 151|                     msvcrt.locking(self._lock_file.fileno(), msvcrt.LK_UNLCK, 1)
 152|                 else:
 153|                     fcntl.flock(self._lock_file.fileno(), fcntl.LOCK_UN)
 154|                 self._lock_file.close()
 155|                 self._lock_file = None
 156|         except Exception as e:
 157|             logger.error(f"Unlocking failed: {e}")
 158| 
 159|     def validate_project_state(self) -> Dict[str, Any]:
 160|         """Валидация целостности состояния текущего проекта."""
 161|         self._load_state()
 162|         current_path = self._state.get("current_project_path")
 163|         if not current_path:
 164|             return {"valid": False, "error": "No project selected"}
 165|         
 166|         project_dir = Path(current_path)
 167|         if not project_dir.exists():
 168|             return {"valid": False, "error": f"Project directory missing: {current_path}"}
 169|         
 170|         info_file = project_dir / "project_info.json"
 171|         if not info_file.exists():
 172|             return {"valid": False, "error": "project_info.json missing"}
 173|         
 174|         try:
 175|             with open(info_file, 'r', encoding='utf-8') as f:
 176|                 project_info = json.load(f)
 177|                 project_id = project_info.get("project_id", project_dir.name)
 178|         except Exception:
 179|             project_id = project_dir.name
 180|         
 181|         return {
 182|             "valid": True, 
 183|             "project_id": project_id, 
 184|             "project_path": str(project_dir.absolute())
 185|         }
 186| 
 187| # Экспортируем глобальный экземпляр
 188| shared_state = SharedState()
 189| 
 190| def get_shared_state():
 191|     return shared_state
```


## SOURCE_EVIDENCE: core/chat_storage.py
```
REPOSITORY: lhc-lab/AI-Colab
SOURCE: HF_DATASET
REVISION: UNKNOWN
FILE: core/chat_storage.py
CONTENT_SHA256: 7309fc7362f09d98f95dd5195978406bfad4318bc64b9e8e635e8ab8eb2cbc99
BYTES: 4639
LINES: 119
MODE: VERBATIM
TRUNCATED: false
EVIDENCE_LEVEL: CODE_READ
```
```text
   1| import os
   2| import json
   3| import re
   4| import logging
   5| from pathlib import Path
   6| from datetime import datetime
   7| from typing import List, Dict, Optional, Any
   8| 
   9| logger = logging.getLogger(__name__)
  10| 
  11| def sanitize_session_id(session_id: str) -> str:
  12|     """Защита от path traversal: разрешены только буквы, цифры, _ и -."""
  13|     return re.sub(r'[^a-zA-Z0-9_\-]', '_', session_id)
  14| 
  15| class ChatStorage:
  16|     def __init__(self, base_dir: str = "chats"):
  17|         self.base_dir = Path(base_dir)
  18|         self._ensure_dir(self.base_dir)
  19| 
  20|     def _ensure_dir(self, path: Path):
  21|         if not path.exists():
  22|             path.mkdir(parents=True, exist_ok=True)
  23| 
  24|     def _get_role_dir(self, role: str) -> Path:
  25|         role_dir = self.base_dir / role
  26|         self._ensure_dir(role_dir)
  27|         return role_dir
  28| 
  29|     def _get_session_path(self, session_id: str, role: str) -> Path:
  30|         safe_id = sanitize_session_id(session_id)
  31|         return self._get_role_dir(role) / f"{safe_id}.json"
  32| 
  33|     def create_session(self, session_id: str, role: str, metadata: Optional[Dict] = None) -> bool:
  34|         path = self._get_session_path(session_id, role)
  35|         if path.exists():
  36|             return False
  37|         
  38|         session_data = {
  39|             "session_id": session_id,
  40|             "role": role,
  41|             "created_at": datetime.now().isoformat(),
  42|             "updated_at": datetime.now().isoformat(),
  43|             "metadata": metadata or {},
  44|             "messages": []
  45|         }
  46|         self._save_session(path, session_data)
  47|         return True
  48| 
  49|     def get_session(self, session_id: str, role: str) -> Optional[Dict]:
  50|         path = self._get_session_path(session_id, role)
  51|         if not path.exists():
  52|             return None
  53|         try:
  54|             with open(path, 'r', encoding='utf-8') as f:
  55|                 return json.load(f)
  56|         except Exception as e:
  57|             logger.error(f"[ChatStorage] Failed to read {path}: {e}")
  58|             return None
  59| 
  60|     def append_message(self, session_id: str, role: str, message: Dict) -> bool:
  61|         path = self._get_session_path(session_id, role)
  62|         session = self.get_session(session_id, role)
  63|         if not session:
  64|             return False
  65|         
  66|         message["timestamp"] = datetime.now().isoformat()
  67|         session["messages"].append(message)
  68|         session["updated_at"] = datetime.now().isoformat()
  69|         
  70|         return self._save_session(path, session)
  71| 
  72|     def list_sessions(self, role: str, limit: int = 50) -> List[Dict]:
  73|         role_dir = self._get_role_dir(role)
  74|         sessions = []
  75|         try:
  76|             # Сортировка по времени модификации (новые сверху)
  77|             files = sorted(role_dir.glob("*.json"), key=os.path.getmtime, reverse=True)
  78|             for f in files[:limit]:
  79|                 try:
  80|                     with open(f, 'r', encoding='utf-8') as sf:
  81|                         data = json.load(sf)
  82|                         # Возвращаем только метаданные без сообщений для списка
  83|                         sessions.append({
  84|                             "session_id": data["session_id"],
  85|                             "created_at": data["created_at"],
  86|                             "updated_at": data["updated_at"],
  87|                             "metadata": data.get("metadata", {}),
  88|                             "message_count": len(data.get("messages", []))
  89|                         })
  90|                 except Exception as ef:
  91|                     logger.warning(f"[ChatStorage] Skipping corrupted file {f}: {ef}")
  92|         except Exception as e:
  93|             logger.error(f"[ChatStorage] Failed to list sessions for {role}: {e}")
  94|         return sessions
  95| 
  96|     def _save_session(self, path: Path, data: Dict) -> bool:
  97|         tmp_path = path.with_suffix(".tmp")
  98|         try:
  99|             with open(tmp_path, 'w', encoding='utf-8') as f:
 100|                 json.dump(data, f, indent=2, ensure_ascii=False)
 101|             tmp_path.replace(path)
 102|             return True
 103|         except Exception as e:
 104|             logger.error(f"[ChatStorage] Failed to save {path}: {e}")
 105|             if tmp_path.exists():
 106|                 try:
 107|                     os.remove(tmp_path)
 108|                 except:
 109|                     pass
 110|             return False
 111| 
 112| _storage_instance = None
 113| 
 114| def get_chat_storage() -> ChatStorage:
 115|     global _storage_instance
 116|     if _storage_instance is None:
 117|         # Путь относительно корня проекта, где запускается app2.py
 118|         _storage_instance = ChatStorage(base_dir="AIColab/chats")
 119|     return _storage_instance
```


## SOURCE_EVIDENCE: core/llm_integrations/chief_orchestrator.py
```
REPOSITORY: lhc-lab/AI-Colab
SOURCE: HF_DATASET
REVISION: UNKNOWN
FILE: core/llm_integrations/chief_orchestrator.py
CONTENT_SHA256: 3f85e4278d4f668da6eb015ce9b1b0930c89d7d25d82cb41b2f4859ca3ce27c9
BYTES: 10436
LINES: 211
MODE: VERBATIM
TRUNCATED: false
EVIDENCE_LEVEL: CODE_READ
```
```text
   1| import asyncio
   2| import time
   3| import logging
   4| from typing import List, Dict, Any, Optional
   5| 
   6| from core.llm_integrations.pce_engine import PairChatEngine
   7| from core.llm_integrations.cse_engine import ChairmanSynthesisEngine
   8| from core.llm_integrations.obe_engine import OpsBriefingEngine
   9| from core.llm_integrations.soul_layer import SoulLayerHook
  10| from core.llm_integrations.gcb_engine import GCBEngine
  11| from core.model_management import ModelManager
  12| from core.project_context import ProjectContext
  13| 
  14| logger = logging.getLogger(__name__)
  15| 
  16| class OrchestrationError(Exception):
  17|     """Исключение для ошибок оркестровки."""
  18|     pass
  19| 
  20| class ChiefOrchestrator:
  21|     def __init__(self, model_manager: Optional[ModelManager] = None, project_context: Optional[ProjectContext] = None, session_memory=None):
  22|         """
  23|         Инициализация с зависимостями, которые могут быть None.
  24|         Фактическая инициализация откладывается до первого использования.
  25|         """
  26|         self._model_manager = model_manager
  27|         self._project_context = project_context
  28|         self._session_memory = session_memory
  29|         self._initialized = False
  30|         self._chief_model = None
  31|         self.synthesis_engine = None
  32|         self.briefing_engine = None
  33|         self.soul_layer = None
  34|         self.gcb = None
  35| 
  36|         # Конфигурация отделов согласно интерфейсу, может быть загружена позже
  37|         self.departments = {
  38|             "A": {"name": "Аналитика", "models": ["Флик", "Флок"]},
  39|             "B": {"name": "Локализация", "models": ["Клик", "Клак"]},
  40|             "C": {"name": "Критика", "models": ["Чек", "Чок"]},
  41|             "D": {"name": "Интеграция", "models": ["Линк", "Синх"]}
  42|         }
  43| 
  44|     async def ensure_initialized(self):
  45|         """Отложенная инициализация ChiefOrchestrator."""
  46|         if self._initialized:
  47|             return
  48| 
  49|         if not self._model_manager:
  50|             self._model_manager = ModelManager.get_instance()
  51|         
  52|         if not self._project_context:
  53|             self._project_context = ProjectContext.get_instance()
  54| 
  55|         # Инициализируем GCB сразу, он не зависит от моделей LLM
  56|         if self.gcb is None:
  57|             self.gcb = GCBEngine()
  58| 
  59|         try:
  60|             # Инициализируем контекст (но не падаем, если нет проекта)
  61|             await self._project_context.ensure_initialized()
  62|             
  63|             # Загружаем модель Шефа
  64|             self._chief_model = await self._model_manager.get_model(
  65|                 'chief', 
  66|                 require_context=False  # Шеф может работать без проекта
  67|             )
  68|             
  69|             # Инициализация дочерних движков, зависящих от моделей
  70|             self.synthesis_engine = ChairmanSynthesisEngine(model=self._chief_model)
  71|             self.briefing_engine = OpsBriefingEngine(chief_model=self._chief_model, api_client=self._model_manager)
  72|             self.soul_layer = SoulLayerHook(api_client=self._model_manager, session_memory=self._session_memory)
  73| 
  74|             self._initialized = True
  75|             logger.info("ChiefOrchestrator fully initialized.")
  76|         except Exception as e:
  77|             # Логируем, но не падаем, чтобы позволить повторную попытку или ограниченную работу
  78|             logger.warning(f"ChiefOrchestrator delayed initialization warning: {e}")
  79| 
  80|     async def orchestrate(self, user_query: str, session_id: str = None) -> str:
  81|         """Прямая координация задачи Шефом с привлечением отделов при необходимости."""
  82|         await self.ensure_initialized()
  83|         
  84|         if not self._chief_model:
  85|             raise OrchestrationError("Chief model not available. Check your models_config.json and project context.")
  86|             
  87|         print(f"\n[Chief] Координация задачи: {user_query[:50]}...")
  88|         
  89|         # --- Режим с привлечением отделов ---
  90|         # По умолчанию задействуем Отдел А (Аналитика) для глубокого разбора
  91|         from core.role_binding_manager import RoleBindingManager
  92|         rbm = RoleBindingManager()
  93|         
  94|         # Добавляем [TASK] для активации формального режима отдела
  95|         task_with_marker = f"[TASK] {user_query}"
  96|         dept_result = await rbm.run_department("A", {"message": task_with_marker}, caller="chief")
  97|         
  98|         # Загружаем системный промпт Шефа для соблюдения контракта
  99|         system_prompt_chief = await rbm.get_prompt('chief')
 100|         
 101|         prompt = f"""Вы — Шеф (Главный координатор лаборатории AIColab). 
 102| Ваша задача — проанализировать запрос пользователя и экспертное заключение аналитического отдела.
 103| 
 104| Запрос пользователя: {user_query}
 105| 
 106| Заключение Отдела А (Аналитика):
 107| {dept_result}
 108| 
 109| На основе этого дайте финальный, структурированный ответ пользователю:"""
 110|         
 111|         response = await self._chief_model.generate(prompt, system_prompt=system_prompt_chief)
 112|         
 113|         # Сохранение в память если доступно
 114|         if self._session_memory and session_id:
 115|             try:
 116|                 await self._session_memory.save_chairman_synthesis(session_id, response, {"query": user_query, "dept_a_raw": dept_result})
 117|             except:
 118|                 pass
 119|                 
 120|         return response
 121| 
 122|     async def call_department_work(self, dept_key: str, task: str) -> str:
 123|         """Вызов отдела через RoleBindingManager."""
 124|         from core.role_binding_manager import RoleBindingManager
 125|         rbm = RoleBindingManager()
 126|         # Добавляем [TASK] для активации формального режима
 127|         task_with_marker = f"[TASK] {task}"
 128|         return await rbm.run_department(dept_key, {"message": task_with_marker}, caller="chief")
 129| 
 130|     async def run_department_pce(self, dept_key: str, task: str, session_id: str = None) -> Dict[str, Any]:
 131|         """Запуск PCE для конкретного отдела."""
 132|         await self.ensure_initialized()
 133|         if not self._chief_model:
 134|             raise OrchestrationError("Chief model not available for department PCE.")
 135| 
 136|         dept_info = self.departments[dept_key]
 137|         model_a = OpenRouterModelWrapper(self._model_manager, dept_info["models"][0])
 138|         model_b = OpenRouterModelWrapper(self._model_manager, dept_info["models"][1])
 139|         
 140|         pce = PairChatEngine(model_a, model_b, role=dept_info["name"])
 141|         result = await pce.run_competitive_dialogue(task)
 142|         
 143|         pair_id = f"dept_{dept_key}_{int(time.time())}"
 144|         result["pair_id"] = pair_id # Сохраняем ID в результат
 145| 
 146|         if self._session_memory and session_id:
 147|             for turn in result["history"]:
 148|                 await self._session_memory.save_pair_turn(session_id, pair_id, turn)
 149|         
 150|         return result
 151| 
 152|     async def run_briefing(self, topic: str, session_id: str = None) -> str:
 153|         """Оперативка: Шеф собирает краткие отчеты от ВСЕХ 8 моделей через OBE."""
 154|         await self.ensure_initialized()
 155|         if not self._chief_model:
 156|             raise OrchestrationError("Chief model not available for briefing.")
 157|             
 158|         print(f"\n[Chief] Запуск микродвижка OBE для темы: {topic}")
 159|         
 160|         participants = []
 161|         for dept_id, info in self.departments.items():
 162|             for model_name_key in info["models"]:
 163|                 model_key = model_name_key if model_name_key else "google/gemini-2.0-flash-exp:free"
 164|                 model = OpenRouterModelWrapper(self._model_manager, model_key)
 165|                 participants.append({"role": f"{info['name']} ({model_name_key})", "model": model})
 166|             
 167|         from core.role_binding_manager import RoleBindingManager
 168|         rbm = RoleBindingManager()
 169|         system_prompt_chief = await rbm.get_prompt('chief')
 170| 
 171|         briefing_result = await self.briefing_engine.run_briefing(
 172|             phase_name="Оперативка",
 173|             task_context=topic,
 174|             participants=participants,
 175|             system_prompt=system_prompt_chief
 176|         )
 177|         
 178|         summary = briefing_result["synthesis"]
 179|         
 180|         if self._session_memory and session_id:
 181|             await self._session_memory.save_briefing(
 182|                 session_id, 
 183|                 summary, 
 184|                 briefing_result["participants"] + ["Шеф"]
 185|             )
 186|             
 187|         return summary
 188| 
 189|     async def analyze_quality(self, session_id: str, pair_id: str) -> Dict[str, Any]:
 190|         """Запуск анализа качества для конкретной пары через Soul Layer."""
 191|         await self.ensure_initialized()
 192|         if not self._chief_model:
 193|             raise OrchestrationError("Chief model not available for quality analysis.")
 194| 
 195|         if not self._session_memory:
 196|             return {"error": "Session memory not initialized"}
 197|             
 198|         history = await self._session_memory.load_pair_history(session_id, pair_id)
 199|         if not history:
 200|             return {"error": f"No history found for pair {pair_id}"}
 201|             
 202|         return await self.soul_layer.analyze_pair_quality(session_id, pair_id, history)
 203| 
 204| class OpenRouterModelWrapper:
 205|     def __init__(self, model_manager: ModelManager, model_key: str):
 206|         self.model_manager = model_manager
 207|         self.model_key = model_key
 208| 
 209|     async def generate(self, prompt: str) -> str:
 210|         model_instance = await self.model_manager.get_model(self.model_key, require_context=False)
 211|         return await model_instance.generate(prompt)
```


## SOURCE_EVIDENCE: core/llm_integrations/doctor_engine.py
```
REPOSITORY: lhc-lab/AI-Colab
SOURCE: HF_DATASET
REVISION: UNKNOWN
FILE: core/llm_integrations/doctor_engine.py
CONTENT_SHA256: 79245027a070fd404f729132758b3ceab067a32f9c9ccefef9e00cd48fe92645
BYTES: 3613
LINES: 78
MODE: VERBATIM
TRUNCATED: false
EVIDENCE_LEVEL: CODE_READ
```
```text
   1| import json
   2| import re
   3| import logging
   4| from typing import List, Dict, Any, Optional
   5| from pathlib import Path
   6| 
   7| class DoctorEngine:
   8|     def __init__(self, doctor_model):
   9|         self.doctor_model = doctor_model
  10|         self.config_path = Path("D:/Gemini/AIColab/config/models_config.json")
  11|         self.prompts_dir = Path("D:/Gemini/AIColab/prompts")
  12| 
  13|     async def run_diagnostics(self, dialogue_history: List[Dict[str, Any]], context: str = "") -> Dict[str, Any]:
  14|         """
  15|         Запуск диагностики Доктора на основе истории диалога.
  16|         """
  17|         logging.info("[DoctorEngine] Запуск холодной диагностики...")
  18|         
  19|         formatted_history = self._format_history(dialogue_history)
  20|         
  21|         # Промпт уже заложен в системном промпте модели Доктора.
  22|         # Здесь мы просто передаем данные для анализа.
  23|         input_data = f"""
  24| КОНТЕКСТ: {context}
  25| ИСТОРИЯ ДИАЛОГОВ:
  26| {formatted_history}
  27| 
  28| ПРОВЕДИ ДИАГНОСТИКУ.
  29| """
  30|         try:
  31|             # Модель Доктора (Qwen) настроена на JSON-выход в системном промпте.
  32|             response = await self.doctor_model.generate(input_data)
  33|             
  34|             # Очистка от <think> тегов (на всякий случай, если GptOssModel их пропустил)
  35|             response = re.sub(r'<think>.*?</think>', '', response, flags=re.DOTALL).strip()
  36|             
  37|             # Извлечение JSON
  38|             json_match = re.search(r'\{.*\}', response, re.DOTALL)
  39|             if json_match:
  40|                 diagnosis = json.loads(json_match.group())
  41|             else:
  42|                 diagnosis = json.loads(response)
  43|                 
  44|             logging.info(f"[DoctorEngine] Диагноз получен: {diagnosis.get('diagnosis', 'UNKNOWN')}")
  45|             return diagnosis
  46|         except Exception as e:
  47|             logging.error(f"[DoctorEngine] Ошибка при диагностике: {e}")
  48|             return {"diagnosis": "ERROR", "error": str(e)}
  49| 
  50|     def _format_history(self, history: List[Dict[str, Any]]) -> str:
  51|         lines = []
  52|         for turn in history:
  53|             role = turn.get("role", turn.get("model", "Unknown"))
  54|             content = turn.get("content", "")[:500] # Доктору нужны только симптомы
  55|             lines.append(f"[{role}]: {content}")
  56|         return "\n".join(lines)
  57| 
  58|     async def execute_hr_rotation(self, diagnosis: Dict[str, Any]) -> List[Dict[str, Any]]:
  59|         """
  60|         Реализация кадровых решений на основе диагноза Доктора.
  61|         """
  62|         if diagnosis.get("diagnosis") != "INTERVENE":
  63|             return []
  64| 
  65|         enforcement = diagnosis.get("enforcement", {})
  66|         if not enforcement.get("pause_model"):
  67|             return []
  68| 
  69|         notifications = enforcement.get("notify", [])
  70|         rotations = []
  71| 
  72|         # В будущем здесь будет логика подбора альтернативной модели из available_openrouter_models.
  73|         # Пока просто фиксируем необходимость ротации.
  74|         for model_key in notifications:
  75|             logging.warning(f"[DoctorEngine] HR-РОТАЦИЯ: Модель {model_key} деградировала и требует замены.")
  76|             rotations.append({"model_key": model_key, "action": "rotate"})
  77| 
  78|         return rotations
```


## SOURCE_EVIDENCE: integrations/openrouter_adapter.py
```
REPOSITORY: lhc-lab/AI-Colab
SOURCE: HF_DATASET
REVISION: UNKNOWN
FILE: integrations/openrouter_adapter.py
CONTENT_SHA256: 46daccfc8104f17c9d041ed3917bd92d295a85d576535ece6157332dabfb8deb
BYTES: 10545
LINES: 184
MODE: VERBATIM
TRUNCATED: false
EVIDENCE_LEVEL: CODE_READ
```
```text
   1| import aiohttp
   2| import json
   3| import os
   4| import asyncio
   5| import logging
   6| from pathlib import Path
   7| from core.role_binding_manager import RoleBindingManager
   8| 
   9| logger = logging.getLogger(__name__)
  10| 
  11| class ConfigError(Exception):
  12|     """Ошибка конфигурации моделей."""
  13|     pass
  14| 
  15| class RateLimitError(Exception):
  16|     """Превышен лимит запросов к OpenRouter."""
  17|     pass
  18| 
  19| class OpenRouterModel:
  20|     def __init__(self, config):
  21|         self.config = config
  22|         self.role_key = config.get("key")  # например 'flick'
  23|         self.api_key = os.getenv("OPENROUTER_API_KEY")
  24|         self.model_id = None # Будет получено в generate
  25|         self.short_name = config.get("short_name", "unknown")
  26|         
  27|         if not self.api_key:
  28|             raise ValueError("OPENROUTER_API_KEY не установлен")
  29|     
  30|     async def _ensure_model_id(self):
  31|         if self.model_id:
  32|             return
  33|         
  34|         rbm = RoleBindingManager()
  35|         self.model_id = await rbm.get_fixed_model(self.role_key)
  36|         
  37|         if not self.model_id:
  38|             fallback_model = self.config.get("model_id") or "meta-llama/llama-3.2-3b-instruct:free"
  39|             logger.warning(f"Для роли {self.role_key} не найдена фиксированная модель, используется fallback: {fallback_model}")
  40|             self.model_id = fallback_model
  41|         
  42|         if not self.short_name or self.short_name == "unknown":
  43|             self.short_name = self.model_id.split('/')[-1].split(':')[0]
  44| 
  45|     async def generate(self, prompt=None, system_prompt=None, messages=None, **kwargs):
  46|         """
  47|         Генерация ответа.
  48|         """
  49|         await self._ensure_model_id()
  50|         return await self._generate_with_retry(prompt, system_prompt, messages=messages, retry_count=0, **kwargs)
  51| 
  52|     async def _generate_with_retry(self, prompt, system_prompt, messages=None, retry_count=0, **kwargs):
  53|         if messages is not None:
  54|             # Используем переданный список сообщений
  55|             payload_messages = messages
  56|         else:
  57|             # Старое поведение для обратной совместимости
  58|             payload_messages = []
  59|             if system_prompt:
  60|                 payload_messages.append({"role": "system", "content": system_prompt})
  61|             if prompt:
  62|                 payload_messages.append({"role": "user", "content": prompt})
  63|             else:
  64|                 raise ValueError("Either messages or prompt must be provided")
  65|         
  66|         data = {
  67|             "model": self.model_id,
  68|             "messages": payload_messages,
  69|             "max_tokens": kwargs.get('max_tokens', 512),
  70|             "temperature": kwargs.get('temperature', 0.7),
  71|             "top_p": kwargs.get('top_p', 1.0)
  72|         }
  73|         
  74|         headers = {
  75|             "Authorization": f"Bearer {self.api_key}",
  76|             "Content-Type": "application/json",
  77|             "HTTP-Referer": "https://huggingface.co/lhc-lab/AIColab",
  78|             "X-Title": "AIColab"
  79|         }
  80|         
  81|         async with aiohttp.ClientSession() as session:
  82|             # ============================================================================
  83|             # EXPONENTIAL BACKOFF — SPEC_2026_04_02
  84|             # ============================================================================
  85|             MAX_RETRY_ATTEMPTS = 3
  86|             RETRY_DELAYS = [1, 2, 4]
  87|             
  88|             try:
  89|                 for attempt in range(MAX_RETRY_ATTEMPTS):
  90|                     try:
  91|                         async with session.post(
  92|                             "https://openrouter.ai/api/v1/chat/completions",
  93|                             headers=headers,
  94|                             json=data,
  95|                             timeout=35
  96|                         ) as response:
  97|                             if response.status == 429:
  98|                                 raise RateLimitError(f"Rate limit exceeded for {self.model_id}")
  99| 
 100|                             if response.status == 200:
 101|                                 result = await response.json()
 102|                                 text = result['choices'][0]['message']['content']
 103|                                 if text and text.strip():
 104|                                     logger.info(f"✅ Ответ от зафиксированной модели {self.model_id} для {self.role_key} получен.")
 105|                                     return text
 106|                                 else:
 107|                                     raise Exception("Empty response from model")
 108|                             
 109|                             # Обработка специфических ошибок для Failover (404, 402, 5xx)
 110|                             # 429 теперь обрабатывается в retry-цикле выше
 111|                             error_text = await response.text()
 112|                             if response.status in [404, 402, 500, 502, 503, 504] and retry_count < 1:
 113|                                 logger.warning(f"⚠️ Ошибка {response.status} для {self.model_id} ({self.role_key}). Попытка авто-переключения...")
 114|                                 return await self._perform_auto_switch(prompt, system_prompt, messages, response.status, **kwargs)
 115|                             
 116|                             raise Exception(f"OpenRouter ошибка {response.status} для {self.model_id}: {error_text}")
 117| 
 118|                     except RateLimitError as e:
 119|                         if attempt == MAX_RETRY_ATTEMPTS - 1:
 120|                             logger.error(
 121|                                 f"[FAIL] model={self.model_id} role={self.role_key} "
 122|                                 f"task={kwargs.get('task_id', 'default')} retries_exhausted={MAX_RETRY_ATTEMPTS}"
 123|                             )
 124|                             # Бросаем RuntimeError, чтобы внешний except поймал его и запустил Failover
 125|                             raise RuntimeError(
 126|                                 f"Rate limit exceeded after {MAX_RETRY_ATTEMPTS} retries for model '{self.model_id}'"
 127|                             ) from e
 128| 
 129|                         delay = RETRY_DELAYS[attempt] if attempt < len(RETRY_DELAYS) else RETRY_DELAYS[-1]
 130|                         logger.warning(
 131|                             f"[RETRY] model={self.model_id} role={self.role_key} task={kwargs.get('task_id', 'default')} "
 132|                             f"attempt={attempt + 1}/{MAX_RETRY_ATTEMPTS} delay={delay}s reason=429"
 133|                         )
 134|                         await asyncio.sleep(delay)
 135|                     
 136|                     except (asyncio.TimeoutError, aiohttp.ClientError) as e:
 137|                         # Сетевые ошибки и таймауты сразу пробрасываем во внешний try для Failover
 138|                         raise e
 139|                     
 140|                     except Exception as e:
 141|                         # Любые другие ошибки (включая наши Exception("OpenRouter ошибка...")) пробрасываем
 142|                         raise e
 143|                         
 144|             except (asyncio.TimeoutError, aiohttp.ClientError, Exception) as e:
 145|                 # Если это не наше собственное исключение (Exception с текстом "OpenRouter ошибка"),
 146|                 # то пробуем переключиться
 147|                 if retry_count < 1 and not str(e).startswith("OpenRouter ошибка"):
 148|                     logger.warning(f"⏰ Сбой (таймаут/сеть/429) для {self.model_id} ({self.role_key}): {e}. Попытка авто-переключения...")
 149|                     return await self._perform_auto_switch(prompt, system_prompt, messages, "timeout_or_error_or_429", **kwargs)
 150|                 raise e
 151| 
 152|     async def _perform_auto_switch(self, prompt, system_prompt, messages, error_reason, **kwargs):
 153|         """Выполняет поиск новой модели и повторный запрос."""
 154|         rbm = RoleBindingManager()
 155|         # REM [2026-03-16 21:05] new_model_id = rbm.get_next_available_model(self.role_key, exclude=self.model_id)
 156|         new_model_id = await rbm.get_model_for_role(self.role_key, task_id=kwargs.get('task_id', 'default'), exclude=[self.model_id]) # exclude=self.model_id заменен на exclude=[self.model_id] для корректной работы с List[str]
 157|         
 158|         # FAILOVER GUARD: предотвращает бесконечный цикл 429 → exclude → та же модель
 159|         # Если после исключения current_model выбирается та же модель —
 160|         # значит, в пуле нет альтернатив. Останавливаем цикл явной ошибкой.
 161|         # Это предпочтительнее, чем молчаливое зависание или повторные 429.
 162|         if new_model_id == self.model_id:
 163|             logger.warning(
 164|                 f"Failover ineffective: {self.model_id} selected again. "
 165|                 f"Role: {self.role_key}, Task: {kwargs.get('task_id', 'default')}, "
 166|                 f"Pool size: {len(rbm._get_available_models())}. "
 167|                 f"No alternative models available."
 168|             )
 169|             raise RuntimeError(
 170|                 f"Failover ineffective: no alternative models for role '{self.role_key}'"
 171|             )
 172|         
 173|         if new_model_id and new_model_id != self.model_id:
 174|             old_model = self.model_id
 175|             # Фиксируем новую привязку в реестре
 176|             await rbm.switch_binding(self.role_key, new_model_id, reason=f"auto_failover:{str(error_reason)}")
 177|             # Обновляем текущий экземпляр
 178|             self.model_id = new_model_id
 179|             logger.info(f"🔄 Роль {self.role_key} успешно переключена: {old_model} -> {new_model_id}")
 180|             # Повторяем запрос (один retry)
 181|             return await self._generate_with_retry(prompt, system_prompt, messages, retry_count=1, **kwargs)
 182|         else:
 183|             logger.error(f"❌ Нет доступных fallback-моделей для роли {self.role_key} (текущая: {self.model_id})")
 184|             raise Exception(f"Failover failed: No fallback models for {self.role_key}")
```


## SOURCE_EVIDENCE: integrations/gptoss_adapter.py
```
REPOSITORY: lhc-lab/AI-Colab
SOURCE: HF_DATASET
REVISION: UNKNOWN
FILE: integrations/gptoss_adapter.py
CONTENT_SHA256: 9443fc2b82c933c70884c92198533c4384b91473fbdbd2ccf632577babcf2766
BYTES: 6103
LINES: 146
MODE: VERBATIM
TRUNCATED: false
EVIDENCE_LEVEL: CODE_SKIMMED (структура и ключевые строки, не построчно)
```
```text
   1| import os
   2| import logging
   3| import asyncio
   4| import gc
   5| from typing import Optional
   6| from pathlib import Path
   7| from core.project_context import ProjectContext
   8| import torch
   9| 
  10| logger = logging.getLogger(__name__)
  11| 
  12| class GptOssModel:
  13|     def __init__(self, config):
  14|         self.config = config
  15|         self.model_id = config.get("model_id")
  16|         self.model = None
  17|         self.model_format = config.get("model_format", "default")
  18|         
  19|         # ОПРЕДЕЛЕНИЕ ПУТЕЙ (Строго по реальной структуре папок)
  20|         base_dir = Path(__file__).resolve().parent.parent # Корень AIColab
  21|         models_root = base_dir / "integrations" / "models"
  22|         
  23|         if self.model_id == "Phi-3-mini-4k-instruct-q4.gguf":
  24|             self.model_path = str(models_root / "Phi-3-mini" / self.model_id)
  25|         elif self.model_id == "gemma-2-2b-it.Q4_K_M.gguf":
  26|             self.model_path = str(models_root / "gemma-2-2b" / self.model_id)
  27|         elif "Qwen2.5-1.5B-VibeThinker" in self.model_id:
  28|             self.model_path = str(models_root / "Qwen2.5-1.5B-VibeThinker-heretic-uncensored-abliterated-GGUF" / self.model_id)
  29|         else:
  30|             self.model_path = str(models_root / self.model_id)
  31|             
  32|         self._has_done_intro = False  # Флаг первого вызова
  33| 
  34|     def _format_prompt(self, system_prompt, user_prompt):
  35|         """Форматирование промпта в зависимости от модели (ДАО Сенсея)"""
  36|         if self.model_format == "phi3":
  37|             # Формат для Phi-3-mini
  38|             return f"<|user|>\n{system_prompt}\n{user_prompt}<|assistant|>"
  39|         elif self.model_format == "gemma":
  40|             # Формат для Gemma-2
  41|             return f"<start_of_turn>user\n{system_prompt}\n{user_prompt}<end_of_turn>\n<start_of_turn>model\n"
  42|         else:
  43|             # Стандартный формат
  44|             return f"{system_prompt}\n\n{user_prompt}"
  45| 
  46|     async def load_model(self):
  47|         """Загрузка модели GGUF через llama.cpp (Шаг 2.4 ТЗ)"""
  48|         try:
  49|             from llama_cpp import Llama
  50|             
  51|             if not os.path.exists(self.model_path):
  52|                 raise FileNotFoundError(f"Файл модели не найден: {self.model_path}")
  53|             
  54|             # Параметры напрямую из корня конфига модели
  55|             n_gpu_layers = self.config.get("n_gpu_layers", 0)
  56|             n_ctx = self.config.get("n_ctx", 2048)
  57|             
  58|             self.model = Llama(
  59|                 model_path=self.model_path,
  60|                 n_ctx=n_ctx,
  61|                 n_gpu_layers=n_gpu_layers,
  62|                 verbose=False
  63|             )
  64|             
  65|             logger.info(f"Загружена модель: {self.model_id} (GPU слоев: {n_gpu_layers})")
  66|             return True
  67|             
  68|         except Exception as e:
  69|             logger.error(f"Ошибка загрузки модели {self.model_id}: {e}")
  70|             raise
  71| 
  72|     async def generate(self, prompt, system_prompt=None, **kwargs):
  73|         """Генерация ответа (Шаг 2.3 ТЗ)"""
  74|         if self.model is None:
  75|             await self.load_model()
  76|         
  77|         # Получаем системный промпт роли, если он не передан
  78|         if not system_prompt:
  79|             prompt_filename = self.config.get("system_prompt_file")
  80|             if prompt_filename:
  81|                 ctx = ProjectContext.get_instance()
  82|                 await ctx.ensure_initialized()
  83|                 
  84|                 search_dirs = [
  85|                     ctx.get_current_project_path() / "prompts",
  86|                     ctx.base_dir / "docs" / "prompts"
  87|                 ]
  88|                 
  89|                 found_path = None
  90|                 for s_dir in search_dirs:
  91|                     test_path = s_dir / prompt_filename
  92|                     if test_path.exists():
  93|                         found_path = test_path
  94|                         break
  95|                 
  96|                 if found_path:
  97|                     system_prompt = found_path.read_text(encoding='utf-8').strip()
  98|         
  99|         # Форматируем промпт
 100|         formatted_prompt = self._format_prompt(system_prompt or "", prompt)
 101|         
 102|         # ПАРАМЕТРЫ ГЕНЕРАЦИИ (Строго по ТЗ)
 103|         if self.model_format == "phi3":
 104|             params = {
 105|                 "max_tokens": kwargs.get('max_tokens', 512),
 106|                 "temperature": 0.3,
 107|                 "top_p": 0.9,
 108|                 "repeat_penalty": 1.1,
 109|                 "stop": ['<|end|>', '<|user|>', '\n\n'],
 110|                 "echo": False
 111|             }
 112|         else:
 113|             params = {
 114|                 "max_tokens": kwargs.get('max_tokens', 512),
 115|                 "temperature": kwargs.get('temperature', 0.7),
 116|                 "top_p": kwargs.get('top_p', 0.9),
 117|                 "stop": kwargs.get('stop_sequences', [])
 118|             }
 119|         
 120|         if 'stop' in params and not params['stop']:
 121|             del params['stop']
 122|         
 123|         # Асинхронная генерация
 124|         loop = asyncio.get_event_loop()
 125|         response = await loop.run_in_executor(
 126|             None,
 127|             lambda: self.model(formatted_prompt, **params)
 128|         )
 129|         
 130|         return response['choices'][0]['text'].strip()
 131| 
 132|     async def unload_model(self):
 133|         """Безопасная выгрузка модели с полной очисткой"""
 134|         if self.model is not None:
 135|             try:
 136|                 model_id = self.model_id
 137|                 del self.model
 138|                 self.model = None
 139|                 gc.collect()
 140|                 if torch.cuda.is_available():
 141|                     torch.cuda.empty_cache()
 142|                     torch.cuda.synchronize()
 143|                 logger.info(f"Модель {model_id} полностью выгружена")
 144|             except Exception as e:
 145|                 logger.warning(f"Ошибка при выгрузке {self.model_id}: {e}")
 146|                 self.model = None
```


## SOURCE_EVIDENCE: config/models_config.json
```
REPOSITORY: lhc-lab/AI-Colab
SOURCE: HF_DATASET
REVISION: UNKNOWN
FILE: config/models_config.json
CONTENT_SHA256: 18bfbb8c5cb51854eb4d9047612e509419e058d46001013d1df98e0de752eb06
BYTES: 5292
LINES: 169
MODE: VERBATIM
TRUNCATED: false
EVIDENCE_LEVEL: CODE_READ (конфигурация; секретов нет)
```
```text
   1| {
   2|   "active_models": [
   3|     {
   4|       "key": "flick",
   5|       "model_id": "arcee-ai/trinity-large-preview:free",
   6|       "provider": "openrouter",
   7|       "status": "active"
   8|     },
   9|     {
  10|       "key": "flock",
  11|       "model_id": "arcee-ai/trinity-large-preview:free",
  12|       "provider": "openrouter",
  13|       "status": "active"
  14|     },
  15|     {
  16|       "key": "click",
  17|       "model_id": "arcee-ai/trinity-large-preview:free",
  18|       "provider": "openrouter",
  19|       "status": "active"
  20|     },
  21|     {
  22|       "key": "clack",
  23|       "model_id": "arcee-ai/trinity-large-preview:free",
  24|       "provider": "openrouter",
  25|       "status": "active"
  26|     },
  27|     {
  28|       "key": "check",
  29|       "model_id": "arcee-ai/trinity-large-preview:free",
  30|       "provider": "openrouter",
  31|       "status": "active"
  32|     },
  33|     {
  34|       "key": "chock",
  35|       "model_id": "arcee-ai/trinity-large-preview:free",
  36|       "provider": "openrouter",
  37|       "status": "active"
  38|     },
  39|     {
  40|       "key": "link",
  41|       "model_id": "arcee-ai/trinity-large-preview:free",
  42|       "provider": "openrouter",
  43|       "status": "active"
  44|     },
  45|     {
  46|       "key": "sync",
  47|       "model_id": "arcee-ai/trinity-large-preview:free",
  48|       "provider": "openrouter",
  49|       "status": "active"
  50|     },
  51|     {
  52|       "key": "ceo",
  53|       "model_id": "D:/Gemini/AIColab/integrations/models/gemma-2-2b/gemma-2-2b-it.Q4_K_M.gguf",
  54|       "provider": "gptoss",
  55|       "status": "active",
  56|       "system_prompt_file": "core/ceo.txt"
  57|     },
  58|     {
  59|       "key": "chief",
  60|       "model_id": "D:/Gemini/AIColab/integrations/models/Phi-3-mini/Phi-3-mini-4k-instruct-q4.gguf",
  61|       "provider": "gptoss",
  62|       "status": "active",
  63|       "system_prompt_file": "core/chief.txt"
  64|     }
  65|   ],
  66|   "available_openrouter_models": [
  67|     "arcee-ai/trinity-large-preview:free",
  68|     "arcee-ai/trinity-mini:free",
  69|     "cognitivecomputations/dolphin-mistral-24b-venice-edition:free",
  70|     "google/gemma-3-12b-it:free",
  71|     "google/gemma-3-27b-it:free",
  72|     "google/gemma-3-4b-it:free",
  73|     "google/gemma-3n-e2b-it:free",
  74|     "google/gemma-3n-e4b-it:free",
  75|     "liquid/lfm-2.5-1.2b-instruct:free",
  76|     "liquid/lfm-2.5-1.2b-thinking:free",
  77|     "meta-llama/llama-3.2-3b-instruct:free",
  78|     "meta-llama/llama-3.3-70b-instruct:free",
  79|     "nousresearch/hermes-3-llama-3.1-405b:free",
  80|     "nvidia/nemotron-3-nano-30b-a3b:free",
  81|     "nvidia/nemotron-3-super-120b-a12b:free",
  82|     "nvidia/nemotron-nano-12b-v2-vl:free",
  83|     "nvidia/nemotron-nano-9b-v2:free",
  84|     "openrouter/free:free",
  85|     "qwen/qwen3-coder:free",
  86|     "qwen/qwen3-next-80b-a3b-instruct:free",
  87|     "qwen/qwen3.6-plus-preview:free",
  88|     "stepfun/step-3.5-flash:free",
  89|     "z-ai/glm-4.5-air:free"
  90|   ],
  91|   "roles_fixed_mapping": {
  92|     "flick": {
  93|       "primary": "arcee-ai/trinity-large-preview:free",
  94|       "fallback": [],
  95|       "status": "active"
  96|     },
  97|     "flock": {
  98|       "primary": "arcee-ai/trinity-large-preview:free",
  99|       "fallback": [],
 100|       "status": "active"
 101|     },
 102|     "click": {
 103|       "primary": "arcee-ai/trinity-large-preview:free",
 104|       "fallback": [],
 105|       "status": "active"
 106|     },
 107|     "clack": {
 108|       "primary": "arcee-ai/trinity-large-preview:free",
 109|       "fallback": [],
 110|       "status": "active"
 111|     },
 112|     "check": {
 113|       "primary": "arcee-ai/trinity-large-preview:free",
 114|       "fallback": [],
 115|       "status": "active"
 116|     },
 117|     "chock": {
 118|       "primary": "arcee-ai/trinity-large-preview:free",
 119|       "fallback": [],
 120|       "status": "active"
 121|     },
 122|     "link": {
 123|       "primary": "arcee-ai/trinity-large-preview:free",
 124|       "fallback": [],
 125|       "status": "active"
 126|     },
 127|     "sync": {
 128|       "primary": "arcee-ai/trinity-large-preview:free",
 129|       "fallback": [],
 130|       "status": "active"
 131|     }
 132|   },
 133|   "last_updated": "2026-04-01T16:55:45.431274",
 134|   "last_updated_by_samurai": "2026-03-25T23:45:00",
 135|   "verification_report": {
 136|     "total_working": 23,
 137|     "timestamp": "2026-04-01T16:55:45.431274",
 138|     "details": {
 139|       "arcee-ai/trinity-large-preview:free": "limit",
 140|       "arcee-ai/trinity-mini:free": "limit",
 141|       "cognitivecomputations/dolphin-mistral-24b-venice-edition:free": "limit",
 142|       "google/gemma-3-12b-it:free": "limit",
 143|       "google/gemma-3-27b-it:free": "limit",
 144|       "google/gemma-3-4b-it:free": "limit",
 145|       "google/gemma-3n-e2b-it:free": "limit",
 146|       "google/gemma-3n-e4b-it:free": "limit",
 147|       "google/lyria-3-clip-preview:free": "fatal",
 148|       "google/lyria-3-pro-preview:free": "fatal",
 149|       "liquid/lfm-2.5-1.2b-instruct:free": "limit",
 150|       "liquid/lfm-2.5-1.2b-thinking:free": "limit",
 151|       "meta-llama/llama-3.2-3b-instruct:free": "limit",
 152|       "meta-llama/llama-3.3-70b-instruct:free": "limit",
 153|       "minimax/minimax-m2.5:free": "fatal",
 154|       "nousresearch/hermes-3-llama-3.1-405b:free": "limit",
 155|       "nvidia/nemotron-3-nano-30b-a3b:free": "limit",
 156|       "nvidia/nemotron-3-super-120b-a12b:free": "limit",
 157|       "nvidia/nemotron-nano-12b-v2-vl:free": "limit",
 158|       "nvidia/nemotron-nano-9b-v2:free": "limit",
 159|       "openai/gpt-oss-120b:free": "fatal",
 160|       "openai/gpt-oss-20b:free": "fatal",
 161|       "openrouter/free:free": "working",
 162|       "qwen/qwen3-coder:free": "limit",
 163|       "qwen/qwen3-next-80b-a3b-instruct:free": "limit",
 164|       "qwen/qwen3.6-plus-preview:free": "working",
 165|       "stepfun/step-3.5-flash:free": "exception",
 166|       "z-ai/glm-4.5-air:free": "limit"
 167|     }
 168|   }
 169| }
```