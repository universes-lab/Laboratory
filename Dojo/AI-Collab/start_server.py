#!/usr/bin/env python3
"""
Запуск AIColab с предварительной очисткой
"""
import os
import sys
from pathlib import Path
import shutil
import socket
import psutil
import time
import importlib
from core.project_context import ProjectContext

# Очистка Python кэша
def clean_python_cache():
    root = Path(__file__).parent
    for cache_dir in root.rglob("__pycache__"):
        shutil.rmtree(cache_dir, ignore_errors=True)
    
    for pyc_file in root.rglob("*.pyc"):
        pyc_file.unlink(missing_ok=True)
    
    print("Python cache cleaned")

# Проверка порта
def ensure_port_free(port=5000):
    
    # Убиваем процессы на порту
    for conn in psutil.net_connections():
        if hasattr(conn.laddr, 'port') and conn.laddr.port == port:
            try:
                p = psutil.Process(conn.pid)
                if 'python' in p.name().lower():
                    print(f"Terminating process {p.pid} ({p.name()}) on port {port}")
                    p.terminate()
                    p.wait(timeout=5)
            except (psutil.NoSuchProcess, psutil.AccessDenied):
                pass
    
    # Даем время на завершение процессов
    time.sleep(1)

    # Проверяем доступность порта
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        sock.bind(('localhost', port))
        print(f"Port {port} is free")
    except OSError:
        raise RuntimeError(f"Port {port} is still busy after cleanup")
    finally:
        sock.close()

def ensure_project_context():
    """Убедиться, что контекст проекта инициализирован."""
    if not ProjectContext.is_initialized():
        # Автоматически инициализировать последний проект
        projects_dir = Path("projects")
        if projects_dir.exists():
            # Найти последний проект
            projects = list(projects_dir.glob("*/project_info.json"))
            if projects:
                latest = max(projects, key=lambda p: p.stat().st_mtime)
                project_path = latest.parent
                ProjectContext.initialize(str(project_path))
                print(f"📁 Автоинициализация проекта: {project_path.name}")
    

if __name__ == "__main__":
    # Устанавливаем PYTHONPATH, чтобы импорты работали корректно
    sys.path.insert(0, str(Path(__file__).parent))

    clean_python_cache()
    ensure_port_free(5000)
    
    # Автоинициализация контекста
    ensure_project_context()
    
    # Запускаем Uvicorn
    print("Starting Uvicorn server...")
    # Используем os.system для запуска, чтобы избежать проблем с блокировкой в текущем процессе
    os.system("uvicorn app:app --host 127.0.0.1 --port 5000 --workers 2 --reload")
