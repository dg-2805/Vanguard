import requests
from typing import List

class BlacklistUpdater:
    def _init_(self, blacklist_url: str):
        self.blacklist_url = blacklist_url

    def fetch_blacklist(self) -> List[str]:
        """Fetch the latest blacklist from a remote source."""
        response = requests.get(self.blacklist_url)
        if response.status_code == 200:
            return response.text.splitlines()
        return []

    def update_blacklist(self, file_path: str):
        """Update the local blacklist file."""
        blacklist = self.fetch_blacklist()
        with open(file_path, "w") as f:
            f.write("\n".join(blacklist))
        print(f"Blacklist updated at {file_path}")