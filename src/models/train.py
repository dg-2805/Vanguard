import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
import joblib

class ModelTrainer:
    def _init_(self, data_path: str, model_path: str):
        self.data_path = data_path
        self.model_path = model_path

    def load_data(self):
        """Load dataset from CSV."""
        return pd.read_csv(self.data_path)

    def train_model(self):
        """Train a RandomForestClassifier."""
        data = self.load_data()
        X = data.drop("label", axis=1)
        y = data["label"]

        # Split data
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        # Train model
        model = RandomForestClassifier(n_estimators=100, random_state=42)
        model.fit(X_train, y_train)

        # Evaluate model
        y_pred = model.predict(X_test)
        print(f"Accuracy: {accuracy_score(y_test, y_pred)}")
        print(f"Precision: {precision_score(y_test, y_pred)}")
        print(f"Recall: {recall_score(y_test, y_pred)}")
        print(f"F1 Score: {f1_score(y_test, y_pred)}")

        # Save model
        joblib.dump(model, self.model_path)
        print(f"Model saved to {self.model_path}")

if __name__ == "_main_":
    trainer = ModelTrainer(data_path="data/processed/training_data.csv", model_path="src/models/phishing_model.pkl")
    trainer.train_model()