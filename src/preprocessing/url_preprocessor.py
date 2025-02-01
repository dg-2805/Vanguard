from urllib.parse import urlparse
from utils.logger import logger

class URLPreprocessor:
    def _init_(self):
        self.logger = logger

    def extract_domain(self, url):
        """Extract domain from a URL."""
        try:
            parsed_url = urlparse(url)
            return parsed_url.netloc
        except Exception as e:
            self.logger.error(f"Failed to extract domain: {e}")
            return None