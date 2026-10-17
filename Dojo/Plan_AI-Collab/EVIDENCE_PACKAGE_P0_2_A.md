# EVIDENCE PACKAGE P0.2-A for DEVELOPER DEEPSEEK
Источник: HF dataset lhc-lab/AI-Colab, REVISION UNKNOWN, MODE VERBATIM (нумерация строк добавлена, в хэш не входит). Ничего не запускалось: RUNTIME_UNVERIFIED. Секретов в файлах нет.



## SOURCE_EVIDENCE: core/role_binding_manager.py
```
REPOSITORY: lhc-lab/AI-Colab
SOURCE: HF_DATASET
REVISION: UNKNOWN
FILE: core/role_binding_manager.py
CONTENT_SHA256: 6df2e425887a1a1792ca969f59b56595a2c21da9d46d28aa613ea0dd9c9d6acc
BYTES: 13623
LINES: 358
MODE: VERBATIM
TRUNCATED: false
EVIDENCE_LEVEL: STATIC_ANALYZED
```
```text
   1| # REM [2026-04-08] Zero Module Execution (SPEC_2026_04_08)
   2| import json
   3| import os
   4| import threading
   5| import hashlib
   6| import logging
   7| import asyncio
   8| from typing import Dict, Optional, Any, List, Tuple, Union
   9| from datetime import datetime, timedelta
  10| from pathlib import Path
  11| 
  12| # REM [2026-04-08] These constants are safe to keep at module level
  13| # Состояния отделов
  14| DEPT_STATE_IDLE = "idle"
  15| DEPT_STATE_BUSY_BY_CEO = "busy_by_ceo"
  16| DEPT_STATE_BUSY_BY_SYSTEM = "busy_by_system"
  17| 
  18| # Константы
  19| LOCK_TTL_SECONDS = 120
  20| MAX_ROUNDS_DEFAULT = 2
  21| 
  22| # Маппинг отделов и ролей
  23| DEPT_ROLES = {
  24|     "A": ["flick", "flock"],
  25|     "B": ["click", "clack"],
  26|     "C": ["check", "chock"],
  27|     "D": ["link", "sync"]
  28| }
  29| 
  30| _role_manager = None
  31| 
  32| def get_role_manager(model_manager=None, config_path=None, state_path=None):
  33|     """
  34|     Lazy getter for the singleton instance.
  35|     This is the ONLY entrypoint to the RoleBindingManager.
  36|     """
  37|     global _role_manager
  38|     if _role_manager is None:
  39|         _role_manager = RoleBindingManager(model_manager, config_path, state_path)
  40|     return _role_manager
  41| 
  42| class RoleBindingManager:
  43|     """
  44|     Manages role-to-model bindings with Zero Module Execution invariant.
  45|     """
  46|     
  47|     def __init__(self, model_manager=None, config_path=None, state_path=None):
  48|         self.model_manager = model_manager
  49|         self.config_path = config_path
  50|         self.state_path = state_path
  51|         
  52|         # Internal state (Lazy initialization in _ensure_initialized)
  53|         self.project_path = None
  54|         self.roles_state = {}
  55|         self.models_config = {}
  56|         self._bindings = {} # Sticky Memory Cache
  57|         
  58|         # Department locks (Initial state is empty, populated in _ensure_initialized)
  59|         self._dept_locks = {}
  60|         
  61|         self._initialized = False
  62|         self._prompt_registry = None
  63|         
  64|         # Lazy objects
  65|         self._logger = None
  66|         self._state_lock = None
  67|         
  68|     def _get_logger(self):
  69|         """Lazy logger initialization."""
  70|         if self._logger is None:
  71|             self._logger = logging.getLogger(__name__)
  72|         return self._logger
  73| 
  74|     def _get_state_lock(self):
  75|         """Lazy threading lock initialization."""
  76|         if self._state_lock is None:
  77|             self._state_lock = threading.RLock()
  78|         return self._state_lock
  79| 
  80|     async def _ensure_initialized(self):
  81|         """
  82|         Guarantees loading of state and configuration paths lazily.
  83|         Triggers execution ONLY when first used in runtime.
  84|         """
  85|         if self._initialized:
  86|             return
  87| 
  88|         # LAZY IMPORTS to avoid module execution on import
  89|         from core.shared_state import get_shared_state
  90|         from core.prompt_registry import PromptRegistry
  91| 
  92|         logger = self._get_logger()
  93|         state = get_shared_state()
  94|         self.project_path = Path(state.get("current_project_path", "."))
  95|         
  96|         # Configure paths based on project state
  97|         if not self.config_path:
  98|             self.config_path = self.project_path / "config" / "models_config.json"
  99|         if not self.state_path:
 100|             self.state_path = self.project_path / "config" / "roles_state.json"
 101|             
 102|         # Global paths (fallback)
 103|         self.global_config_path = Path(__file__).parent.parent / "config" / "models_config.json"
 104|         self.global_state_path = Path(__file__).parent.parent / "config" / "roles_state.json"
 105| 
 106|         # Load data
 107|         self.roles_state = self._load_state()
 108|         self.models_config = self._load_config()
 109|         
 110|         # Ensure state file exists
 111|         if not self.state_path.exists(): 
 112|              self._save_state()
 113|              logger.info(f"Created initial roles_state.json at {self.state_path}")
 114| 
 115|         if self._prompt_registry is None:
 116|             self._prompt_registry = PromptRegistry()
 117|             
 118|         # Initialize department locks
 119|         self._dept_locks = {
 120|             dept: {"state": DEPT_STATE_IDLE, "locked_by": None, "expires": None} 
 121|             for dept in DEPT_ROLES
 122|         }
 123|             
 124|         self._initialized = True
 125|         logger.info("RoleBindingManager initialized. Project: %s", self.project_path)
 126| 
 127|     def _load_config(self) -> Dict:
 128|         path = self.config_path if self.config_path and self.config_path.exists() else self.global_config_path
 129|         if not path.exists():
 130|             return {"available_openrouter_models": [], "active_models": {}}
 131|         try:
 132|             with open(path, 'r', encoding='utf-8') as f:
 133|                 return json.load(f)
 134|         except Exception as e:
 135|             self._get_logger().error(f"Error loading models_config: {e}")
 136|             return {"available_openrouter_models": [], "active_models": {}}
 137| 
 138|     def _load_state(self) -> Dict:
 139|         path = self.state_path if self.state_path and self.state_path.exists() else self.global_state_path
 140|         if path.exists():
 141|             try:
 142|                 with open(path, 'r', encoding='utf-8') as f:
 143|                     return json.load(f)
 144|             except Exception as e:
 145|                 self._get_logger().error(f"Error loading roles_state: {e}")
 146|                 return {}
 147|         return {}
 148| 
 149|     def _save_state(self):
 150|         if not self.state_path:
 151|             return
 152|         try:
 153|             self.state_path.parent.mkdir(parents=True, exist_ok=True)
 154|             with open(self.state_path, 'w', encoding='utf-8') as f:
 155|                 json.dump(self.roles_state, f, indent=2, ensure_ascii=False)
 156|         except Exception as e:
 157|             self._get_logger().error(f"Error saving roles_state: {e}")
 158| 
 159|     def _get_available_models(self) -> List[str]:
 160|         models = self.models_config.get('available_openrouter_models', [])
 161|         result = []
 162|         
 163|         for m in models:
 164|             if isinstance(m, str):
 165|                 cleaned = m.strip()
 166|                 if cleaned:
 167|                     result.append(cleaned)
 168|             elif isinstance(m, dict):
 169|                 key = m.get("key", "")
 170|                 if key and isinstance(key, str):
 171|                     cleaned = key.strip()
 172|                     if cleaned:
 173|                         result.append(cleaned)
 174|         
 175|         if not result:
 176|             raise RuntimeError("No available models in pool. Run openrouter_models_updater.py first.")
 177|         
 178|         return result
 179| 
 180|     async def get_model_for_role(
 181|         self,
 182|         role_key: str,
 183|         task_id: Optional[str] = None,
 184|         override_model_id: Optional[str] = None,
 185|         exclude: Optional[List[str]] = None,
 186|         **kwargs
 187|     ) -> str:
 188|         """Возвращает model_id (строку) для роли."""
 189|         await self._ensure_initialized()
 190|         logger = self._get_logger()
 191|         
 192|         if override_model_id:
 193|             return override_model_id
 194|         
 195|         binding_key = f"{role_key}:{task_id}" if task_id else role_key
 196| 
 197|         if hasattr(self, "_bindings") and binding_key in self._bindings:
 198|             return self._bindings[binding_key]
 199| 
 200|         if task_id:
 201|             role_state = self.roles_state.get(role_key, {})
 202|             binding = role_state.get(task_id)
 203|             if binding and binding.get("status") == "active":
 204|                 model_id = binding["primary"]
 205|                 if not hasattr(self, "_bindings"): self._bindings = {}
 206|                 self._bindings[binding_key] = model_id
 207|                 return model_id
 208| 
 209|         pool_raw = self._get_available_models()
 210|         pool = []
 211|         for m in pool_raw:
 212|             m_key = m if isinstance(m, str) else m.get("key")
 213|             if exclude and m_key in exclude:
 214|                 continue
 215|             pool.append(m)
 216|             
 217|         if not pool:
 218|             if exclude:
 219|                 logger.warning(f"[BINDING] Failover ineffective for '{role_key}' after excluding {exclude}. Falling back.")
 220|                 pool = pool_raw
 221|             
 222|             if not pool:
 223|                 raise RuntimeError(f"No available models for role '{role_key}'")
 224| 
 225|         seed_str = role_key + (task_id or "")
 226|         if exclude:
 227|             seed_str += "".join(exclude)
 228|             
 229|         seed = int(hashlib.md5(seed_str.encode('utf-8')).hexdigest(), 16)
 230|         index = seed % len(pool)
 231|         selected = pool[index]
 232|         model_id = selected["key"] if isinstance(selected, dict) else selected
 233| 
 234|         if not hasattr(self, "_bindings"): self._bindings = {}
 235|         self._bindings[binding_key] = model_id
 236| 
 237|         if not exclude:
 238|             if task_id:
 239|                 if role_key not in self.roles_state:
 240|                     self.roles_state[role_key] = {}
 241|                 self.roles_state[role_key][task_id] = {"primary": model_id, "status": "active"}
 242|                 self._save_state()
 243|                 logger.info(f"[BINDING] Cache MISS: {role_key}:{task_id} -> {model_id}")
 244|             else:
 245|                 logger.info(f"[BINDING] Memory MISS: {role_key} -> {model_id}")
 246|         else:
 247|             logger.info(f"[BINDING] Failover for {role_key}: {model_id}")
 248| 
 249|         return model_id
 250| 
 251|     async def get_prompt(self, role_key: str) -> str:
 252|         await self._ensure_initialized()
 253|         return self._prompt_registry.get_prompt(role_key)
 254| 
 255|     async def switch_binding(self, role_key: str, new_model_id: str, reason: str = "") -> bool:
 256|         await self._ensure_initialized()
 257|         with self._get_state_lock():
 258|             if "defaults" not in self.roles_state:
 259|                 self.roles_state["defaults"] = {}
 260|             self.roles_state["defaults"][role_key] = new_model_id
 261|             self._save_state()
 262|             self._get_logger().info(f"Switch binding for {role_key} to {new_model_id}. Reason: {reason}")
 263|             return True
 264| 
 265|     async def get_state(self) -> Dict:
 266|         await self._ensure_initialized()
 267|         return self.roles_state
 268| 
 269|     async def get_fixed_model(self, role_key: str) -> str:
 270|         await self._ensure_initialized()
 271|         with self._get_state_lock():
 272|             default_model = self.roles_state.get("defaults", {}).get(role_key)
 273|             if default_model:
 274|                 return default_model
 275|             
 276|             pool = self._get_available_models()
 277|             if not pool:
 278|                 active = self.models_config.get("active_models", {})
 279|                 if role_key in active:
 280|                     return active[role_key].get("model_id")
 281|                 raise RuntimeError(f"No available models in pool for role '{role_key}'")
 282|             
 283|             seed_str = f"{role_key}"
 284|             seed = int(hashlib.md5(seed_str.encode()).hexdigest(), 16)
 285|             selected = pool[seed % len(pool)]
 286|             model_id = selected.get("key") if isinstance(selected, dict) else selected
 287|             return model_id
 288| 
 289|     async def is_department_available(self, dept: str) -> bool:
 290|         await self._ensure_initialized()
 291|         lock = self._dept_locks.get(dept)
 292|         if not lock: return True
 293|         return lock["state"] == DEPT_STATE_IDLE
 294| 
 295|     async def lock_department(self, dept: str, state: str, locked_by: str = "system") -> bool:
 296|         await self._ensure_initialized()
 297|         if not await self.is_department_available(dept): return False
 298|         self._dept_locks[dept] = {
 299|             "state": state,
 300|             "locked_by": locked_by,
 301|             "expires": datetime.now() + timedelta(seconds=LOCK_TTL_SECONDS) if LOCK_TTL_SECONDS else None
 302|         }
 303|         return True
 304| 
 305|     async def unlock_department(self, dept: str):
 306|         await self._ensure_initialized()
 307|         if dept in self._dept_locks:
 308|             self._dept_locks[dept] = {"state": DEPT_STATE_IDLE, "locked_by": None, "expires": None}
 309| 
 310|     async def run_department(self, dept: str, request_data: Dict, caller: str = "system") -> Any:
 311|         await self._ensure_initialized()
 312|         if not await self.is_department_available(dept):
 313|             return {"error": f"Department {dept} is busy"}
 314|         
 315|         await self.lock_department(dept, DEPT_STATE_BUSY_BY_SYSTEM, locked_by=caller)
 316|         try:
 317|             roles = DEPT_ROLES.get(dept, [])
 318|             if not roles:
 319|                 return {"error": f"No roles for department {dept}"}
 320|             return await self._run_cycle(dept, roles, request_data, caller)
 321|         finally:
 322|             self.unlock_department(dept)
 323| 
 324|     async def _run_cycle(self, dept: str, roles: List[str], request_data: Dict, caller: str) -> Any:
 325|         # LAZY IMPORTS
 326|         from core.model_management import ModelManager
 327| 
 328|         message = request_data.get("message") or ""
 329|         session_id = request_data.get("session_id", "default")
 330|         is_formal = "[TASK]" in message
 331|         
 332|         current_result = message
 333|         last_json = None
 334| 
 335|         mm = ModelManager()
 336| 
 337|         for i, role_key in enumerate(roles):
 338|             system_prompt = await self.get_prompt(role_key)
 339|             model_id = await self.get_model_for_role(role_key, task_id=session_id)
 340|             model = await mm.get_model(model_id)
 341|             
 342|             user_prompt = current_result if i > 0 else message
 343|             if i > 0:
 344|                 user_prompt = f"Улучши результат коллеги:\n\n{current_result}"
 345|             
 346|             raw_response = await model.generate(user_prompt, system_prompt=system_prompt)
 347|             current_result = raw_response
 348|             
 349|             if is_formal:
 350|                 try:
 351|                     start = raw_response.find('{')
 352|                     end = raw_response.rfind('}')
 353|                     if start != -1 and end != -1:
 354|                         last_json = json.loads(raw_response[start:end+1])
 355|                 except:
 356|                     pass
 357| 
 358|         return last_json if (is_formal and last_json) else current_result
```


## SOURCE_EVIDENCE: core/llm_integrations/gcb_engine.py
```
REPOSITORY: lhc-lab/AI-Colab
SOURCE: HF_DATASET
REVISION: UNKNOWN
FILE: core/llm_integrations/gcb_engine.py
CONTENT_SHA256: f2476a80ae017f6fae7cd90409ab26c869d88a88c42b7501b7fca7b8f14f93f9
BYTES: 4325
LINES: 104
MODE: VERBATIM
TRUNCATED: false
EVIDENCE_LEVEL: CODE_READ
```
```text
   1| import asyncio
   2| import json
   3| import os
   4| from pathlib import Path
   5| from datetime import datetime
   6| import uuid
   7| import aiofiles
   8| 
   9| class GCBEngine:
  10|     """
  11|     Gemini CLI Bridge Engine.
  12|     Управляет очередью команд для выполнения в локальном терминале.
  13|     """
  14|     def __init__(self, queue_path: str = "D:\\Gemini\\AIColab\\sessions\\gcb_queue.json"):
  15|         self.queue_path = Path(queue_path)
  16|         self.queue_path.parent.mkdir(parents=True, exist_ok=True)
  17|         if not self.queue_path.exists():
  18|             with open(self.queue_path, "w", encoding="utf-8") as f:
  19|                 json.dump([], f)
  20| 
  21|     async def add_command(self, command: str, description: str = "") -> str:
  22|         """Добавляет команду в очередь."""
  23|         cmd_id = f"cmd_{uuid.uuid4().hex[:8]}"
  24|         new_entry = {
  25|             "id": cmd_id,
  26|             "command": command,
  27|             "description": description,
  28|             "status": "pending",
  29|             "created_at": datetime.now().isoformat(),
  30|             "completed_at": None,
  31|             "output": "",
  32|             "exit_code": None
  33|         }
  34|         
  35|         async with aiofiles.open(self.queue_path, mode="r", encoding="utf-8") as f:
  36|             queue = json.loads(await f.read())
  37|         
  38|         queue.append(new_entry)
  39|         
  40|         async with aiofiles.open(self.queue_path, mode="w", encoding="utf-8") as f:
  41|             await f.write(json.dumps(queue, indent=2, ensure_ascii=False))
  42|             
  43|         return cmd_id
  44| 
  45|     async def get_queue(self, status: str = None) -> list:
  46|         """Возвращает список команд."""
  47|         async with aiofiles.open(self.queue_path, mode="r", encoding="utf-8") as f:
  48|             queue = json.loads(await f.read())
  49|         
  50|         if status:
  51|             return [cmd for cmd in queue if cmd["status"] == status]
  52|         return queue
  53| 
  54|     async def update_command_status(self, cmd_id: str, status: str, output: str = "", exit_code: int = None):
  55|         """Обновляет статус и результат выполнения команды."""
  56|         async with aiofiles.open(self.queue_path, mode="r", encoding="utf-8") as f:
  57|             queue = json.loads(await f.read())
  58|             
  59|         for cmd in queue:
  60|             if cmd["id"] == cmd_id:
  61|                 cmd["status"] = status
  62|                 if output:
  63|                     cmd["output"] = output
  64|                 if exit_code is not None:
  65|                     cmd["exit_code"] = exit_code
  66|                 if status in ["completed", "failed"]:
  67|                     cmd["completed_at"] = datetime.now().isoformat()
  68|                 break
  69|                 
  70|         async with aiofiles.open(self.queue_path, mode="w", encoding="utf-8") as f:
  71|             await f.write(json.dumps(queue, indent=2, ensure_ascii=False))
  72| 
  73|     async def execute_local(self, cmd_id: str):
  74|         """
  75|         Выполняет команду локально (если запущено в окружении с доступом к shell).
  76|         ВНИМАНИЕ: Это потенциально небезопасно и требует подтверждения.
  77|         """
  78|         queue = await self.get_queue()
  79|         target_cmd = next((c for c in queue if c["id"] == cmd_id), None)
  80|         
  81|         if not target_cmd:
  82|             return {"error": "Command not found"}
  83|             
  84|         await self.update_command_status(cmd_id, "executing")
  85|         
  86|         try:
  87|             process = await asyncio.create_subprocess_shell(
  88|                 target_cmd["command"],
  89|                 stdout=asyncio.subprocess.PIPE,
  90|                 stderr=asyncio.subprocess.PIPE
  91|             )
  92|             stdout, stderr = await process.communicate()
  93|             
  94|             output = stdout.decode().strip() + "\n" + stderr.decode().strip()
  95|             exit_code = process.returncode
  96|             
  97|             status = "completed" if exit_code == 0 else "failed"
  98|             await self.update_command_status(cmd_id, status, output, exit_code)
  99|             
 100|             return {"status": status, "output": output, "exit_code": exit_code}
 101|             
 102|         except Exception as e:
 103|             await self.update_command_status(cmd_id, "failed", str(e), -1)
 104|             return {"status": "failed", "output": str(e), "exit_code": -1}
```


## SOURCE_EVIDENCE: core/gemini_cli_executor.py
```
REPOSITORY: lhc-lab/AI-Colab
SOURCE: HF_DATASET
REVISION: UNKNOWN
FILE: core/gemini_cli_executor.py
CONTENT_SHA256: 1a6b22944231dea60e1e599fda37d6e6a8a0a7e21dbd292fe93ed9c571e93845
BYTES: 4495
LINES: 126
MODE: VERBATIM
TRUNCATED: false
EVIDENCE_LEVEL: CODE_READ
```
```text
   1| # AIColab/core/gemini_cli_executor.py
   2| """
   3| Gemini CLI Executor — единая точка входа для эфемерных вызовов.
   4| Контракт: asyncio.subprocess_exec → stdin (message) → stdout (JSON) → kill.
   5| """
   6| import asyncio
   7| import json
   8| import logging
   9| import os
  10| import shutil
  11| import tempfile
  12| from pathlib import Path
  13| from typing import Optional
  14| from dotenv import load_dotenv
  15| 
  16| load_dotenv(dotenv_path=Path(__file__).parent.parent / ".env")
  17| 
  18| logger = logging.getLogger(__name__)
  19| FALLBACK_MSG = "[Ошибка: не удалось получить ответ от Админа]"
  20| 
  21| def _resolve_gemini_bin() -> str:
  22|     """Найти бинарник: конфиг → PATH → fallback."""
  23|     try:
  24|         from core.config_loader import load_config
  25|         cfg = load_config("config/gemini_sockets.json", force_reload=True)
  26|         bin_path = cfg.get("gemini_cli_path")
  27|         if bin_path and Path(bin_path).exists():
  28|             return bin_path
  29|     except Exception:
  30|         pass
  31|     
  32|     if path := shutil.which("gemini"):
  33|         return path
  34|         
  35|     fallback = Path(__file__).parent.parent / "integrations" / "gemini_cli.py"
  36|     if fallback.exists():
  37|         return str(fallback)
  38|         
  39|     raise RuntimeError("Gemini CLI not found. Set 'gemini_cli_path' in config.")
  40| 
  41| async def execute(
  42|     mode: str,
  43|     message: str,
  44|     project_path: Optional[str] = None,
  45|     prompt_text: Optional[str] = None,
  46|     timeout: int = 30,
  47|     for_role: Optional[str] = None,
  48|     scope: Optional[str] = None
  49| ) -> str:
  50|     """
  51|     Эфемерный вызов Gemini CLI.
  52|     :return: Текст ответа или fallback-строка (НИКОГДА не кидает исключение наружу)
  53|     """
  54|     try:
  55|         bin_path = _resolve_gemini_bin()
  56|     except RuntimeError as e:
  57|         logger.error(f"[CLI] Binary resolution failed: {e}")
  58|         return FALLBACK_MSG
  59| 
  60|     # Формируем команду: -o json для вывода, -p для промпта
  61|     cmd = [bin_path, "-o", "json"]
  62|     
  63|     # DEBUG
  64|     env_path = Path(__file__).parent.parent / ".env"
  65|     logger.debug(f"[ENV_DEBUG] Path: {env_path}, exists: {env_path.exists()}")
  66|     logger.debug(f"[ENV_DEBUG] GEMINI_API_KEY present: {'GEMINI_API_KEY' in os.environ}")
  67|     logger.debug(f"[ENV_DEBUG] GEMINI_API_KEY value: {os.environ.get('GEMINI_API_KEY', '')[:5]}...")
  68|     
  69|     # Промпт: передаем в headless режиме
  70|     prompt_file = None
  71|     if prompt_text:
  72|         try:
  73|             fd, prompt_file = tempfile.mkstemp(suffix=".txt", prefix="cli_prompt_")
  74|             with os.fdopen(fd, 'w', encoding='utf-8') as f:
  75|                 f.write(prompt_text)
  76|             cmd.extend(["-p", prompt_file])
  77|         except Exception as e:
  78|             logger.warning(f"[CLI] Failed to write prompt temp file: {e}")
  79|     
  80|     cmd_log = cmd.copy()
  81|     logger.debug(f"[CLI] Executing: {' '.join(cmd_log)}, timeout={timeout}s")
  82|     
  83|     proc = None
  84|     try:
  85|         proc = await asyncio.create_subprocess_exec(
  86|             *cmd,
  87|             stdin=asyncio.subprocess.PIPE,
  88|             stdout=asyncio.subprocess.PIPE,
  89|             stderr=asyncio.subprocess.PIPE,
  90|             env=os.environ
  91|         )
  92|         
  93|         stdout, stderr = await asyncio.wait_for(
  94|             proc.communicate(input=message.encode("utf-8")),
  95|             timeout=timeout
  96|         )
  97|         
  98|         if stderr:
  99|             logger.debug(f"[CLI] stderr: {stderr.decode('utf-8', errors='replace')}")
 100| 
 101|         raw = stdout.decode("utf-8", errors="replace").strip()
 102|         if not raw:
 103|             raise ValueError("Empty output from CLI")
 104|             
 105|         try:
 106|             data = json.loads(raw)
 107|             if isinstance(data, dict) and "response" in data:
 108|                 return str(data["response"])
 109|             return raw
 110|         except json.JSONDecodeError:
 111|             return raw
 112|             
 113|     except asyncio.TimeoutError:
 114|         logger.error(f"[CLI] Timeout after {timeout}s (mode={mode})")
 115|         if proc and proc.returncode is None:
 116|             proc.kill()
 117|         return f"[Таймаут: Админ ({mode}) не ответил за {timeout}с]"
 118|     except Exception as e:
 119|         logger.error(f"[CLI] Unexpected error: {e}", exc_info=True)
 120|         return f"[Внутренняя ошибка CLI: {type(e).__name__}]"
 121|     finally:
 122|         if prompt_file and Path(prompt_file).exists():
 123|             try:
 124|                 Path(prompt_file).unlink()
 125|             except Exception:
 126|                 pass
```


## SOURCE_EVIDENCE: core/project_context.py
```
REPOSITORY: lhc-lab/AI-Colab
SOURCE: HF_DATASET
REVISION: UNKNOWN
FILE: core/project_context.py
CONTENT_SHA256: 67b8269c141e23cffde6f4746dcd5c226a2d4fd9eccf89225e155b5d0f82331a
BYTES: 3900
LINES: 95
MODE: VERBATIM
TRUNCATED: false
EVIDENCE_LEVEL: CODE_READ
```
```text
   1| import json
   2| import os
   3| from pathlib import Path
   4| import logging
   5| 
   6| logger = logging.getLogger(__name__)
   7| 
   8| class ProjectContext:
   9|     _instance = None
  10|     
  11|     def __new__(cls):
  12|         if cls._instance is None:
  13|             cls._instance = super().__new__(cls)
  14|         return cls._instance
  15|     
  16|     def __init__(self):
  17|         if not hasattr(self, '_initialized'):
  18|             self._initialized = False
  19|             self.project_path = None
  20|             self.project_id = None
  21|             # Корень папки AIColab (на уровень выше от core/) - нормализуем регистр
  22|             self.base_dir = Path(__file__).resolve().parent.parent
  23|             # Принудительная нормализация к нижнему регистру для Windows
  24|             if os.name == 'nt':
  25|                 self.base_dir = Path(str(self.base_dir).lower())
  26|     
  27|     async def ensure_initialized(self):
  28|         """Ленивая инициализация"""
  29|         if not self._initialized:
  30|             # Всегда смотрим в папку projects в корне AIColab
  31|             projects_dir = self.base_dir / "projects"
  32|             if projects_dir.exists():
  33|                 # Находим последний измененный проект
  34|                 try:
  35|                     projects = sorted(
  36|                         [p for p in projects_dir.iterdir() if p.is_dir()],
  37|                         key=lambda p: p.stat().st_mtime,
  38|                         reverse=True
  39|                     )
  40|                     if projects:
  41|                         self.project_path = projects[0]
  42|                         self.project_id = projects[0].name
  43|                 except Exception as e:
  44|                     logger.warning(f"Ошибка при поиске проектов в {projects_dir}: {e}")
  45|             
  46|             self._initialized = True
  47|     
  48|     def get_current_project_path(self):
  49|         """Получить путь к текущему проекту"""
  50|         if self.project_path and self.project_path.exists():
  51|             return self.project_path
  52|         
  53|         # Fallback: поиск в корне AIColab
  54|         projects_dir = self.base_dir / "projects"
  55|         if projects_dir.exists():
  56|             try:
  57|                 projects = sorted(
  58|                     [p for p in projects_dir.iterdir() if p.is_dir()],
  59|                     key=lambda p: p.stat().st_mtime,
  60|                     reverse=True
  61|                 )
  62|                 if projects:
  63|                     self.project_path = projects[0]
  64|                     self.project_id = projects[0].name
  65|                     return projects[0]
  66|             except Exception as e:
  67|                 logger.warning(f"Ошибка поиска проекта: {e}")
  68|         
  69|         # Дефолтный проект внутри корня AIColab
  70|         default_project = projects_dir / "default"
  71|         default_project.mkdir(parents=True, exist_ok=True)
  72|         self.project_path = default_project
  73|         self.project_id = "default"
  74|         return default_project
  75| 
  76|     def get_role_log_path(self, role: str, log_type: str, filename: str) -> Path:
  77|         """Получить путь к логу конкретной роли."""
  78|         project_path = self.get_current_project_path()
  79|         # logs/subjects/{role}/{log_type}/{filename}
  80|         log_dir = project_path / "logs" / "subjects" / role / log_type
  81|         log_dir.mkdir(parents=True, exist_ok=True)
  82|         return log_dir / filename
  83|     
  84|     def get_state(self):
  85|         return {
  86|             'state': 'initialized' if self._initialized else 'uninitialized',
  87|             'project_id': self.project_id,
  88|             'project_path': str(self.project_path) if self.project_path else None
  89|         }
  90|     
  91|     @classmethod
  92|     def get_instance(cls):
  93|         if cls._instance is None:
  94|             cls._instance = cls()
  95|         return cls._instance
```


## SOURCE_EVIDENCE: start_server.py
```
REPOSITORY: lhc-lab/AI-Colab
SOURCE: HF_DATASET
REVISION: UNKNOWN
FILE: start_server.py
CONTENT_SHA256: NOT_VALID (локальная копия 3020 B != размер на HF 3048 B; пробельные символы могли отличаться)
HF_STAT_BYTES: 3048
MODE: VERBATIM_TEXT_AS_RETURNED_BY_TOOL (копия, возможна потеря хвостовых пробелов; на смысл кода не влияет)
TRUNCATED: false
EVIDENCE_LEVEL: CODE_READ
```
```text
   1| #!/usr/bin/env python3
   2| """
   3| Запуск AIColab с предварительной очисткой
   4| """
   5| import os
   6| import sys
   7| from pathlib import Path
   8| import shutil
   9| import socket
  10| import psutil
  11| import time
  12| import importlib
  13| from core.project_context import ProjectContext
  14| 
  15| # Очистка Python кэша
  16| def clean_python_cache():
  17|     root = Path(__file__).parent
  18|     for cache_dir in root.rglob("__pycache__"):
  19|         shutil.rmtree(cache_dir, ignore_errors=True)
  20| 
  21|     for pyc_file in root.rglob("*.pyc"):
  22|         pyc_file.unlink(missing_ok=True)
  23| 
  24|     print("Python cache cleaned")
  25| 
  26| # Проверка порта
  27| def ensure_port_free(port=5000):
  28| 
  29|     # Убиваем процессы на порту
  30|     for conn in psutil.net_connections():
  31|         if hasattr(conn.laddr, 'port') and conn.laddr.port == port:
  32|             try:
  33|                 p = psutil.Process(conn.pid)
  34|                 if 'python' in p.name().lower():
  35|                     print(f"Terminating process {p.pid} ({p.name()}) on port {port}")
  36|                     p.terminate()
  37|                     p.wait(timeout=5)
  38|             except (psutil.NoSuchProcess, psutil.AccessDenied):
  39|                 pass
  40| 
  41|     # Даем время на завершение процессов
  42|     time.sleep(1)
  43| 
  44|     # Проверяем доступность порта
  45|     sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  46|     try:
  47|         sock.bind(('localhost', port))
  48|         print(f"Port {port} is free")
  49|     except OSError:
  50|         raise RuntimeError(f"Port {port} is still busy after cleanup")
  51|     finally:
  52|         sock.close()
  53| 
  54| def ensure_project_context():
  55|     """Убедиться, что контекст проекта инициализирован."""
  56|     if not ProjectContext.is_initialized():
  57|         # Автоматически инициализировать последний проект
  58|         projects_dir = Path("projects")
  59|         if projects_dir.exists():
  60|             # Найти последний проект
  61|             projects = list(projects_dir.glob("*/project_info.json"))
  62|             if projects:
  63|                 latest = max(projects, key=lambda p: p.stat().st_mtime)
  64|                 project_path = latest.parent
  65|                 ProjectContext.initialize(str(project_path))
  66|                 print(f"📁 Автоинициализация проекта: {project_path.name}")
  67| 
  68| 
  69| if __name__ == "__main__":
  70|     # Устанавливаем PYTHONPATH, чтобы импорты работали корректно
  71|     sys.path.insert(0, str(Path(__file__).parent))
  72| 
  73|     clean_python_cache()
  74|     ensure_port_free(5000)
  75| 
  76|     # Автоинициализация контекста
  77|     ensure_project_context()
  78| 
  79|     # Запускаем Uvicorn
  80|     print("Starting Uvicorn server...")
  81|     # Используем os.system для запуска, чтобы избежать проблем с блокировкой в текущем процессе
  82|     os.system("uvicorn app:app --host 127.0.0.1 --port 5000 --workers 2 --reload")
```


## SOURCE_EVIDENCE: config/gemini_sockets.json
```
REPOSITORY: lhc-lab/AI-Colab
SOURCE: HF_DATASET
REVISION: UNKNOWN
FILE: config/gemini_sockets.json
CONTENT_SHA256: f72874ca6d3f6d926626c6d2621c0a379a69d8b0869de7e07a7ae3f44dbfd080
BYTES: 777
LINES: 33
MODE: VERBATIM
TRUNCATED: false
EVIDENCE_LEVEL: CODE_READ
```
```text
   1| {
   2|   "main_server": {
   3|     "host": "127.0.0.1",
   4|     "port": 5005
   5|   },
   6|   "agents": {
   7|     "gemini_console": {
   8|       "port": 5001,
   9|       "script": "gemini_mcp_server.py",
  10|       "prompt": "gemini_console.txt"
  11|     },
  12|     "secretary_chief": {
  13|       "port": 5002,
  14|       "script": "gemini_mcp_server.py",
  15|       "prompt": "gemini_secretary_chief.txt"
  16|     },
  17|     "secretary_ceo": {
  18|       "port": 5003,
  19|       "script": "gemini_mcp_server.py",
  20|       "prompt": "gemini_secretary_ceo.txt"
  21|     },
  22|     "consultant_strategic": {
  23|       "port": 5004,
  24|       "script": "gemini_mcp_server.py",
  25|       "prompt": "gemini_strategic_orchestrator.txt"
  26|     },
  27|     "audit_orchestrator": {
  28|       "port": 5006,
  29|       "script": "gemini_mcp_server.py",
  30|       "prompt": "gemini_audit_orchestrator.txt"
  31|     }
  32|   }
  33| }
```