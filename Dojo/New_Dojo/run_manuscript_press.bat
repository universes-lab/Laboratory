@echo off
setlocal

cd /d "%~dp0"

set "PYTHONPATH=%CD%"
set "RUN_ID=02_T00"
set "TEMPERATURE=0.0"

if not "%~1"=="" set "RUN_ID=%~1"
if not "%~2"=="" set "TEMPERATURE=%~2"

echo ============================================================
echo MANUSCRIPT PRESS - PAIRED RUN
echo ============================================================
echo Project root: %CD%
echo Run ID: %RUN_ID%
echo Temperature: %TEMPERATURE%
echo.

echo [PRECHECK] Checking stale authorization...

if exist "state\PART2_AUTHORIZED" (
    echo ERROR: state\PART2_AUTHORIZED already exists.
    echo Fresh paired run aborted.
    pause
    exit /b 1
)

if not exist "Gemma.md" (
    echo ERROR: Gemma.md not found in project root.
    pause
    exit /b 1
)

if not exist "src\paired_runner.py" (
    echo ERROR: src\paired_runner.py not found.
    pause
    exit /b 1
)

echo [PRECHECK] PASS
echo.
echo [RUN] Starting resident paired runner...
echo.

python -m src.paired_runner --run_id "%RUN_ID%" --temperature "%TEMPERATURE%"

set "RC=%ERRORLEVEL%"

if not "%RC%"=="0" (
    echo.
    echo ERROR: paired_runner failed with exit code %RC%.
    pause
    exit /b %RC%
)

echo.
echo Paired run completed.
rem pause
exit /b 0