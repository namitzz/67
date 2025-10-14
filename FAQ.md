# Frequently Asked Questions (FAQ)

## General Questions

### Q: What is the "6 7" meme?
**A:** It's a popular internet meme/gesture. This detector recognizes when someone shows 6 or 7 fingers and responds with a flood of meme text!

### Q: Do I need a special camera?
**A:** No! Any webcam will work. Built-in laptop cameras work great.

### Q: Does it work on mobile devices?
**A:** This version is designed for desktop/laptop computers. Mobile support could be added in the future!

## Technical Questions

### Q: Which Python version do I need?
**A:** Python 3.7 or higher. We recommend Python 3.8+.

### Q: What are the system requirements?
**A:**
- Python 3.7+
- Webcam/camera
- ~100MB disk space for dependencies
- 2GB+ RAM recommended
- Any modern OS (Windows, macOS, Linux)

### Q: Can I use this without OpenCV or MediaPipe?
**A:** No, these are essential dependencies for hand detection and camera access.

### Q: Why does it need so many dependencies?
**A:**
- **OpenCV**: Camera access and image processing
- **MediaPipe**: Advanced hand landmark detection (Google's ML model)
- **NumPy**: Fast numerical operations
- **Pillow**: Image manipulation utilities

## Usage Questions

### Q: How do I show 6 fingers with one hand?
**A:** That's tricky! The detector is flexible and accepts various interpretations. Try:
- Using both hands (3+3, 4+2, etc.)
- The algorithm might detect 5 fingers as 6 in certain positions
- Be creative with your gestures!

### Q: How do I show 7 fingers?
**A:** Use two hands! Examples:
- 3 fingers + 4 fingers = 7
- 2 fingers + 5 fingers = 7
- Any combination that totals 7

### Q: Why doesn't it detect my gesture?
**A:** Try these solutions:
1. Improve lighting in your room
2. Move closer to the camera (1-2 feet is ideal)
3. Use a plain background
4. Hold your hands steady for 1-2 seconds
5. Make sure your fingers are clearly separated
6. Face your palms toward the camera

### Q: How sensitive is the detection?
**A:** The detector uses a 10-frame history buffer. You need to consistently show the gesture for about 5 frames (less than a second) to trigger the meme mode.

### Q: Can I change the detection sensitivity?
**A:** Yes! Edit `detector.py`:
- Line ~213: Change `sum(self.detection_history) >= 5` to a lower number for higher sensitivity
- Line ~18: Adjust `min_detection_confidence` (0.7 = strict, 0.3 = loose)

### Q: How long does the meme flood last?
**A:** 5 seconds by default. You can change this by editing `self.meme_duration` on line ~25 in `detector.py`.

### Q: Can I trigger it multiple times?
**A:** Yes! After the 5-second meme display ends, you can trigger it again by showing the gesture.

## Troubleshooting

### Q: "ModuleNotFoundError: No module named 'cv2'"
**A:** Run: `pip install -r requirements.txt`

### Q: "ModuleNotFoundError: No module named 'mediapipe'"
**A:** Run: `pip install -r requirements.txt`

### Q: Camera opens but hands aren't detected
**A:**
1. Check lighting - make sure your room is well-lit
2. Ensure your hands are visible in the camera frame
3. Try adjusting the `min_detection_confidence` in the code

### Q: Error: "Could not open camera"
**A:**
1. Make sure no other application is using your camera
2. Check camera permissions in your OS settings
3. Try a different camera if you have multiple
4. On Linux, you might need to add yourself to the `video` group

### Q: The program is laggy/slow
**A:**
1. Close other applications
2. Your computer might be underpowered
3. Try reducing the camera resolution in the code
4. Reduce the number of memes displayed (edit line ~125)

### Q: Installation fails with timeout errors
**A:**
1. Check your internet connection
2. Try: `pip install --default-timeout=300 -r requirements.txt`
3. Install packages one by one if bulk install fails

## Customization Questions

### Q: Can I change the meme text?
**A:** Yes! Edit the `texts` array in `create_meme_overlay()` function (around line ~137).

### Q: Can I add images instead of text?
**A:** Yes, but it requires code modification. You'd need to:
1. Load meme images using PIL/OpenCV
2. Modify `create_meme_overlay()` to place images instead of text
3. Handle image resizing and positioning

### Q: Can I detect other numbers?
**A:** Absolutely! Modify the `detect_six_seven()` function to check for different finger counts.

### Q: Can I add sound effects?
**A:** Yes! Install `pygame` or `playsound` and add sound playback when meme mode triggers.

### Q: Can I save the video with memes?
**A:** Yes! Use OpenCV's `VideoWriter` to record the output. Add this to the main loop.

## Platform-Specific Questions

### Q: Does it work on macOS?
**A:** Yes! Make sure to:
1. Install Python 3 via Homebrew or python.org
2. Grant camera permissions when prompted
3. Use `start.sh` to launch

### Q: Does it work on Linux?
**A:** Yes! On most distros:
```bash
sudo apt-get install python3-pip
pip install -r requirements.txt
python3 detector.py
```

### Q: Does it work on Windows?
**A:** Yes! Just:
1. Install Python from python.org
2. Double-click `start.bat` or run `python detector.py`

### Q: Raspberry Pi support?
**A:** Yes, but it might be slow. Use a Pi 4 for best results. You may need to install additional system packages.

## Privacy & Security

### Q: Does this send my camera feed anywhere?
**A:** No! Everything runs locally on your computer. No data is transmitted.

### Q: Is it safe to use?
**A:** Yes! The code is open source and you can review it. It only accesses your camera when you run it.

### Q: Can I use this in a public space?
**A:** Be mindful of others' privacy if using in public spaces with cameras.

## Contributing

### Q: Can I contribute to this project?
**A:** Absolutely! Pull requests are welcome. Some ideas:
- Add more meme variations
- Improve detection accuracy
- Add gesture combinations
- Create a GUI
- Add sound effects
- Mobile version

### Q: I found a bug, what should I do?
**A:** Open an issue on GitHub with:
- Description of the bug
- Steps to reproduce
- Your OS and Python version
- Error messages if any

### Q: Can I use this code in my project?
**A:** Yes! This is open source. Just give credit and check the license.

## Performance

### Q: What FPS should I expect?
**A:** Typically 15-30 FPS depending on your computer. MediaPipe is optimized but still requires decent hardware.

### Q: Does it use GPU?
**A:** MediaPipe can use GPU acceleration on supported systems, but CPU-only mode works fine too.

### Q: How much CPU does it use?
**A:** Expect 20-40% CPU usage on a modern processor (one core heavily utilized).

---

## Still have questions?

Open an issue on GitHub or check the code documentation in `detector.py`!
