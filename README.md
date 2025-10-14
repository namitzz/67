# 67 Meme Detector 🔥

A real-time gesture detector that uses your camera to detect the "6 7" gesture (finger counting) and floods the screen with "6 7" memes when detected!

![Python](https://img.shields.io/badge/Python-3.7%2B-blue)
![OpenCV](https://img.shields.io/badge/OpenCV-4.8%2B-green)
![MediaPipe](https://img.shields.io/badge/MediaPipe-0.10%2B-orange)

## 🎯 Features

- 🎥 **Real-time camera-based hand gesture detection**
- 👆 **Counts fingers on both hands simultaneously** using advanced ML
- 🔥 **Triggers meme flood** when 6 or 7 fingers are detected
- 💫 **Animated meme overlay** with random positions, sizes, and colors
- 🎨 **Pulsating effects** for maximum meme impact
- ⚡ **Smooth detection** with temporal filtering to avoid false triggers

## 🚀 Quick Start

### Linux/macOS
```bash
git clone https://github.com/namitzz/67.git
cd 67
pip install -r requirements.txt
python3 detector.py
```

Or use the quick start script:
```bash
./start.sh
```

### Windows
```bash
git clone https://github.com/namitzz/67.git
cd 67
pip install -r requirements.txt
python detector.py
```

Or double-click `start.bat`

## 📋 Requirements

- Python 3.7 or higher
- Webcam/camera
- Dependencies (auto-installed from requirements.txt):
  - OpenCV (opencv-python)
  - MediaPipe
  - NumPy
  - Pillow

## 📖 Documentation

- **[DEMO.md](DEMO.md)** - Visual walkthrough and usage tips
- **[FAQ.md](FAQ.md)** - Frequently asked questions and troubleshooting
- **[test_detector.py](test_detector.py)** - Test installation and setup

## 🎮 How to Use

1. Run the detector: `python3 detector.py`
2. Position yourself in front of the camera
3. Show 6 or 7 fingers to trigger the meme flood
4. Watch the screen flood with "6 7" memes! 🎉
5. Press 'q' to quit

### Gesture Examples

**Easy ways to trigger:**
- 👋 + 👋 Two hands: 3 + 3 fingers = 6 detected
- 👋 + ✋ Two hands: 3 + 4 fingers = 7 detected  
- ✋ + ✋ Two hands: 5 + 2 fingers = 7 detected

### Tips for Best Results

- ✅ Good lighting
- ✅ Plain background
- ✅ Hold hands 1-2 feet from camera
- ✅ Keep gesture steady for ~1 second
- ✅ Face palms toward camera

## 🔧 How It Works

The detector uses:
- **OpenCV** for camera capture and image processing
- **MediaPipe Hands** for accurate hand landmark detection (21 points per hand)
- **Finger counting algorithm** that analyzes finger tip vs joint positions
- **Temporal smoothing** (10-frame history buffer) for reliable detection
- **Dynamic meme generation** with randomized text properties

When 6 or 7 fingers are detected consistently across multiple frames, "meme mode" activates and floods your screen with animated "6 7" text for 5 seconds! 🎉

## 🎨 Customization

Edit `detector.py` to customize:

```python
# Meme duration (line ~25)
self.meme_duration = 5  # seconds

# Detection sensitivity (line ~18)
min_detection_confidence=0.7  # 0.0 to 1.0

# Number of memes (line ~125)
num_memes = min(int(elapsed * 10) + 5, 50)

# Meme texts (line ~137)
texts = ["6 7", "67", "🔥 6 7 🔥", "SIX SEVEN", "6️⃣7️⃣"]

# Detection threshold (line ~213)
sum(self.detection_history) >= 5  # frames needed to trigger
```

## 🛠️ Troubleshooting

**Camera not opening?**
- Ensure no other app is using the camera
- Check camera permissions in OS settings

**Hands not detected?**
- Improve lighting
- Move closer to camera
- Use plain background

**Can't install dependencies?**
```bash
pip install --default-timeout=300 -r requirements.txt
```

For more help, see **[FAQ.md](FAQ.md)**

## 🧪 Testing

Run the test suite to verify installation:
```bash
python3 test_detector.py
```

This will:
- ✓ Check all dependencies are installed
- ✓ Verify detector class can be instantiated  
- ✓ Test core methods without requiring a camera

## 📦 Project Structure

```
67/
├── detector.py         # Main application
├── requirements.txt    # Python dependencies
├── test_detector.py    # Test suite
├── start.sh           # Quick start (Linux/macOS)
├── start.bat          # Quick start (Windows)
├── README.md          # This file
├── DEMO.md            # Visual walkthrough
├── FAQ.md             # FAQs and troubleshooting
└── .gitignore         # Git ignore rules
```

## 🤝 Contributing

Contributions welcome! Ideas:
- Add more meme variations
- Improve detection accuracy
- Create gesture combinations
- Add sound effects
- Build a GUI
- Mobile support

## 📝 License

Open source - feel free to use and modify!

## 🎉 Credits

Built with:
- [OpenCV](https://opencv.org/) - Computer vision library
- [MediaPipe](https://mediapipe.dev/) - Google's ML framework
- Love for memes! 🔥

---

**Made with ❤️ for the 6 7 meme community**