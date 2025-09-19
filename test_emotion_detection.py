"""
Test module for emotion detection package containing function for testing 
emotion_detector function from emotion_detection module
"""

# Import required libraries
import unittest
from EmotionDetection.emotion_detection import emotion_detector

class TestEmotionDetection(unittest.TestCase):
    def test_emotion_detector(self):
        """
        Tets method for emotion detector function
        """

        # Test case for expected dominant emotion of "joy"
        self.assertEqual(emotion_detector("I am glad this happened")['dominant_emotion'], "joy")

        # Test case for expected dominant emotion of "anger"
        self.assertEqual(emotion_detector("I am really mad about this")['dominant_emotion'], "anger")

        # Test case for expected dominant emotion of "disgust"
        self.assertEqual(emotion_detector("I feel disgusted just hearing about this")['dominant_emotion'], "disgust")

        # Test case for expected dominant emotion of "sadness"
        self.assertEqual(emotion_detector("I am so sad about this")['dominant_emotion'], "sadness")

        # Test case for expected dominant emotion of "fear"
        self.assertEqual(emotion_detector("I am really afraid that this will happen")['dominant_emotion'], "fear")

# Run all test methods defined in the module
unittest.main()