@echo off
setlocal EnableExtensions

set "PROJECT_ROOT=%~dp0"
cd /d "%PROJECT_ROOT%"

set "PYTHON=E:\Gemini\Unseen_University_Workshops\OmniVoice_latest.git\.venv\Scripts\python.exe"

if not exist "%PYTHON%" (
    echo ERROR: Python not found:
    echo %PYTHON%
    exit /b 1
)

if not exist "%PROJECT_ROOT%chronicles_tts_runner.py" (
    echo ERROR: chronicles_tts_runner.py not found in:
    echo %PROJECT_ROOT%
    exit /b 1
)

echo Chronicles TTS - OmniVoice 0.2.1
echo Root: %PROJECT_ROOT%
echo.

"%PYTHON%" "%PROJECT_ROOT%chronicles_tts_runner.py" %*
set "RC=%ERRORLEVEL%"

if not "%RC%"=="0" (
    echo.
    echo ERROR: runner exited with code %RC%
)

endlocal & exit /b %RC%
