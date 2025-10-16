# 67 Meme Camera Effect 🔥

A viral TikTok/Instagram-style meme camera that triggers an intense visual explosion when you show 6 or 7 fingers! Built with MediaPipe Hands for real-time gesture detection.

![JavaScript](https://img.shields.io/badge/JavaScript-ES6%2B-yellow)
![MediaPipe](https://img.shields.io/badge/MediaPipe-0.10%2B-orange)
![HTML5](https://img.shields.io/badge/HTML5-Camera-red)

## ✨ Features

- 🎥 **Real-time webcam hand detection** using MediaPipe Hands
- 👆 **Smart finger counting** across both hands (detects 6 or 7 total fingers)
- 💥 **Intense meme effects**:
  - Screen shakes and zooms
  - Flash effects
  - Random "67" text spam across screen
  - Bold white/yellow font with random sizes
- 🔊 **Bass drop sound** using Web Audio API (no external files needed!)
- ⚙️ **Customizable controls**:
  - Sound toggle
  - Intensity slider (10-120 meme texts)
  - Cooldown slider (0.8-4 seconds)
  - Party mode for extra effects
- 🎮 **Smooth user experience**:
  - Graceful camera permission handling
  - Cooldown system prevents spam
  - Fullscreen mode support
  - Works on desktop and mobile browsers

## 🚀 Quick Start

### 🌐 Try it Online

**[Launch Web App](https://namitzz.github.io/67/)** - No installation needed!

Just open the link, allow camera access, and start making memes! 🎉

### 💻 Run Locally

```bash
git clone https://github.com/namitzz/67.git
cd 67
# Simply open index.html in your browser
# Or use a local server:
python -m http.server 8000
# Then visit http://localhost:8000
```

## 📖 How to Use

1. Click **"Start camera"** button
2. Allow camera access when prompted
3. Show **6 or 7 fingers** to the camera (try 3+3, 3+4, 5+2)
4. Hold the gesture steady for ~1 second
5. Watch the **MEME EXPLOSION** happen! 💥🔥
6. Adjust intensity, cooldown, and toggle party mode for different effects

### Pro Tips

- ✅ Good lighting helps detection
- ✅ Face palms toward camera
- ✅ Keep hands 1-2 feet from camera
- ✅ Hold gesture steady for reliable triggers
- ✅ Use party mode for maximum chaos! 🎉

## 🎨 Customization

All controls are built into the UI:

- **Sound Toggle**: Enable/disable bass drop sound
- **Intensity Slider**: Control number of meme texts (10-120)
- **Cooldown Slider**: Time between triggers (0.8-4 seconds)
- **Party Mode**: Double the meme texts for extra effect!
- **Fullscreen Button**: Go fullscreen for maximum immersion

## 🛠️ Technical Details

### Built With

- **MediaPipe Hands** (Vision Tasks v0.10.10) - Hand landmark detection
- **Web Audio API** - Synthesized bass drop sound
- **Canvas API** - Video feed rendering
- **ResizeObserver** - Responsive canvas sizing
- **Vanilla JavaScript** - No frameworks needed!

### How It Works

1. **Hand Detection**: MediaPipe detects up to 2 hands with 21 landmarks each
2. **Finger Counting**: Algorithm checks if finger tips are above joints (y-axis) and thumb laterally positioned
3. **Trigger Smoothing**: Requires 5/10 frames to match to avoid false triggers
4. **Cooldown System**: Prevents rapid re-triggering using configurable cooldown
5. **Effect System**:
   - CSS animations for shake/zoom/flash
   - JavaScript for spawning random text elements
   - Web Audio for synthesized bass sound
   - Automatic cleanup after ~2 seconds

### Browser Compatibility

✅ Chrome/Edge (recommended)
✅ Firefox
✅ Safari (iOS/macOS)
⚠️ Requires HTTPS or localhost for camera access

## 📦 Project Structure

```
67/
├── index.html          # Main HTML structure
├── style.css          # All styling and animations
├── script.js          # Hand detection and effects logic
├── assets/            # Directory for assets
├── README.md          # This file
└── Python files...    # Legacy Python desktop version
```

## 🎯 Advanced Features

### Detection Algorithm

The finger counting uses a sophisticated heuristic:
- **4 fingers** (index-pinky): Checks if tip Y < pip Y
- **Thumb**: Checks lateral distance from wrist (>0.04 normalized)
- **Both hands**: Combines counts across all detected hands
- **Smoothing**: 10-frame rolling buffer prevents jitter

### Audio Synthesis

The bass drop is synthesized in real-time:
```javascript
// Frequency: 90Hz → 40Hz (exponential)
// Gain: 0.0001 → 0.8 → 0.0001
// Duration: 0.3 seconds
```
No external audio files needed!

## 🚧 Troubleshooting

**Camera not working?**
- Ensure you're on HTTPS or localhost
- Check browser camera permissions
- Close other apps using the camera

**Hands not detected?**
- Improve lighting
- Move hands closer (but not too close)
- Ensure palms face camera
- Try different hand positions

**Performance issues?**
- Lower the intensity slider
- Close other browser tabs
- Try a simpler background

## 🌐 Deployment

The app automatically deploys to GitHub Pages via `.github/workflows/pages.yml`:

```yaml
# Serves index.html, style.css, script.js
# Updates on push to main branch
# Available at: https://namitzz.github.io/67/
```

## 🎬 Python Desktop Version

A Python/OpenCV desktop version is also available in this repo:

```bash
pip install -r requirements.txt
python detector.py
```

Features offline usage and additional customization options.

## 🤝 Contributing

Ideas for contributions:
- 📹 Add MediaRecorder for video recording/download
- 📤 Add share button for social media
- 🎨 Add custom overlay upload
- 🎵 Add custom sound upload
- 🌈 Add more animation effects
- 📱 Improve mobile performance

## 📝 License

Open source - feel free to use and modify!

## 🎉 Credits

Built with:
- [MediaPipe](https://mediapipe.dev/) - Google's ML framework
- Web Audio API - For synthesized sounds
- Inspired by viral TikTok/Instagram "67" trend
- Made with ❤️ for the meme community

---

**#67Meme — Inspired by TikTok trend** 🔥💯

**[Try it now!](https://namitzz.github.io/67/)**