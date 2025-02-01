from bs4 import BeautifulSoup

class WebsitePreprocessor:
    def clean_html(self, html_content: str) -> str:
        """Clean HTML content by removing scripts and styles."""
        soup = BeautifulSoup(html_content, "html.parser")
        for script in soup(["script", "style"]):
            script.decompose()
        return soup.get_text()

    def extract_links(self, html_content: str) -> list:
        """Extract all links from HTML content."""
        soup = BeautifulSoup(html_content, "html.parser")
        return [a.get("href") for a in soup.find_all("a", href=True)]