@echo off
setlocal

cd /d "%~dp0"

set "PYTHONPATH=%CD%"
set "RUN_ID=01_T00"
set "TEMPERATURE=0.0"

if not "%~1"=="" set "RUN_ID=%~1"
if not "%~2"=="" set "TEMPERATURE=%~2"

echo ============================================================
echo MANUSCRIPT PRESS - PILOT PRODUCTION RUNNER
echo ============================================================
echo Project root: %CD%
echo Run ID: %RUN_ID%
echo Temperature: %TEMPERATURE%
echo.

echo [PRECHECK] Checking for stale authorization...

if exist "state\PART2_AUTHORIZED" (
    echo ERROR: state\PART2_AUTHORIZED already exists.
    echo Fresh pilot runner execution aborted.
rem     pause
    exit /b 1
)

if not exist "Gemma.md" (
    echo ERROR: Gemma.md not found in project root.
rem     pause
    exit /b 1
)

if not exist "src\production_runner.py" (
    echo ERROR: src\production_runner.py not found.
rem     pause
    exit /b 1
)

echo [PRECHECK] PASS
echo.
echo [RUN] Starting pilot production runner...
echo.

python -m src.production_runner --run_id "%RUN_ID%" --temperature "%TEMPERATURE%"

set "RC=%ERRORLEVEL%"

if not "%RC%"=="0" (
    echo.
    echo ERROR: production_runner failed with exit code %RC%.
    exit /b %RC%
)

echo.
echo Pilot production runner completed.
rem pause
exit /b 0
