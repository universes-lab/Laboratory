@echo off
cd /d "%~dp0"
set PYTHONPATH=%CD%
.venv\Scripts\python.exe -m src.production_runner