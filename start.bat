@echo off
REM Quick start script for the 6-7 Meme Detector (Windows)

echo ==================================
echo 6-7 Meme Detector - Quick Start
echo ==================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo X Python is not installed!
    echo Please install Python 3.7 or higher from https://www.python.org/
    pause
    exit /b 1
)

echo [OK] Python found
python --version
echo.

REM Check if requirements are installed
echo Checking dependencies...
python -c "import cv2" >nul 2>&1
if errorlevel 1 (
    echo [*] Installing dependencies...
    pip install -r requirements.txt
    if errorlevel 1 (
        echo X Failed to install dependencies
        echo Please run: pip install -r requirements.txt
        pause
        exit /b 1
    )
) else (
    echo [OK] Dependencies already installed
)

echo.
echo [*] Starting 6-7 Meme Detector...
echo.
echo Instructions:
echo   - Show 6 or 7 fingers to trigger the meme flood
echo   - Press 'q' to quit
echo.
echo Starting in 3 seconds...
timeout /t 3 /nobreak >nul

python detector.py
pause
