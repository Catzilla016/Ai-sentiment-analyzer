import unittest
from EmotionDetection import emotion_detector

class TestEmotionDetection(unittest.TestCase):
    def test_sentiment_analyzer(self):
        
        case1 = emotion_detector("I am glad this happened")
        self.assertEqual(case1['dominant_emotion'], 'joy')

        case2 = emotion_detector("I am really mad about this")
        self.assertEqual(case2['dominant_emotion'], 'anger')

        case3 = emotion_detector("I feel disgusted just hearing about this")
        self.assertEqual(case3['dominant_emotion'], 'disgust')

        case4 = emotion_detector("I am so sad about this")
        self.assertEqual(case4['dominant_emotion'], 'sadness')

        case5 = emotion_detector("I am really afraid that this will happen")
        self.assertEqual(case5['dominant_emotion'], 'fear')

unittest.main()
