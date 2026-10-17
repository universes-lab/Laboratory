@echo off
setlocal EnableExtensions

cd /d "%~dp0"

set "SELF=%~nx0"
set "STASHED=0"
set "DIRTY=0"

echo === SAFE SYNC: HONC ===
echo.

git rev-parse --is-inside-work-tree >nul 2>&1
if errorlevel 1 (
    echo ERROR: This folder is not a Git repository.
    exit /b 1
)

echo [1/5] Fetching origin...
git fetch origin
if errorlevel 1 exit /b 1

echo.
echo [2/5] Checking local changes...

for /f "delims=" %%A in ('git status --porcelain -- . ":(exclude)%SELF%"') do (
    set "DIRTY=1"
)

if "%DIRTY%"=="0" goto PULL

echo Local changes detected.
echo Saving them temporarily...

git stash push -u -m "safe_sync temporary stash" -- . ":(exclude)%SELF%"
if errorlevel 1 exit /b 1

set "STASHED=1"

:PULL
echo.
echo [3/5] Updating local main...

git pull --rebase origin main
if errorlevel 1 (
    echo.
    echo ERROR: pull/rebase stopped.
    echo Local stash was NOT discarded.
    exit /b 1
)

if "%STASHED%"=="0" goto STATUS

echo.
echo [4/5] Restoring local changes...

git stash pop
if errorlevel 1 (
    echo.
    echo ATTENTION: remote update succeeded,
    echo but restoring local changes produced a conflict.
    echo The stash was preserved by Git.
    exit /b 1
)

:STATUS
echo.
echo [5/5] Final status...
git status --short --branch

echo.
echo SAFE SYNC COMPLETE.
endlocal