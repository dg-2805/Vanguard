import requests
from utils.logger import logger

class ThreatIntelFeed:
    def _init_(self, feed_url):
        self.feed_url = feed_url

    def fetch_feed(self):
        """Fetch and return threat intelligence feed."""
        try:
            response = requests.get(self.feed_url)
            response.raise_for_status()
            return response.json()
        except Exception as e:
            logger.error(f"Failed to fetch threat intelligence feed: {e}")
            return None