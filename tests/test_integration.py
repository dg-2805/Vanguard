import unittest
from src.api.main import app
from fastapi.testclient import TestClient

class TestIntegration(unittest.TestCase):
    def test_api_health(self):
        client = TestClient(app)
        response = client.get("/health")
        self.assertEqual(response.status_code, 200)

if __name__ == "_main_":
    unittest.main()