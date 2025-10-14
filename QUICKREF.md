# Quick Reference Card

## 🚀 Getting Started (30 seconds)
```bash
git clone https://github.com/namitzz/67.git
cd 67
pip install -r requirements.txt
python3 detector.py
```

## 🎯 Usage
| Action | Method |
|--------|--------|
| Start detector | `python3 detector.py` or `./start.sh` |
| Trigger memes | Show 6 or 7 fingers to camera |
| Quit | Press 'q' |
| Test setup | `python3 test_detector.py` |

## 🎮 Gesture Examples
| Gesture | Result |
|---------|--------|
| 👋 + 👋 (3+3) | ✅ Triggers |
| 👋 + ✋ (3+4) | ✅ Triggers |
| ✋ + ✋ (5+2) | ✅ Triggers |
| ✌️ + ✌️ (2+2) | ❌ No trigger |

## ⚙️ Quick Customization
Edit `config.py`:
```python
MIN_DETECTION_CONFIDENCE = 0.7  # Sensitivity (0.3 = easy, 0.9 = hard)
DETECTION_THRESHOLD = 5         # Frames to trigger (3 = fast, 7 = slow)
MEME_DURATION = 5.0            # Seconds (3.0 = short, 10.0 = long)
MAX_MEMES = 50                 # Number of memes (20 = few, 100 = many)
```

## 🔧 Common Issues & Fixes
| Problem | Solution |
|---------|----------|
| Camera won't open | Close other apps using camera |
| Hands not detected | Better lighting, move closer |
| Too sensitive | Increase `DETECTION_THRESHOLD` |
| Not sensitive enough | Lower `MIN_DETECTION_CONFIDENCE` |
| Wrong camera | Change `CAMERA_INDEX` in config |
| Install errors | `pip install --upgrade pip` |

## 📁 File Overview
| File | Purpose |
|------|---------|
| `detector.py` | Main application |
| `config.py` | Easy settings (edit this!) |
| `banner.py` | ASCII art |
| `test_detector.py` | Installation test |
| `requirements.txt` | Dependencies |
| `start.sh` / `start.bat` | Quick launchers |
| `README.md` | Full documentation |
| `FAQ.md` | Troubleshooting |
| `DEMO.md` | Visual guide |

## 🎨 Add Your Own Memes
In `config.py`, edit:
```python
MEME_TEXTS = [
    "6 7",
    "YOUR TEXT HERE",
    "🎉 CUSTOM MEME 🎉",
]
```

## 📊 System Requirements
| Item | Requirement |
|------|-------------|
| Python | 3.7+ |
| RAM | 2GB+ |
| Camera | Any webcam |
| OS | Windows/macOS/Linux |
| Disk Space | ~100MB |

## 🔗 Key Shortcuts
| Key | Action |
|-----|--------|
| `q` | Quit |
| `ESC` | Quit (alternative) |

## 💡 Pro Tips
1. ✅ Use good lighting
2. ✅ Plain background works best
3. ✅ Keep hands 1-2 feet from camera
4. ✅ Hold gesture for 1 second
5. ✅ Face palms toward camera
6. ✅ Separate fingers clearly

## 📱 Documentation Links
- Full Guide: `README.md`
- Visual Demo: `DEMO.md`
- Troubleshooting: `FAQ.md`
- GitHub: https://github.com/namitzz/67

## 🎯 Detection Logic
```
1. Camera captures frame
2. MediaPipe detects hands (up to 2)
3. Count extended fingers per hand
4. If 6 or 7 detected → add to history
5. If 5+ of last 10 frames detected → MEME MODE!
6. Display memes for 5 seconds
7. Return to detection mode
```

## 🏆 Advanced Usage
```bash
# Custom camera
CAMERA_INDEX=1 python3 detector.py

# Test without camera
python3 test_detector.py

# Debug mode (see MediaPipe output)
# Edit detector.py: add print statements in detect_six_seven()
```

---

**For full documentation, see README.md**
