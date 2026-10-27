@echo off
setlocal

set "SRC=E:\Gemini\Dojo\AI-Collab"
set "DST=E:\Gemini\Post_TOE_Physics\Laboratory\Dojo\AI-Collab"

echo === SAMURAI - ARCHIVE SYNC ===

robocopy "%SRC%" "%DST%" /E /XO /R:2 /W:1 /XJ

set "RC=%ERRORLEVEL%"

if %RC% GEQ 8 (
    echo ERROR: Robocopy failed. Code: %RC%
) else (
    echo SUCCESS: Archive updated. Code: %RC%
)

pause
