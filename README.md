# 67 Meme Detector 🔥

A real-time gesture detector that uses your camera to detect the "6 7" gesture (finger counting) and floods the screen with "6 7" memes when detected!

## Features

- 🎥 Real-time camera-based hand gesture detection
- 👆 Counts fingers on both hands simultaneously
- 🔥 Triggers meme flood when 6 or 7 fingers are detected
- 💫 Animated meme overlay with random positions, sizes, and colors
- 🎨 Pulsating effect for maximum meme impact

## Requirements

- Python 3.7 or higher
- Webcam/camera
- Dependencies listed in `requirements.txt`

## Installation

1. Clone this repository:
```bash
git clone https://github.com/namitzz/67.git
cd 67
```

2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

## Usage

Run the detector:
```bash
python detector.py
```

### How to Use:

1. The application will open and access your camera
2. Show your hand(s) to the camera
3. Hold up 6 or 7 fingers to trigger the meme flood
4. The screen will flood with "6 7" memes for 5 seconds
5. Press 'q' to quit the application

### Tips:

- Make sure you're in a well-lit environment for best detection
- Hold your hand(s) steady for a moment to ensure detection
- You can trigger with one hand (6 or 7 fingers - okay, 7 is tricky with one hand!) or be creative with both hands
- The detector shows finger count for each detected hand in real-time

## How It Works

The detector uses:
- **OpenCV** for camera capture and image processing
- **MediaPipe** for hand landmark detection and tracking
- **Finger counting algorithm** that detects extended fingers on each hand
- **Meme generation** that creates a flood of animated "6 7" text overlays

When 6 or 7 fingers are detected consistently, it triggers "meme mode" which floods the screen with randomly positioned, sized, and colored "6 7" text for maximum meme effect! 🎉

## Technologies

- Python 3
- OpenCV (cv2)
- MediaPipe
- NumPy

## License

Open source - feel free to use and modify!