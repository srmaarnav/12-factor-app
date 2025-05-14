from unittest.mock import MagicMock, patch

import pytest
from fastapi.testclient import TestClient

# Create mock settings
mock_settings = MagicMock()
mock_settings.api_base_url = "https://mock-api.com"
mock_settings.api_key = "mock-key"
mock_settings.redis_host = "localhost"
mock_settings.redis_port = 6379


@pytest.fixture
def client():
    """Test client fixture with mocked Redis"""
    with patch("app.services.redis_client"), patch(
        "app.config.get_settings", return_value=mock_settings
    ):
        from app.main import app

        yield TestClient(app)
