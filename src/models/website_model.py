import joblib
from sklearn.base import BaseEstimator

class WebsitePhishingDetector:
    def _init_(self, model_path: str):
        self.model = joblib.load(model_path)

    def predict(self, features: dict) -> bool:
        """Predict if a website is phishing."""
        return self.model.predict([features])[0]

    def predict_proba(self, features: dict) -> float:
        """Get the probability of phishing."""
        return self.model.predict_proba([features])[0][1]