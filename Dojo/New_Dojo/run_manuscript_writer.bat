@echo off
setlocal enabledelayedexpansion

echo ============================================================
echo  MANUSCRIPT WRITER — PRODUCTION RUN (Package 01)
echo ============================================================
echo.

set PYTHONPATH=D:\Gemini\dojo
cd /d D:\Gemini\dojo

echo [1/5] Building compiled_input for Package 01...
python -m src.builder --package_id "01" --run_id "01_T00"
if errorlevel 1 (
    echo ERROR: Builder failed. Check input files.
    pause
    exit /b 1
)
echo   ✅ compiled_input.txt created
echo.

echo [2/5] Running generator...
python -m src.generator --run_id "01_T00" --temperature 0.0
if errorlevel 1 (
    echo ERROR: Generator failed.
    pause
    exit /b 1
)
echo   ✅ Generation complete
echo.

echo [3/5] Checking artifacts...
set MISSING=0

if exist logs\runs\01_T00\raw_output.md (
    echo   ✅ raw_output.md exists
) else (
    echo   ❌ raw_output.md MISSING
    set MISSING=1
)

if exist logs\runs\01_T00\metadata.yaml (
    echo   ✅ metadata.yaml exists
) else (
    echo   ❌ metadata.yaml MISSING
    set MISSING=1
)

if exist logs\runs\01_T00\constants_check.yaml (
    echo   ✅ constants_check.yaml exists
) else (
    echo   ❌ constants_check.yaml MISSING
    set MISSING=1
)

if exist Output\01_T00.manuscript.md (
    echo   ✅ manuscript.md exists
) else (
    echo   ❌ manuscript.md MISSING
    set MISSING=1
)

echo.

if !MISSING! == 0 (
    echo [4/5] ✅ All artifacts present.
) else (
    echo [4/5] ❌ Some artifacts missing. Check logs.
)

echo [5/5] Done.
