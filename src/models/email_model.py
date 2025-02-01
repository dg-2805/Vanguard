from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from utils.logger import logger

class EmailPhishingDetector:
    def _init_(self):
        self.model = RandomForestClassifier()

    def train(self, X, y):
        """Train the phishing detection model."""
        try:
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
            self.model.fit(X_train, y_train)
            y_pred = self.model.predict(X_test)
            logger.info(f"Model trained. Accuracy: {accuracy_score(y_test, y_pred)}")
        except Exception as e:
            logger.error(f"Failed to train model: {e}")