@echo off
cd /d E:\Gemini\Dojo\AI-Collab
netstat -ano | findstr ":5999 :8000"
taskkill /PID <pid> /F
echo Fixture: http://127.0.0.1:5999/conv_a
echo Stop: Ctrl+C
python fixture_server.py