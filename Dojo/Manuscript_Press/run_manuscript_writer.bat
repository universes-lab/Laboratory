@echo off
echo ========================================
echo  MANUSCRIPT WRITER — PRODUCTION RUN
echo  run_id: 01_T00
echo  temperature: 0.0
echo ========================================
echo.
echo [1/4] Setting PYTHONPATH...
set PYTHONPATH=D:\Gemini\dojo

echo [2/4] Running generator...
cd /d D:\Gemini\dojo
python -m src.generator --run_id "01_T00" --temperature 0.0

echo.
echo [3/4] Checking artifacts...
if exist logs\runs\01_T00\raw_output.md (
  echo   ✅ raw_output.md exists
) else (
  echo   ❌ raw_output.md MISSING
)
if exist logs\runs\01_T00\metadata.yaml (
  echo   ✅ metadata.yaml exists
) else (
  echo   ❌ metadata.yaml MISSING
)
if exist logs\runs\01_T00\constants_check.yaml (
  echo   ✅ constants_check.yaml exists
) else (
  echo   ❌ constants_check.yaml MISSING
)
if exist Output\01_T00.manuscript.md (
  echo   ✅ manuscript.md exists
) else (
  echo   ❌ manuscript.md MISSING
)

echo.
echo [4/4] Done.
pause