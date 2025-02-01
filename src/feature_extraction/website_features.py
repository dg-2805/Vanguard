from bs4 import BeautifulSoup
from typing import Dict

class WebsiteFeatureExtractor:
    def extract_features(self, html_content: str) -> Dict:
        """Extract features from website HTML content."""
        soup = BeautifulSoup(html_content, "html.parser")
        features = {
            "num_links": len(soup.find_all("a")),
            "num_images": len(soup.find_all("img")),
            "num_forms": len(soup.find_all("form")),
            "has_login_form": self._has_login_form(soup),
            "has_external_scripts": self._has_external_scripts(soup),
        }
        return features

    def _has_login_form(self, soup) -> bool:
        """Check if the website has a login form."""
        for form in soup.find_all("form"):
            if "login" in form.get("action", "").lower():
                return True
        return False

    def _has_external_scripts(self, soup) -> bool:
        """Check if the website uses external scripts."""
        for script in soup.find_all("script"):
            if script.get("src") and "http" in script.get("src"):
                return True
        return False