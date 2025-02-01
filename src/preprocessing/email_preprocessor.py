import re
from bs4 import BeautifulSoup
from utils.logger import logger

class EmailPreprocessor:
    def _init_(self):
        self.logger = logger

    def clean_email(self, email_content):
        """Clean email content by removing HTML tags and special characters."""
        try:
            # Remove HTML tags
            soup = BeautifulSoup(email_content, "html.parser")
            text = soup.get_text()
            # Remove special characters
            text = re.sub(r"[^a-zA-Z0-9\s]", "", text)
            return text
        except Exception as e:
            self.logger.error(f"Failed to clean email: {e}")
            return None