@echo off
setlocal

cd /d "%~dp0"

echo ============================================================ 
echo  AI-Collab dual run: fixture 5999 + serve_interface 8000
echo ============================================================ 
echo.

REM --- check ports are free ---
echo [CHECK] port 5999...
netstat -ano | findstr ":5999" | findstr "LISTENING" >nul
if %ERRORLEVEL%==0 (
    echo ERROR: port 5999 is already in use. Kill existing process first.
    echo Run:  netstat -ano ^| findstr :5999
    exit /b 1
)
echo [CHECK] port 5999 free

echo [CHECK] port 8000...
netstat -ano | findstr ":8000" | findstr "LISTENING" >nul
if %ERRORLEVEL%==0 (
    echo ERROR: port 8000 is already in use. Kill existing process first.
    echo Run:  netstat -ano ^| findstr :8000
    exit /b 1
)
echo [CHECK] port 8000 free

echo.
echo [START] fixture_server.py on 5999...
start "AI-Collab FIXTURE" cmd /k python fixture_server.py

timeout /t 2 /nobreak >nul

echo [START] serve_interface.py on 8000...
start "AI-Collab UI" cmd /k python serve_interface.py

timeout /t 2 /nobreak >nul

echo.
echo ============================================================ 
echo  UI:  http://127.0.0.1:8000/
echo  API: http://127.0.0.1:5999/health
echo ============================================================ 
echo.
echo Both servers started in separate windows.
echo Close those windows to stop the servers.
echo.
