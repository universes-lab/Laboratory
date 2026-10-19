import subprocess
import sys
import time
import os
from pathlib import Path

# Путь к директории проекта
project_dir = Path("D:\\gemini")
app_dir = project_dir / "AI-colab"

# Путь к файлу лога
log_file_path = app_dir / "logs" / "uvicorn_out.log"

with open(log_file_path, "w", encoding="utf-8") as log_file:
    if sys.platform == "win32":
        # На Windows используем shell=True для корректной обработки команды
        process = subprocess.Popen(
            "uvicorn app:app --host 0.0.0.0 --port 5000 --workers 4", 
            cwd=app_dir, 
            shell=True, 
            stdout=log_file, 
            stderr=subprocess.STDOUT
        )
    else:
        process = subprocess.Popen(
            ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "5000", "--workers", "4"],
            cwd=app_dir, 
            stdout=log_file, 
            stderr=subprocess.STDOUT
        )

print(f"Uvicorn process started with PID: {process.pid}. Output redirected to {log_file_path}")
# Дождемся, пока сервер инициализируется
time.sleep(15)
