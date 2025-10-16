# 67 Meme Camera Effect - Demo & Usage Guide

This guide will walk you through using the new 67 Meme Camera Effect with practical examples and tips.

## 📸 Screenshot

### Main Interface

![Main Interface](https://github.com/user-attachments/assets/c461c2bb-c0a1-41a1-9d1f-c805608bc58d)

The interface features:
- Clean dark theme with centered camera stage (16:9 aspect ratio)
- Fullscreen dark background
- Control panel with Start/Stop/Fullscreen buttons
- Customization controls: Sound toggle, Intensity slider, Cooldown slider, Party mode
- Status message display
- Footer with TikTok trend credit

## 🎯 Quick Start

1. **Open the app** - Visit https://namitzz.github.io/67/
2. **Click "Start camera"** - Allow camera access when prompted
3. **Show 6 or 7 fingers** - Try 3+3, 3+4, or 5+2
4. **Watch the explosion!** 💥

## 🎨 Visual Effects

When you trigger (show 6 or 7 fingers):

- 🎬 **Screen shakes** - Earthquake effect
- 🔍 **Screen zooms** - Pulsating in/out
- ⚡ **Flash effect** - White pulses (5 times)
- 💥 **Text spam** - Random "67" texts across screen
- 🔊 **Bass drop** - Synthesized sound (90Hz → 40Hz)
- ⏱️ **Duration** - Effects last ~2.2 seconds

## 🎮 Controls

### Sound Toggle
Enable/disable the bass drop sound effect

### Intensity Slider (10-120)
Controls how many meme texts appear
- Low (10-30): Subtle effect
- Medium (40-70): Balanced
- High (80-120): Maximum chaos!

### Cooldown Slider (800-4000ms)
Time between allowed triggers
- Short (800-1500ms): Rapid firing
- Medium (1500-3000ms): Balanced
- Long (3000-4000ms): Controlled

### Party Mode
Double the meme texts for extra effect! 🎉

### Fullscreen
Go fullscreen for immersive experience

## 🖐️ Hand Gestures

Easy ways to trigger:

### Option 1: Three + Three (6 total)
```
Left hand:  👌 (3 fingers)
Right hand: 👌 (3 fingers)
Total: 6 = TRIGGER! 🔥
```

### Option 2: Three + Four (7 total)
```
Left hand:  👌 (3 fingers)
Right hand: ✋ (4 fingers)
Total: 7 = TRIGGER! 🔥
```

### Option 3: Five + Two (7 total)
```
Left hand:  ✋ (5 fingers)
Right hand: ✌️ (2 fingers)
Total: 7 = TRIGGER! 🔥
```

## 💡 Pro Tips

✅ **For Best Results:**
- Use good lighting
- Keep hands 1-2 feet from camera
- Face palms toward camera
- Hold gesture steady for ~1 second

❌ **Avoid:**
- Very dim lighting
- Moving hands too quickly
- Blocking hands with objects
- Getting too close (cuts off frame)

## 🛠️ Troubleshooting

### Camera Not Starting
- Check browser permissions
- Ensure HTTPS or localhost
- Close other apps using camera

### Gesture Not Detected
- Improve lighting
- Hold hands steadier
- Try different finger combinations
- Check MediaPipe loaded (no console errors)

### Performance Issues
- Lower intensity slider
- Close other browser tabs
- Try different browser (Chrome recommended)

## 📱 Mobile Support

Works on:
- ✅ iOS Safari
- ✅ Chrome Android
- ✅ Samsung Internet

Tips for mobile:
- Use front camera
- Prop phone against something
- Ensure good lighting

## 🎬 Use Cases

### TikTok/Instagram Content
Record screen while triggering effect on beat

### Party Entertainment
Connect to TV, let guests trigger effects

### Virtual Meetings
Fun icebreaker for remote teams

## 🔧 How It Works

**Detection:**
- MediaPipe Hands detects up to 2 hands
- Counts extended fingers (tip above joint)
- Requires 5/10 frames to match (smoothing)
- Cooldown prevents spam

**Effects:**
- CSS animations (shake, zoom, flash)
- JavaScript spawns random text elements
- Web Audio API synthesizes bass sound
- Auto-cleanup after 2.2 seconds

## 🌟 Technical Details

- **Frame rate**: 30-60 FPS
- **Detection latency**: ~50-100ms
- **Trigger delay**: ~300-500ms
- **Effect duration**: 2200ms
- **Browser**: Chrome/Edge recommended

## 🎉 Share Your Creations

Tag with:
- #67Meme
- #67MemeCamera
- #TikTokTrend

---

**Have fun creating viral content!** 🔥💯

For more info, see [README.md](README.md) or [FAQ.md](FAQ.md)
