from unittest.mock import AsyncMock, patch

import pytest


@pytest.mark.asyncio
async def test_convert_endpoint_success(client):
    """Test successful currency conversion"""
    mock_result = {"converted_amount": 100.0, "cached": False}
    with patch("app.api.convert_currency", AsyncMock(return_value=mock_result)):
        response = client.get("/convert?from_currency=USD&to_currency=EUR&amount=50")
        assert response.status_code == 200
        assert response.json() == mock_result


@pytest.mark.asyncio
async def test_convert_endpoint_invalid_params(client):
    """Test validation for missing parameters"""
    response = client.get("/convert")
    assert response.status_code == 422  # Validation error


@pytest.mark.asyncio
async def test_convert_endpoint_invalid_currency(client):
    """Test handling of invalid currency codes"""
    with patch(
        "app.api.convert_currency",
        AsyncMock(side_effect=ValueError("Invalid currency code")),
    ):
        response = client.get(
            "/convert?from_currency=INVALID&to_currency=EUR&amount=50"
        )
        assert response.status_code == 400
        assert response.json() == {"detail": "Invalid currency code"}


@pytest.mark.asyncio
async def test_convert_endpoint_network_error(client):
    """Test handling of network errors"""
    with patch(
        "app.api.convert_currency",
        AsyncMock(side_effect=ConnectionError("Network error")),
    ):
        response = client.get("/convert?from_currency=USD&to_currency=EUR&amount=50")
        assert response.status_code == 400
        assert response.json() == {"detail": "Network error"}
