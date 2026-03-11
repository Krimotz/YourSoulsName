@echo off
cd /d "%~dp0"

REM Start the Python server in a new command prompt window
start cmd /k "python server.py"

REM Open the name generator in the browser
start "" http://localhost:5000/name_generator.html
