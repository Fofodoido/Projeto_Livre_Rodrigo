@echo off
cd /d "%~dp0"

REM Create venv if it doesn't exist
if not exist "venv\Scripts\activate.bat" (
    echo Creating virtual environment...
    python -m venv venv
)

call venv\Scripts\activate.bat
pip install --upgrade pip >nul
pip install -r requirements.txt

python jogo_main.py
pause
