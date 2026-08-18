@echo off
setlocal EnableExtensions EnableDelayedExpansion

rem ============================================================
rem DOJO GIT SAFETY v1
rem Local recovery only. No remote. Fail-closed safety gates.
rem ============================================================

set "PROD_ROOT=D:\Gemini\dojo"
set "ROOT=%PROD_ROOT%"
set "GIT=git"

rem Test override is accepted ONLY when explicitly enabled.
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
        echo Expected: %PROD_ROOT%
        echo Actual:   %ROOT%
        exit /b 91
    )
)

if not exist "%ROOT%\" (
    echo [BLOCKED: ROOT_NOT_FOUND]
    echo %ROOT%
    exit /b 92
)

where git >nul 2>&1
if errorlevel 1 (
    echo [BLOCKED: GIT_NOT_FOUND]
    exit /b 93
)

cd /d "%ROOT%" || (
    echo [BLOCKED: ROOT_NOT_ACCESSIBLE]
    exit /b 94
)

if "%~1"=="" goto MENU
if /I "%~1"=="BASELINE" goto CMD_BASELINE
if /I "%~1"=="WIP" goto CMD_WIP
if /I "%~1"=="STEP" goto CMD_STEP
if /I "%~1"=="STATUS" goto STATUS
if /I "%~1"=="ROLLBACK_REPORT" goto ROLLBACK_REPORT
if /I "%~1"=="FINAL" goto CMD_FINAL

echo [BLOCKED: UNKNOWN_COMMAND]
exit /b 2

:MENU
echo.
echo ========================================
echo        CODING SAMURAI - DOJO GIT
echo ========================================
echo.
echo 1. CREATE BASELINE
echo 2. CREATE WIP CHECKPOINT
echo 3. CREATE ACCEPTED STEP CHECKPOINT
echo 4. STATUS / HISTORY
echo 5. PREPARE ROLLBACK REPORT
echo 6. CREATE FINAL RELEASE CHECKPOINT
echo 0. EXIT
echo.
set /p "CHOICE=Select: "

if "%CHOICE%"=="1" (
    set /p "PROJECT_ID=Externally supplied project identifier: "
    if not defined PROJECT_ID (
        echo [BLOCKED: PROJECT_IDENTIFIER_REQUIRED]
        exit /b 10
    )
    call "%~f0" BASELINE "!PROJECT_ID!"
    exit /b !errorlevel!
)
if "%CHOICE%"=="2" (
    set /p "WIP_REASON=Externally authorized WIP reason: "
    if not defined WIP_REASON (
        echo [BLOCKED: WIP_REASON_REQUIRED]
        exit /b 11
    )
    call "%~f0" WIP "!WIP_REASON!"
    exit /b !errorlevel!
)
if "%CHOICE%"=="3" (
    echo [BLOCKED: ACCEPTANCE_TOKEN_REQUIRED]
    echo Use:
    echo   dojo_git.bat STEP STEP-ID ACCEPTANCE-TOKEN "accepted description"
    exit /b 12
)
if "%CHOICE%"=="4" (
    call "%~f0" STATUS
    exit /b !errorlevel!
)
if "%CHOICE%"=="5" (
    call "%~f0" ROLLBACK_REPORT
    exit /b !errorlevel!
)
if "%CHOICE%"=="6" (
    echo [BLOCKED: ACCEPTANCE_TOKEN_REQUIRED]
    echo Use:
    echo   dojo_git.bat FINAL PROJECT-ID ACCEPTANCE-TOKEN
    exit /b 13
)
if "%CHOICE%"=="0" exit /b 0

echo [BLOCKED: INVALID_MENU_SELECTION]
exit /b 14

:CMD_BASELINE
set "PROJECT_ID=%~2"
if not defined PROJECT_ID (
    echo [BLOCKED: PROJECT_IDENTIFIER_REQUIRED]
    exit /b 20
)

if exist "%ROOT%\.git\" (
    echo [BLOCKED: BASELINE_REPOSITORY_ALREADY_EXISTS]
    echo BASELINE v1 requires .git to be absent.
    exit /b 21
)

if not exist "%ROOT%\.gitignore" (
    echo [BLOCKED: GITIGNORE_REQUIRED]
    exit /b 22
)

call :CHECK_IDENTITY
if errorlevel 1 exit /b %errorlevel%

echo ROOT: %ROOT%
echo.
echo .gitignore:
echo ----------------------------------------
type "%ROOT%\.gitignore"
echo ----------------------------------------
echo.
echo TOP-LEVEL INVENTORY:
dir /b /a "%ROOT%"
echo.
echo git status --short:
echo [repository not initialized yet]

%GIT% init -q
if errorlevel 1 (
    echo [BLOCKED: GIT_INIT_FAILED]
    exit /b 23
)
%GIT% branch -M main
if errorlevel 1 (
    call :ABORT_NEW_REPO
    echo [BLOCKED: MAIN_BRANCH_INIT_FAILED]
    exit /b 24
)

call :CHECK_NO_REMOTE
if errorlevel 1 (
    call :ABORT_NEW_REPO
    exit /b 25
)

call :CHECKPOINT_PREFLIGHT
if errorlevel 1 (
    set "RC=!errorlevel!"
    call :ABORT_NEW_REPO
    exit /b !RC!
)

%GIT% commit -m "BASELINE - %PROJECT_ID%"
if errorlevel 1 (
    call :ABORT_NEW_REPO
    echo [BLOCKED: BASELINE_COMMIT_FAILED]
    exit /b 26
)

for /f %%H in ('%GIT% rev-parse HEAD') do set "HEAD_HASH=%%H"
%GIT% status --porcelain > "%TEMP%\dojo_git_status_%RANDOM%.tmp"
for %%Z in ("%TEMP%\dojo_git_status_%RANDOM%.tmp") do rem no-op

echo.
echo BASELINE CREATED
echo commit: !HEAD_HASH!
call :PRINT_WORKTREE_STATE
exit /b 0

:CMD_WIP
set "WIP_REASON=%~2"
if not defined WIP_REASON (
    echo [BLOCKED: WIP_REASON_REQUIRED]
    exit /b 30
)
call :REPO_REQUIRED
if errorlevel 1 exit /b %errorlevel%
call :CHECK_NO_REMOTE
if errorlevel 1 exit /b %errorlevel%
call :CHECK_IDENTITY
if errorlevel 1 exit /b %errorlevel%
call :CHECKPOINT_PREFLIGHT
if errorlevel 1 exit /b %errorlevel%

%GIT% diff --cached --quiet
if not errorlevel 1 (
    echo [BLOCKED: NO_CHANGES_TO_COMMIT]
    exit /b 31
)

%GIT% commit -m "WIP - %WIP_REASON%"
if errorlevel 1 (
    echo [BLOCKED: WIP_COMMIT_FAILED]
    exit /b 32
)
for /f %%H in ('%GIT% rev-parse HEAD') do set "HEAD_HASH=%%H"
echo WIP CREATED
echo commit: !HEAD_HASH!
call :PRINT_WORKTREE_STATE
exit /b 0

:CMD_STEP
set "STEP_ID=%~2"
set "ACCEPT_TOKEN=%~3"
set "STEP_DESC=%~4"

if not defined STEP_ID (
    echo [BLOCKED: STEP_ID_REQUIRED]
    exit /b 40
)
if not defined ACCEPT_TOKEN (
    echo [BLOCKED: ACCEPTANCE_TOKEN_REQUIRED]
    echo Use WIP instead.
    exit /b 41
)
if not defined STEP_DESC (
    echo [BLOCKED: STEP_DESCRIPTION_REQUIRED]
    exit /b 42
)

call :REPO_REQUIRED
if errorlevel 1 exit /b %errorlevel%
call :CHECK_NO_REMOTE
if errorlevel 1 exit /b %errorlevel%
call :CHECK_IDENTITY
if errorlevel 1 exit /b %errorlevel%
call :CHECKPOINT_PREFLIGHT
if errorlevel 1 exit /b %errorlevel%

%GIT% diff --cached --quiet
if not errorlevel 1 (
    echo [BLOCKED: NO_CHANGES_TO_COMMIT]
    exit /b 43
)

%GIT% commit -m "STEP - %STEP_ID% - %STEP_DESC%"
if errorlevel 1 (
    echo [BLOCKED: STEP_COMMIT_FAILED]
    exit /b 44
)
for /f %%H in ('%GIT% rev-parse HEAD') do set "HEAD_HASH=%%H"
echo ACCEPTED STEP CREATED
echo commit: !HEAD_HASH!
call :PRINT_WORKTREE_STATE
exit /b 0

:STATUS
call :REPO_REQUIRED
if errorlevel 1 exit /b %errorlevel%
echo.
echo git status --short
%GIT% status --short
echo.
echo git log --oneline --decorate -10
%GIT% log --oneline --decorate -10
echo.
echo git diff --stat
%GIT% diff --stat
echo.
echo git diff --cached --stat
%GIT% diff --cached --stat
exit /b 0

:ROLLBACK_REPORT
call :REPO_REQUIRED
if errorlevel 1 exit /b %errorlevel%
for /f %%H in ('%GIT% rev-parse HEAD') do set "HEAD_HASH=%%H"

%GIT% status --porcelain > "%TEMP%\dojo_status_%RANDOM%.txt"
set "WORKTREE_CLEAN=YES"
for /f "usebackq delims=" %%L in ("%TEMP%\dojo_status_%RANDOM%.txt") do set "WORKTREE_CLEAN=NO"
del "%TEMP%\dojo_status_%RANDOM%.txt" >nul 2>&1

%GIT% diff --quiet
if errorlevel 1 (set "UNSTAGED=YES") else (set "UNSTAGED=NO")

%GIT% diff --cached --quiet
if errorlevel 1 (set "STAGED=YES") else (set "STAGED=NO")

if "!WORKTREE_CLEAN!"=="YES" (
    set "FORENSIC_REQUIRED=NO"
) else (
    set "FORENSIC_REQUIRED=YES"
)

echo.
echo Rollback Preparation:
echo   current_head: !HEAD_HASH!
echo   working_tree_clean: !WORKTREE_CLEAN!
echo   unstaged_changes: !UNSTAGED!
echo   staged_changes: !STAGED!
echo   proposed_recovery_point: EXTERNAL_DECISION_REQUIRED
echo   forensic_checkpoint_required: !FORENSIC_REQUIRED!
echo   rollback_performed: NO
echo.
echo recent_checkpoints:
%GIT% log --oneline --decorate -10
exit /b 0

:CMD_FINAL
set "PROJECT_ID=%~2"
set "ACCEPT_TOKEN=%~3"
if not defined PROJECT_ID (
    echo [BLOCKED: PROJECT_IDENTIFIER_REQUIRED]
    exit /b 60
)
if not defined ACCEPT_TOKEN (
    echo [BLOCKED: ACCEPTANCE_TOKEN_REQUIRED]
    exit /b 61
)

call :REPO_REQUIRED
if errorlevel 1 exit /b %errorlevel%
call :CHECK_NO_REMOTE
if errorlevel 1 exit /b %errorlevel%
call :CHECK_IDENTITY
if errorlevel 1 exit /b %errorlevel%
call :CHECKPOINT_PREFLIGHT
if errorlevel 1 exit /b %errorlevel%

rem FINAL is a release marker and may be an empty commit.
%GIT% commit --allow-empty -m "FINAL - %PROJECT_ID%"
if errorlevel 1 (
    echo [BLOCKED: FINAL_COMMIT_FAILED]
    exit /b 62
)

for /f %%H in ('%GIT% rev-parse HEAD') do set "HEAD_HASH=%%H"
for /f %%H in ('%GIT% rev-parse --short HEAD') do set "SHORT_HASH=%%H"

for %%I in ("%ROOT%\..\dojo_bundles") do set "BUNDLE_ROOT=%%~fI"
if not exist "!BUNDLE_ROOT!\" mkdir "!BUNDLE_ROOT!"
if errorlevel 1 (
    echo [BLOCKED: BUNDLE_DIRECTORY_FAILED]
    exit /b 63
)

set "SAFE_PROJECT=%PROJECT_ID: =_%"
set "BUNDLE_PATH=!BUNDLE_ROOT!\FINAL_!SAFE_PROJECT!_!SHORT_HASH!.bundle"

echo.
echo FINAL CHECKPOINT CREATED
echo commit: !HEAD_HASH!
echo.
%GIT% status
echo.
%GIT% log --oneline -10
echo.
echo Creating bundle:
echo !BUNDLE_PATH!
%GIT% bundle create "!BUNDLE_PATH!" --all
if errorlevel 1 (
    echo [BLOCKED: BUNDLE_CREATE_FAILED]
    exit /b 64
)
%GIT% bundle verify "!BUNDLE_PATH!"
if errorlevel 1 (
    echo [BLOCKED: BUNDLE_VERIFY_FAILED]
    exit /b 65
)

echo.
echo FINAL RELEASE PREPARED
echo bundle: !BUNDLE_PATH!
echo cleanup_authorized: NO
exit /b 0

:CHECKPOINT_PREFLIGHT
echo.
echo git status --short
%GIT% status --short

call :CHECK_UNEXPECTED_UNTRACKED
if errorlevel 1 exit /b %errorlevel%

%GIT% add -A
if errorlevel 1 (
    echo [BLOCKED: STAGING_FAILED]
    exit /b 70
)

echo.
echo git diff --cached --name-status
%GIT% diff --cached --name-status

call :CHECK_STAGED_FORBIDDEN
if errorlevel 1 (
    call :UNSTAGE_ALL
    exit /b 71
)
exit /b 0

:CHECK_UNEXPECTED_UNTRACKED
set "UNEXPECTED_FOUND=0"
for /f "delims=" %%F in ('%GIT% ls-files --others --exclude-standard') do (
    set "P=%%F"
    set "P=!P:\=/!"
    call :IS_DEFAULT_ALLOWED_UNTRACKED "!P!"
    if errorlevel 1 (
        echo [REVIEW REQUIRED]
        echo Unexpected file in checkpoint candidate:
        echo !P!
        echo.
        echo Checkpoint aborted.
        echo Review .gitignore or active task.
        set "UNEXPECTED_FOUND=1"
    )
)
if "!UNEXPECTED_FOUND!"=="1" exit /b 72
exit /b 0

:IS_DEFAULT_ALLOWED_UNTRACKED
set "P=%~1"
if /I "%P%"==".gitignore" exit /b 0
if /I "%P%"=="dojo_git.bat" exit /b 0

echo(%P%| findstr /I /R "^[^/]*\.md$" >nul
if not errorlevel 1 exit /b 0

if /I "%P:~0,6%"=="Input/" exit /b 0
if /I "%P:~0,4%"=="src/" exit /b 0
if /I "%P:~0,7%"=="config/" exit /b 0
if /I "%P:~0,9%"=="Evidence/" exit /b 0
if /I "%P:~0,10%"=="git_tools/" exit /b 0
exit /b 1

:CHECK_STAGED_FORBIDDEN
set "FORBIDDEN_FOUND=0"
for /f "delims=" %%F in ('%GIT% diff --cached --name-only') do (
    set "P=%%F"
    set "P=!P:\=/!"
    call :IS_FORBIDDEN "!P!"
    if not errorlevel 1 (
        echo [BLOCKED: FORBIDDEN_FILE_IN_CHECKPOINT]
        echo !P!
        set "FORBIDDEN_FOUND=1"
    )
)
if "!FORBIDDEN_FOUND!"=="1" exit /b 73
exit /b 0

:IS_FORBIDDEN
set "P=%~1"
set "NAME=%~nx1"
set "EXT=%~x1"

if /I "%EXT%"==".gguf" exit /b 0
if /I "%EXT%"==".bin" exit /b 0
if /I "%EXT%"==".safetensors" exit /b 0
if /I "%EXT%"==".key" exit /b 0
if /I "%EXT%"==".pem" exit /b 0
if /I "%NAME%"==".env" exit /b 0
if /I "%NAME:~0,5%"==".env." exit /b 0
if /I "%P%"=="models" exit /b 0
if /I "%P:~0,7%"=="models/" exit /b 0
exit /b 1

:UNSTAGE_ALL
%GIT% rev-parse --verify HEAD >nul 2>&1
if errorlevel 1 (
    %GIT% rm -r --cached -q --ignore-unmatch .
) else (
    %GIT% reset -q
)
exit /b 0

:CHECK_NO_REMOTE
set "REMOTE_FOUND=0"
for /f "delims=" %%R in ('%GIT% remote') do (
    echo [BLOCKED: REMOTE_CONFIGURED]
    echo remote: %%R
    set "REMOTE_FOUND=1"
)
if "%REMOTE_FOUND%"=="1" exit /b 74
exit /b 0

:REPO_REQUIRED
if not exist "%ROOT%\.git\" (
    echo [BLOCKED: DOJO_REPOSITORY_NOT_INITIALIZED]
    exit /b 75
)
%GIT% rev-parse --is-inside-work-tree >nul 2>&1
if errorlevel 1 (
    echo [BLOCKED: INVALID_GIT_REPOSITORY]
    exit /b 76
)
exit /b 0

:CHECK_IDENTITY
for /f "delims=" %%N in ('%GIT% config --get user.name') do set "GIT_USER_NAME=%%N"
for /f "delims=" %%E in ('%GIT% config --get user.email') do set "GIT_USER_EMAIL=%%E"
if not defined GIT_USER_NAME (
    echo [BLOCKED: GIT_USER_NAME_NOT_CONFIGURED]
    exit /b 77
)
if not defined GIT_USER_EMAIL (
    echo [BLOCKED: GIT_USER_EMAIL_NOT_CONFIGURED]
    exit /b 78
)
exit /b 0

:PRINT_WORKTREE_STATE
%GIT% status --porcelain > "%TEMP%\dojo_clean_%RANDOM%.txt"
set "CLEAN=YES"
for /f "usebackq delims=" %%L in ("%TEMP%\dojo_clean_%RANDOM%.txt") do set "CLEAN=NO"
del "%TEMP%\dojo_clean_%RANDOM%.txt" >nul 2>&1
if "!CLEAN!"=="YES" (
    echo working tree: clean
) else (
    echo working tree: NOT CLEAN
    %GIT% status --short
)
exit /b 0

:ABORT_NEW_REPO
if exist "%ROOT%\.git\" rmdir /s /q "%ROOT%\.git"
exit /b 0
