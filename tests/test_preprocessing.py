import unittest
from src.preprocessing.email_preprocessor import EmailPreprocessor

class TestPreprocessing(unittest.TestCase):
    def test_email_cleaning(self):
        preprocessor = EmailPreprocessor()
        cleaned_email = preprocessor.clean_email("<html>Test email</html>")
        self.assertEqual(cleaned_email, "Test email")