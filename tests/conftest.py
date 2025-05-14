from unittest.mock import patch

import pytest
from fastapi.testclient import TestClient

from app.main import app


@pytest.fixture
def client():
    """Test client fixture with mocked Redis"""
    with patch("app.services.redis_client"):
        yield TestClient(app)
