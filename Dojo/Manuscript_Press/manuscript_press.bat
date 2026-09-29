@echo off
REM cd /d E:\Gemini\dojo
set PYTHONPATH=%CD%
python -m src.production_runner --start-marker MP:0170 --prior-run-dir Output/runs/20260923T144611Z