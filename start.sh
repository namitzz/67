#!/bin/bash
# Quick start script for the 6-7 Meme Detector

echo "=================================="
echo "6-7 Meme Detector - Quick Start"
echo "=================================="
echo ""

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed!"
    echo "Please install Python 3.7 or higher from https://www.python.org/"
    exit 1
fi

echo "✓ Python 3 found: $(python3 --version)"
echo ""

# Check if requirements are installed
echo "Checking dependencies..."
python3 -c "import cv2" 2>/dev/null
if [ $? -ne 0 ]; then
    echo "📦 Installing dependencies..."
    pip install -r requirements.txt
    if [ $? -ne 0 ]; then
        echo "❌ Failed to install dependencies"
        echo "Please run: pip install -r requirements.txt"
        exit 1
    fi
else
    echo "✓ Dependencies already installed"
fi

echo ""
echo "🎥 Starting 6-7 Meme Detector..."
echo ""
echo "Instructions:"
echo "  • Show 6 or 7 fingers to trigger the meme flood"
echo "  • Press 'q' to quit"
echo ""
echo "Starting in 3 seconds..."
sleep 3

python3 detector.py
