@echo off
echo ========================================
echo  MANUSCRIPT WRITER — SHORT INFERENCE TEST
echo ========================================
set PYTHONPATH=D:\Gemini\dojo
cd /d D:\Gemini\dojo
python -m src.test_inference > test.txt 2>&1
pause