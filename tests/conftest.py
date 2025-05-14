from unittest.mock import MagicMock, patch

import pytest
from fastapi.testclient import TestClient

from app.main import app

# Create mock settings
mock_settings = MagicMock(
    api_base_url="https://mock-api.com",
    api_key="mock-key",
    redis_host="localhost",
    redis_port=6379,
)


@pytest.fixture
def client():
    """Test client fixture with mocked Redis"""
    with patch("app.services.redis_client"), patch(
        "app.config.settings", mock_settings
    ):
        yield TestClient(app)
