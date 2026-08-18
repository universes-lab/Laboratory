@echo off
setlocal EnableExtensions EnableDelayedExpansion

rem ============================================================
rem DOJO GIT SAFETY v1 - AUTHORIZED ROLLBACK
rem Not exposed through dojo_git.bat menu.
rem Uses history-preserving tree restore + RECOVERY commit.
rem ============================================================

set "PROD_ROOT=D:\Gemini\dojo"
set "ROOT=%PROD_ROOT%"
set "GIT=git"

if /I "%DOJO_GIT_TEST_MODE%"=="1" (
    if not defined DOJO_GIT_TEST_ROOT (
        echo [BLOCKED: TEST_ROOT_REQUIRED]
        exit /b 90
    )
    set "ROOT=%DOJO_GIT_TEST_ROOT%"
)

for %%I in ("%ROOT%") do set "ROOT=%%~fI"
for %%I in ("%PROD_ROOT%") do set "PROD_ROOT=%%~fI"

if /I not "%DOJO_GIT_TEST_MODE%"=="1" (
    if /I not "%ROOT%"=="%PROD_ROOT%" (
        echo [BLOCKED: INVALID_ROOT]
        exit /b 91
    )
)

if "%~1"=="" (
    echo [BLOCKED: TARGET_COMMIT_REQUIRED]
    echo Usage:
    echo   git_tools\rollback_authorized.bat ^<commit-hash^> ^<authorization-token^>
    exit /b 2
)
if "%~2"=="" (
    echo [BLOCKED: ROLLBACK_AUTHORIZATION_REQUIRED]
    exit /b 3
)

set "TARGET_HASH=%~1"
set "AUTH_TOKEN=%~2"

if not exist "%ROOT%\.git\" (
    echo [BLOCKED: DOJO_REPOSITORY_NOT_INITIALIZED]
    exit /b 4
)

where git >nul 2>&1
if errorlevel 1 (
    echo [BLOCKED: GIT_NOT_FOUND]
    exit /b 5
)

cd /d "%ROOT%" || (
    echo [BLOCKED: ROOT_NOT_ACCESSIBLE]
    exit /b 6
)

set "REMOTE_FOUND=0"
for /f "delims=" %%R in ('%GIT% remote') do (
    echo [BLOCKED: REMOTE_CONFIGURED]
    echo remote: %%R
    set "REMOTE_FOUND=1"
)
if "!REMOTE_FOUND!"=="1" exit /b 7

%GIT% cat-file -e "%TARGET_HASH%^{commit}" >nul 2>&1
if errorlevel 1 (
    echo [BLOCKED: INVALID_TARGET_COMMIT]
    echo %TARGET_HASH%
    exit /b 8
)

echo TARGET:
%GIT% show -s --format="%%H %%s" "%TARGET_HASH%"
echo.
echo CURRENT STATUS:
%GIT% status --short

set "DIRTY=0"
for /f "delims=" %%L in ('%GIT% status --porcelain') do set "DIRTY=1"
if "!DIRTY!"=="1" (
    echo.
    echo [BLOCKED: FORENSIC_CHECKPOINT_REQUIRED]
    echo Working tree/index is not clean.
    echo First preserve the state with an authorized WIP forensic checkpoint,
    echo then obtain fresh external rollback authorization.
    exit /b 9
)

for /f %%H in ('%GIT% rev-parse HEAD') do set "ORIGINAL_HEAD=%%H"
for /f %%H in ('%GIT% rev-parse --short "%TARGET_HASH%"') do set "SHORT_TARGET=%%H"

for /f "delims=" %%N in ('%GIT% config --get user.name') do set "GIT_USER_NAME=%%N"
for /f "delims=" %%E in ('%GIT% config --get user.email') do set "GIT_USER_EMAIL=%%E"
if not defined GIT_USER_NAME (
    echo [BLOCKED: GIT_USER_NAME_NOT_CONFIGURED]
    exit /b 10
)
if not defined GIT_USER_EMAIL (
    echo [BLOCKED: GIT_USER_EMAIL_NOT_CONFIGURED]
    exit /b 11
)

echo.
echo AUTHORIZATION: supplied externally
echo METHOD: history-preserving restore to target tree
echo rollback_performed: PENDING

%GIT% restore --source="%TARGET_HASH%" --staged --worktree -- .
if errorlevel 1 (
    echo [BLOCKED: RESTORE_FAILED]
    exit /b 12
)

%GIT% diff --cached --quiet
if not errorlevel 1 (
    echo Target tree already matches current HEAD.
    echo rollback_performed: NO-OP
    exit /b 0
)

echo.
echo RECOVERY CHANGES:
%GIT% diff --cached --name-status

%GIT% commit -m "RECOVERY - restore state %SHORT_TARGET%"
if errorlevel 1 (
    echo [BLOCKED: RECOVERY_COMMIT_FAILED]
    echo Restoring original HEAD tree...
    %GIT% restore --source="%ORIGINAL_HEAD%" --staged --worktree -- .
    exit /b 13
)

%GIT% diff --quiet "%TARGET_HASH%" HEAD --
if errorlevel 1 (
    echo [BLOCKED: POST_ROLLBACK_TREE_MISMATCH]
    exit /b 14
)

for /f %%H in ('%GIT% rev-parse HEAD') do set "RECOVERY_HEAD=%%H"

echo.
echo ROLLBACK COMPLETED
echo target: %TARGET_HASH%
echo recovery_commit: !RECOVERY_HEAD!
echo history_preserved: YES
echo authorization_token_recorded: NO
exit /b 0
