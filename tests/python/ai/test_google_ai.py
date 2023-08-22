
import unittest
from src.python.ai.google_ai import GoogleAI

class TestGoogleAI(unittest.TestCase):

    def setUp(self):
        self.google_ai = GoogleAI()

    def test_initialize(self):
        self.assertIsInstance(self.google_ai, GoogleAI)

    def test_process(self):
        input_text = "Hello, Google AI"
        response = self.google_ai.process(input_text)
        self.assertIsInstance(response, str)

    def test_translate(self):
        input_text = "Hello, Google AI"
        target_language = "fr"
        translated_text = self.google_ai.translate(input_text, target_language)
        self.assertIsInstance(translated_text, str)

if __name__ == '__main__':
    unittest.main()
