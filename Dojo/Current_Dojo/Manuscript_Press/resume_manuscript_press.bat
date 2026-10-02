@echo off
cd /d "%~dp0"
set PYTHONPATH=%CD%
if "%~1"=="" goto usage
if "%~2"=="" goto usage
if "%~3"=="" (
  .venv\Scripts\python.exe -m src.production_runner --start-marker %1 --prior-run-dir %2
  exit /b %ERRORLEVEL%
)
.venv\Scripts\python.exe -m src.production_runner --start-marker %1 --prior-run-dir %2 --end-marker %3
exit /b %ERRORLEVEL%
:usage
echo resume_manuscript_press.bat START_MARKER PRIOR_RUN_DIR [END_MARKER]
exit /b 2