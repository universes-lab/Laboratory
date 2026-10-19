import subprocess
import sys
import os
import time
from pathlib import Path

# Роли и порты
agents = [
    (5001, "gemini_console", "docs/prompts/Gemini/gemini_console.txt"),
    (5002, "secretary_chief", "docs/prompts/Gemini/gemini_secretary_chief.txt"),
    (5003, "secretary_ceo", "docs/prompts/Gemini/gemini_secretary_ceo.txt"),
    (5004, "consultant_strategic", "docs/prompts/Gemini/gemini_strategic_orchestrator.txt"),
    (5005, "audit_orchestrator", "docs/prompts/Gemini/gemini_audit_orchestrator.txt"),
]

project_root = Path(r"D:\gemini\AIColab")

for port, role, prompt in agents:
    env = os.environ.copy()
    env["GEMINI_PORT"] = str(port)
    env["GEMINI_ROLE"] = role
    env["GEMINI_PROMPT"] = str(project_root / prompt)
    
    cmd = [sys.executable, str(project_root / "gemini_mcp_server.py")]
    subprocess.Popen(cmd, env=env, cwd=str(project_root))
    print(f"Launched {role} on {port}")
