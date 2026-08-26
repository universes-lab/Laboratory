@echo off
set PYTHONPATH=D:\Gemini\dojo
cd /d D:\Gemini\dojo

echo === Building compiled_input for package 02 ===
python -c "from src.builder import build_prompt; build_prompt('02', '02_T00')"

echo === Running generator ===
python -m src.generator --run_id "02_T00" --temperature 0.0

echo === Checking artifacts ===
if exist logs\runs\02_T00\raw_output.md (echo raw_output.md OK) else (echo raw_output.md MISSING)
if exist logs\runs\02_T00\metadata.yaml (echo metadata.yaml OK) else (echo metadata.yaml MISSING)
if exist logs\runs\02_T00\constants_check.yaml (echo constants_check.yaml OK) else (echo constants_check.yaml MISSING)
if exist Output\02_T00.manuscript.md (echo manuscript.md OK) else (echo manuscript.md MISSING)
pause