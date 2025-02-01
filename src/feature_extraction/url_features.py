import re
from urllib.parse import urlparse
from typing import List, Dict

class URLFeatureExtractor:
    def _init_(self):
        self.features = [
            "url_length",
            "num_dots",
            "num_hyphens",
            "num_underscores",
            "num_special_chars",
            "has_ip",
            "has_port",
            "is_https",
        ]

    def extract_features(self, urls: List[str]) -> List[Dict]:
        """Extract features from a list of URLs."""
        results = []
        for url in urls:
            features = {}
            features["url_length"] = len(url)
            features["num_dots"] = url.count(".")
            features["num_hyphens"] = url.count("-")
            features["num_underscores"] = url.count("_")
            features["num_special_chars"] = len(re.findall(r"[^\w\s]", url))
            features["has_ip"] = self._has_ip(url)
            features["has_port"] = self._has_port(url)
            features["is_https"] = url.startswith("https://")
            results.append(features)
        return results

    def _has_ip(self, url: str) -> bool:
        """Check if the URL contains an IP address."""
        parsed = urlparse(url)
        host = parsed.netloc
        return bool(re.match(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", host))

    def _has_port(self, url: str) -> bool:
        """Check if the URL contains a port number."""
        parsed = urlparse(url)
        return ":" in parsed.netloc