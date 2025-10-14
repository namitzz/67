#!/usr/bin/env python3
"""
Test script for the 6-7 Meme Detector
Tests the core logic without requiring a camera
"""

import sys
import numpy as np

def test_imports():
    """Test that all required modules can be imported"""
    print("Testing imports...")
    try:
        import cv2
        print(f"✓ OpenCV imported successfully (version: {cv2.__version__})")
    except ImportError as e:
        print(f"✗ Failed to import OpenCV: {e}")
        return False
    
    try:
        import mediapipe as mp
        print(f"✓ MediaPipe imported successfully (version: {mp.__version__})")
    except ImportError as e:
        print(f"✗ Failed to import MediaPipe: {e}")
        return False
    
    try:
        import numpy as np
        print(f"✓ NumPy imported successfully (version: {np.__version__})")
    except ImportError as e:
        print(f"✗ Failed to import NumPy: {e}")
        return False
    
    try:
        from PIL import Image
        print(f"✓ Pillow imported successfully")
    except ImportError as e:
        print(f"✗ Failed to import Pillow: {e}")
        return False
    
    return True

def test_detector_class():
    """Test that the detector class can be instantiated"""
    print("\nTesting detector class...")
    try:
        from detector import SixSevenDetector
        detector = SixSevenDetector()
        print("✓ SixSevenDetector instantiated successfully")
        return True
    except Exception as e:
        print(f"✗ Failed to instantiate SixSevenDetector: {e}")
        return False

def test_detector_methods():
    """Test detector methods without camera"""
    print("\nTesting detector methods...")
    try:
        from detector import SixSevenDetector
        detector = SixSevenDetector()
        
        # Test that methods exist
        assert hasattr(detector, 'count_fingers'), "count_fingers method missing"
        print("✓ count_fingers method exists")
        
        assert hasattr(detector, 'detect_six_seven'), "detect_six_seven method missing"
        print("✓ detect_six_seven method exists")
        
        assert hasattr(detector, 'create_meme_overlay'), "create_meme_overlay method missing"
        print("✓ create_meme_overlay method exists")
        
        assert hasattr(detector, 'run'), "run method missing"
        print("✓ run method exists")
        
        # Test meme overlay creation with a dummy frame
        import cv2
        dummy_frame = np.zeros((480, 640, 3), dtype=np.uint8)
        detector.meme_mode = True
        detector.meme_start_time = 0
        result = detector.create_meme_overlay(dummy_frame)
        assert result.shape == dummy_frame.shape, "Meme overlay changed frame shape"
        print("✓ create_meme_overlay works with dummy frame")
        
        return True
    except Exception as e:
        print(f"✗ Method test failed: {e}")
        import traceback
        traceback.print_exc()
        return False

def main():
    print("=" * 60)
    print("6-7 Meme Detector Test Suite")
    print("=" * 60)
    
    all_passed = True
    
    # Test imports
    if not test_imports():
        all_passed = False
        print("\n⚠ Warning: Some dependencies are missing.")
        print("Run: pip install -r requirements.txt")
    
    # Test detector class
    if not test_detector_class():
        all_passed = False
    
    # Test detector methods
    if not test_detector_methods():
        all_passed = False
    
    print("\n" + "=" * 60)
    if all_passed:
        print("✓ All tests passed!")
        print("The detector is ready to use. Run: python detector.py")
    else:
        print("✗ Some tests failed.")
        print("Please check the errors above and install missing dependencies.")
    print("=" * 60)
    
    return 0 if all_passed else 1

if __name__ == "__main__":
    sys.exit(main())
