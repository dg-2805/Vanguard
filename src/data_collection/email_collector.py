import os
import requests
import json
from utils.logger import logger
from utils.config import DATA_DIR

class EmailCollector:
    def __init__(self):
        self.email_data_dir = os.path.join(DATA_DIR, "emails")
        os.makedirs(self.email_data_dir, exist_ok=True)

    def collect_emails(self, source_url):
        """Collect phishing emails from a source URL."""
        try:
            response = requests.get(source_url)
            response.raise_for_status()
            emails = response.json()
            with open(os.path.join(self.email_data_dir, "phishing_emails.json"), "w") as f:
                json.dump(emails, f)
            logger.info(f"Collected {len(emails)} phishing emails.")
        except Exception as e:
            logger.error(f"Failed to collect emails: {e}")

if __name__ == "__main__":
    collector = EmailCollector()
    collector.collect_emails("https://example.com/phishing-emails")