# Demo & Usage Guide

## Visual Walkthrough

### Normal Mode
When you first start the detector, you'll see:
- Your camera feed
- Hand landmark detection (skeleton drawn on your hands)
- Finger count for each detected hand
- Status message: "Ready to detect 6-7..."

### Meme Mode Activated! 🔥
When you show 6 or 7 fingers and hold for a moment:
- The screen floods with "6 7" text in various:
  - Sizes (small to very large)
  - Colors (bright, random colors)
  - Positions (scattered across the screen)
- A large pulsating message appears in the center: "🔥 6 7 DETECTED! 🔥"
- The text variations include:
  - "6 7"
  - "67"
  - "🔥 6 7 🔥"
  - "SIX SEVEN"
  - "6️⃣7️⃣"
- Status message changes to: "MEME MODE!" in red
- The meme flood continues for 5 seconds

## How to Trigger

### Single Hand (showing 6 fingers)
This is a bit tricky but possible! Try:
- Extend all 5 fingers on one hand fully
- The algorithm might detect it as 6 if your hand position is just right
- Or use creative positioning

### Two Hands (easier)
- Show 3 fingers on one hand and 3 on the other (total 6)
- Show 3 fingers on one hand and 4 on the other (total 7)
- Show 4 fingers on one hand and 3 on the other (total 7)

The detector looks for:
- Any hand showing 6 or 7 individual fingers (advanced!)
- Combinations of hands that suggest you're making a "6 7" gesture

## Tips for Best Results

1. **Lighting**: Make sure you're in a well-lit room
2. **Background**: Plain backgrounds work better
3. **Distance**: Keep your hands about 1-2 feet from the camera
4. **Steadiness**: Hold the gesture steady for about 1 second
5. **Hand Orientation**: Face your palm toward the camera

## Controls

- **'q'**: Quit the application
- **ESC**: (alternative) Quit the application

## Technical Details

The detector uses:
- MediaPipe's hand landmark detection (21 landmarks per hand)
- Finger counting algorithm based on tip vs PIP joint positions
- Temporal smoothing (10-frame history) to avoid false positives
- 5-second meme display duration with animated effects

## Customization

You can easily modify the behavior by editing `detector.py`:

- **Meme duration**: Change `self.meme_duration` (line ~25)
- **Detection sensitivity**: Adjust `min_detection_confidence` (line ~18)
- **Number of memes**: Modify the calculation in `create_meme_overlay()` (line ~125)
- **Meme texts**: Edit the `texts` array (line ~137)
- **Detection threshold**: Change the sum check in detection_history (line ~213)

## Troubleshooting

**Problem**: Camera not opening
- **Solution**: Make sure no other application is using your camera

**Problem**: Hands not detected
- **Solution**: Improve lighting or move closer to camera

**Problem**: False triggers
- **Solution**: Increase the detection threshold in the code

**Problem**: No triggers even with correct gesture
- **Solution**: Lower the detection confidence or hold gesture longer

## Examples of What Works

✅ **Detected:**
- 5 fingers extended fully (sometimes detected as 6)
- Two hands showing 3+3, 3+4, 4+3 fingers
- Clear, well-lit hand gestures

❌ **Not Detected:**
- Fingers too close together
- Hand too far from camera
- Poor lighting
- Blurry/fast motion

Enjoy the meme flood! 🔥
