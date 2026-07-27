@echo off

python.exe -m pip install --upgrade pip

if not exist "venv" (
    python -m venv venv

    "%~dp0\venv\Scripts\python.exe" -m pip install python-dotenv typing_extensions playwright customtkinter pillow aiosqlite aiohttp aiofiles
)

"%~dp0\venv\Scripts\python.exe" -m pip install --upgrade pip

"%~dp0\venv\Scripts\python.exe" -m playwright install

"%~dp0\venv\Scripts\python.exe" -m pip list