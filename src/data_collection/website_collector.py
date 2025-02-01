import os
import requests
import json
from utils.logger import logger
from utils.config import DATA_DIR

class WebsiteCollector:
    def __init__(self):
        self.website_data_dir = os.path.join(DATA_DIR, "websites")
        os.makedirs(self.website_data_dir, exist_ok=True)

    def collect_websites(self, source_url):
        """Collect malicious website URLs from a source."""
        try:
            response = requests.get(source_url)
            response.raise_for_status()
            websites = response.json()
            with open(os.path.join(self.website_data_dir, "malicious_websites.json"), "w") as f:
                json.dump(websites, f)
            logger.info(f"Collected {len(websites)} malicious websites.")
        except Exception as e:
            logger.error(f"Failed to collect websites: {e}")

if __name__ == "__main__":
    collector = WebsiteCollector()
    collector.collect_websites("https://example.com/malicious-websites")