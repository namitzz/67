#!/usr/bin/env python3
"""
6-7 Meme Detector
A gesture detector that uses camera to detect the "6 7" gesture (finger counting)
and floods the screen with "6 7" memes when detected.
"""

import cv2
import mediapipe as mp
import numpy as np
import time
from collections import deque

class SixSevenDetector:
    def __init__(self):
        # Initialize MediaPipe Hands
        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands(
            static_image_mode=False,
            max_num_hands=2,
            min_detection_confidence=0.7,
            min_tracking_confidence=0.5
        )
        self.mp_draw = mp.solutions.drawing_utils
        
        # State tracking
        self.detection_history = deque(maxlen=10)
        self.meme_mode = False
        self.meme_start_time = 0
        self.meme_duration = 5  # Show memes for 5 seconds
        
    def count_fingers(self, hand_landmarks, handedness):
        """
        Count the number of extended fingers on a hand
        """
        # Finger tip and PIP landmark indices
        finger_tips = [
            self.mp_hands.HandLandmark.THUMB_TIP,
            self.mp_hands.HandLandmark.INDEX_FINGER_TIP,
            self.mp_hands.HandLandmark.MIDDLE_FINGER_TIP,
            self.mp_hands.HandLandmark.RING_FINGER_TIP,
            self.mp_hands.HandLandmark.PINKY_TIP
        ]
        
        finger_pips = [
            self.mp_hands.HandLandmark.THUMB_IP,
            self.mp_hands.HandLandmark.INDEX_FINGER_PIP,
            self.mp_hands.HandLandmark.MIDDLE_FINGER_PIP,
            self.mp_hands.HandLandmark.RING_FINGER_PIP,
            self.mp_hands.HandLandmark.PINKY_PIP
        ]
        
        count = 0
        
        # Check each finger
        for tip_idx, pip_idx in zip(finger_tips, finger_pips):
            tip = hand_landmarks.landmark[tip_idx]
            pip = hand_landmarks.landmark[pip_idx]
            
            # For thumb, check horizontal distance
            if tip_idx == self.mp_hands.HandLandmark.THUMB_TIP:
                thumb_cmc = hand_landmarks.landmark[self.mp_hands.HandLandmark.THUMB_CMC]
                if handedness == "Right":
                    if tip.x < thumb_cmc.x:
                        count += 1
                else:  # Left hand
                    if tip.x > thumb_cmc.x:
                        count += 1
            else:
                # For other fingers, check if tip is above PIP
                if tip.y < pip.y:
                    count += 1
        
        return count
    
    def detect_six_seven(self, results):
        """
        Detect if hands are showing 6, 7, or the combination
        """
        if not results.multi_hand_landmarks:
            return False, []
        
        finger_counts = []
        
        for idx, hand_landmarks in enumerate(results.multi_hand_landmarks):
            # Get handedness (Left or Right)
            handedness = results.multi_handedness[idx].classification[0].label
            
            # Count fingers
            count = self.count_fingers(hand_landmarks, handedness)
            finger_counts.append(count)
        
        # Check if we have 6 or 7 fingers shown
        has_six = 6 in finger_counts
        has_seven = 7 in finger_counts
        
        # Detect 6-7 combination (two hands showing different counts that sum to something meaningful)
        detected = has_six or has_seven
        
        # Also check for creative combinations: one hand with 3 and another with 3 or 4
        if len(finger_counts) == 2:
            total = sum(finger_counts)
            if total == 13 or total == 12:  # 6+7 or similar combinations
                detected = True
        
        return detected, finger_counts
    
    def create_meme_overlay(self, frame):
        """
        Create a meme overlay flooding the screen with '6 7' text
        """
        h, w = frame.shape[:2]
        
        # Create semi-transparent overlay
        overlay = frame.copy()
        
        # Random positions for meme text
        font = cv2.FONT_HERSHEY_BOLD
        
        # Calculate how many memes to show based on time
        elapsed = time.time() - self.meme_start_time
        num_memes = min(int(elapsed * 10) + 5, 50)
        
        for i in range(num_memes):
            # Random position
            x = np.random.randint(0, max(1, w - 100))
            y = np.random.randint(50, h - 10)
            
            # Random size
            scale = np.random.uniform(0.5, 2.5)
            
            # Random color (bright colors)
            color = (
                np.random.randint(100, 255),
                np.random.randint(100, 255),
                np.random.randint(100, 255)
            )
            
            # Draw "6 7" or "67" randomly
            texts = ["6 7", "67", "🔥 6 7 🔥", "SIX SEVEN", "6️⃣7️⃣"]
            text = np.random.choice(texts)
            
            thickness = int(scale * 2)
            cv2.putText(overlay, text, (x, y), font, scale, color, thickness)
        
        # Add main centered message
        center_text = "🔥 6 7 DETECTED! 🔥"
        text_size = cv2.getTextSize(center_text, font, 2, 4)[0]
        text_x = (w - text_size[0]) // 2
        text_y = (h + text_size[1]) // 2
        
        # Pulsating effect
        pulse = abs(np.sin(elapsed * 3)) * 0.3 + 0.7
        pulse_scale = 2 * pulse
        
        cv2.putText(overlay, center_text, (text_x, text_y), font, 
                   pulse_scale, (0, 255, 255), 6)
        
        # Blend with original frame
        alpha = 0.7
        frame = cv2.addWeighted(overlay, alpha, frame, 1 - alpha, 0)
        
        return frame
    
    def run(self):
        """
        Main loop for the detector
        """
        cap = cv2.VideoCapture(0)
        
        if not cap.isOpened():
            print("Error: Could not open camera")
            return
        
        print("6-7 Meme Detector Started!")
        print("Show 6 or 7 fingers to trigger the meme flood!")
        print("Press 'q' to quit")
        
        while True:
            ret, frame = cap.read()
            if not ret:
                print("Error: Could not read frame")
                break
            
            # Flip frame horizontally for mirror effect
            frame = cv2.flip(frame, 1)
            
            # Convert to RGB for MediaPipe
            rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            
            # Process the frame
            results = self.hands.process(rgb_frame)
            
            # Detect 6-7 gesture
            detected, finger_counts = self.detect_six_seven(results)
            
            # Update detection history
            self.detection_history.append(detected)
            
            # Trigger meme mode if detected consistently
            if sum(self.detection_history) >= 5 and not self.meme_mode:
                self.meme_mode = True
                self.meme_start_time = time.time()
                print("🔥 6-7 DETECTED! MEME MODE ACTIVATED! 🔥")
            
            # Check if meme mode should end
            if self.meme_mode:
                if time.time() - self.meme_start_time > self.meme_duration:
                    self.meme_mode = False
                    print("Meme mode ended. Ready for next detection!")
            
            # Draw hand landmarks
            if results.multi_hand_landmarks:
                for hand_landmarks in results.multi_hand_landmarks:
                    self.mp_draw.draw_landmarks(
                        frame, hand_landmarks, self.mp_hands.HAND_CONNECTIONS)
            
            # Display finger counts
            if finger_counts:
                y_offset = 30
                for i, count in enumerate(finger_counts):
                    text = f"Hand {i+1}: {count} fingers"
                    cv2.putText(frame, text, (10, y_offset), 
                               cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
                    y_offset += 30
            
            # Apply meme overlay if in meme mode
            if self.meme_mode:
                frame = self.create_meme_overlay(frame)
            
            # Display detection status
            status_text = "MEME MODE!" if self.meme_mode else "Ready to detect 6-7..."
            status_color = (0, 0, 255) if self.meme_mode else (0, 255, 0)
            cv2.putText(frame, status_text, (10, frame.shape[0] - 20),
                       cv2.FONT_HERSHEY_SIMPLEX, 0.7, status_color, 2)
            
            # Show frame
            cv2.imshow('6-7 Meme Detector', frame)
            
            # Check for quit
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        
        # Cleanup
        cap.release()
        cv2.destroyAllWindows()
        self.hands.close()


def main():
    detector = SixSevenDetector()
    detector.run()


if __name__ == "__main__":
    main()
