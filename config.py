# Configuration file for 6-7 Meme Detector
# Edit these values to customize the detector's behavior

# Detection Settings
MIN_DETECTION_CONFIDENCE = 0.7  # Range: 0.0 to 1.0 (higher = stricter)
MIN_TRACKING_CONFIDENCE = 0.5   # Range: 0.0 to 1.0
MAX_NUM_HANDS = 2                # Maximum hands to detect (1 or 2)

# Trigger Settings
DETECTION_THRESHOLD = 5          # Frames needed to trigger (out of 10)
HISTORY_LENGTH = 10              # Number of frames to track

# Meme Display Settings
MEME_DURATION = 5.0              # Seconds to show memes
MIN_MEMES = 5                    # Minimum number of meme texts
MAX_MEMES = 50                   # Maximum number of meme texts
MEME_GROWTH_RATE = 10            # How fast memes multiply over time

# Visual Settings
OVERLAY_ALPHA = 0.7              # Transparency of meme overlay (0.0 to 1.0)
PULSE_SPEED = 3                  # Speed of center text pulsation

# Meme Text Options
MEME_TEXTS = [
    "6 7",
    "67", 
    "🔥 6 7 🔥",
    "SIX SEVEN",
    "6️⃣7️⃣",
    "S I X  S E V E N",
    "★ 67 ★",
    "6•7",
]

# Camera Settings
CAMERA_INDEX = 0                 # Camera device index (0 = default)
FLIP_CAMERA = True              # Mirror the camera feed

# Window Settings
WINDOW_NAME = "6-7 Meme Detector"

# Color Settings (BGR format)
STATUS_COLOR_READY = (0, 255, 0)      # Green
STATUS_COLOR_ACTIVE = (0, 0, 255)     # Red
FINGER_COUNT_COLOR = (0, 255, 0)      # Green
CENTER_TEXT_COLOR = (0, 255, 255)     # Yellow

# Instructions
"""
HOW TO USE THIS CONFIG FILE:

1. Edit the values above to customize the detector
2. Save the file
3. Run the detector normally: python3 detector.py
4. The new settings will be applied automatically

TIPS:
- Lower MIN_DETECTION_CONFIDENCE for easier detection
- Increase DETECTION_THRESHOLD for fewer false triggers  
- Adjust MEME_DURATION to change how long memes display
- Add your own text to MEME_TEXTS list
- Set FLIP_CAMERA to False if mirror effect is unwanted

TROUBLESHOOTING:
- If detection is too sensitive: increase DETECTION_THRESHOLD
- If detection is too difficult: lower MIN_DETECTION_CONFIDENCE
- If too many memes: reduce MAX_MEMES or MEME_GROWTH_RATE
- If wrong camera opens: change CAMERA_INDEX
"""
