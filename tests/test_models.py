import unittest
from src.models.email_model import EmailPhishingDetector

class TestModels(unittest.TestCase):
    def test_email_model(self):
        detector = EmailPhishingDetector("src/models/phishing_model.pkl")
        self.assertTrue(hasattr(detector, "model"))

if __name__ == "_main_":
    unittest.main()