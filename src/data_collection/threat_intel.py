import os
import requests
import json
from utils.logger import logger
from utils.config import DATA_DIR

class ThreatIntelCollector:
    def __init__(self):
        self.threat_intel_dir = os.path.join(DATA_DIR, "threat_intelligence")
        os.makedirs(self.threat_intel_dir, exist_ok=True)

    def fetch_threat_intel(self, feed_url):
        """Fetch threat intelligence data from a feed."""
        try:
            response = requests.get(feed_url)
            response.raise_for_status()
            intel_data = response.json()
            with open(os.path.join(self.threat_intel_dir, "threat_intel.json"), "w") as f:
                json.dump(intel_data, f)
            logger.info("Threat intelligence data collected.")
        except Exception as e:
            logger.error(f"Failed to fetch threat intelligence: {e}")

if __name__ == "__main__":
    collector = ThreatIntelCollector()
    collector.fetch_threat_intel("https://example.com/threat-intel-feed")