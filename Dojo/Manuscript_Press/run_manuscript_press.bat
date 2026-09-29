@echo off
cd /d "%~dp0"
set PYTHONPATH=%CD%
python -m src.production_runner %*