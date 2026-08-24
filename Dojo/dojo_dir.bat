@echo off
chcp 65001 > nul

if not exist "logs" mkdir "logs"
if not exist "Output" mkdir "Output"
if not exist "state" mkdir "state"
if not exist "src" mkdir "src"
if not exist "config" mkdir "config"
if not exist "Input" mkdir "Input"

echo Все 6 папок готовы!
pause