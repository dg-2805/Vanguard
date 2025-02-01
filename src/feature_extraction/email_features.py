from sklearn.feature_extraction.text import TfidfVectorizer
from utils.logger import logger

class EmailFeatureExtractor:
    def _init_(self):
        self.vectorizer = TfidfVectorizer(max_features=1000)

    def extract_features(self, emails):
        """Extract TF-IDF features from email content."""
        try:
            features = self.vectorizer.fit_transform(emails)
            return features
        except Exception as e:
            logger.error(f"Failed to extract email features: {e}")
            return None