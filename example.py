#!/usr/bin/env python3
"""
Example script showing how to use the detector programmatically
or create simulated detections for testing
"""

import numpy as np
import cv2
from detector import SixSevenDetector

def simulate_detection_test():
    """
    Simulate a detection scenario without requiring a camera.
    Useful for testing or demonstration purposes.
    """
    print("=" * 60)
    print("Simulated Detection Test")
    print("=" * 60)
    print()
    
    # Create detector instance
    detector = SixSevenDetector()
    print("✓ Detector initialized")
    
    # Create a dummy frame (black image)
    dummy_frame = np.zeros((480, 640, 3), dtype=np.uint8)
    
    # Test meme overlay creation
    print("✓ Testing meme overlay generation...")
    detector.meme_mode = True
    detector.meme_start_time = 0
    
    result_frame = detector.create_meme_overlay(dummy_frame.copy())
    assert result_frame.shape == dummy_frame.shape, "Frame shape mismatch!"
    print("✓ Meme overlay generated successfully")
    
    # Test detection history
    print("✓ Testing detection history...")
    detector.detection_history.clear()
    for i in range(10):
        detector.detection_history.append(i >= 5)
    
    detections = sum(detector.detection_history)
    print(f"  Detection count: {detections}/10")
    
    # Show configuration
    print("\n✓ Current configuration:")
    try:
        from config import (
            MIN_DETECTION_CONFIDENCE,
            DETECTION_THRESHOLD,
            MEME_DURATION,
            MAX_MEMES
        )
        print(f"  - Detection confidence: {MIN_DETECTION_CONFIDENCE}")
        print(f"  - Detection threshold: {DETECTION_THRESHOLD}")
        print(f"  - Meme duration: {MEME_DURATION}s")
        print(f"  - Max memes: {MAX_MEMES}")
    except ImportError:
        print("  - Using default configuration")
    
    print("\n" + "=" * 60)
    print("✓ All simulation tests passed!")
    print("=" * 60)
    print()
    print("To test with a real camera, run: python3 detector.py")

def show_finger_counting_example():
    """
    Show how finger counting logic works
    """
    print("\n" + "=" * 60)
    print("Finger Counting Logic Example")
    print("=" * 60)
    print()
    print("The detector counts fingers by comparing:")
    print("  1. Finger tip position (e.g., INDEX_FINGER_TIP)")
    print("  2. Finger joint position (e.g., INDEX_FINGER_PIP)")
    print()
    print("A finger is 'extended' if:")
    print("  - Tip Y-coordinate < Joint Y-coordinate")
    print("  - (For thumb: check X-coordinate instead)")
    print()
    print("Detection triggers when:")
    print("  - 6 or 7 fingers detected on any combination of hands")
    print("  - Consistent across multiple frames (temporal smoothing)")
    print()
    
def show_meme_examples():
    """
    Show examples of meme texts that will be displayed
    """
    print("\n" + "=" * 60)
    print("Meme Text Examples")
    print("=" * 60)
    print()
    
    try:
        from config import MEME_TEXTS
        print("Configured meme texts:")
        for i, text in enumerate(MEME_TEXTS, 1):
            print(f"  {i}. {text}")
    except ImportError:
        default_texts = ["6 7", "67", "🔥 6 7 🔥", "SIX SEVEN", "6️⃣7️⃣"]
        print("Default meme texts:")
        for i, text in enumerate(default_texts, 1):
            print(f"  {i}. {text}")
    
    print()
    print("These texts appear randomly with:")
    print("  - Random positions on screen")
    print("  - Random sizes (0.5x to 2.5x)")
    print("  - Random bright colors")
    print("  - Increasing quantity over time")

def main():
    """Run all examples"""
    try:
        simulate_detection_test()
        show_finger_counting_example()
        show_meme_examples()
        
        print("\n" + "=" * 60)
        print("Example completed successfully!")
        print("=" * 60)
        print()
        print("Next steps:")
        print("  1. Run: python3 detector.py")
        print("  2. Show 6 or 7 fingers to your camera")
        print("  3. Watch the meme flood!")
        print()
        
    except Exception as e:
        print(f"\n❌ Error running example: {e}")
        import traceback
        traceback.print_exc()
        return 1
    
    return 0

if __name__ == "__main__":
    import sys
    sys.exit(main())
