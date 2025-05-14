from unittest.mock import AsyncMock, patch

import pytest
from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


@pytest.mark.asyncio
async def test_convert_endpoint_success():
    mock_result = {"converted_amount": 100.0, "cached": False}
    with patch(
        "app.api.convert_currency", AsyncMock(return_value=mock_result)
    ) as mock_convert:
        response = client.get("/convert?from_currency=USD&to_currency=EUR&amount=50")
        assert response.status_code == 200
        assert response.json() == {"converted_amount": mock_result}
        mock_convert.assert_called_once_with("USD", "EUR", 50.0)


@pytest.mark.asyncio
async def test_convert_endpoint_cached_result():
    mock_result = {"converted_amount": 100.0, "cached": True}
    with patch(
        "app.api.convert_currency", AsyncMock(return_value=mock_result)
    ) as mock_convert:
        response = client.get("/convert?from_currency=USD&to_currency=EUR&amount=50")
        assert response.status_code == 200
        assert response.json() == {"converted_amount": mock_result}
        mock_convert.assert_called_once_with("USD", "EUR", 50.0)


@pytest.mark.asyncio
async def test_convert_endpoint_negative_amount():
    mock_result = {"converted_amount": -100.0, "cached": False}
    with patch(
        "app.api.convert_currency", AsyncMock(return_value=mock_result)
    ) as mock_convert:
        response = client.get("/convert?from_currency=USD&to_currency=EUR&amount=-100")
        assert response.status_code == 200
        assert response.json() == {"converted_amount": mock_result}
        mock_convert.assert_called_once_with("USD", "EUR", -100.0)


@pytest.mark.asyncio
async def test_convert_endpoint_invalid_currency():
    with patch(
        "app.api.convert_currency",
        AsyncMock(side_effect=ValueError("Invalid currency code")),
    ) as mock_convert:
        response = client.get(
            "/convert?from_currency=INVALID&to_currency=EUR&amount=50"
        )
        assert response.status_code == 400
        assert response.json() == {"detail": "Invalid currency code"}
        mock_convert.assert_called_once_with("INVALID", "EUR", 50.0)


@pytest.mark.asyncio
async def test_convert_endpoint_decimal_amount():
    mock_result = {"converted_amount": 50.55, "cached": False}
    with patch(
        "app.api.convert_currency", AsyncMock(return_value=mock_result)
    ) as mock_convert:
        response = client.get("/convert?from_currency=USD&to_currency=EUR&amount=50.55")
        assert response.status_code == 200
        assert response.json() == {"converted_amount": mock_result}
        mock_convert.assert_called_once_with("USD", "EUR", 50.55)


@pytest.mark.asyncio
async def test_convert_endpoint_case_insensitive():
    mock_result = {"converted_amount": 100.0, "cached": False}
    with patch(
        "app.api.convert_currency", AsyncMock(return_value=mock_result)
    ) as mock_convert:
        response = client.get("/convert?from_currency=usd&to_currency=eur&amount=100")
        assert response.status_code == 200
        assert response.json() == {"converted_amount": mock_result}
        mock_convert.assert_called_once_with("usd", "eur", 100.0)


@pytest.mark.asyncio
async def test_convert_endpoint_same_currency():
    mock_result = {"converted_amount": 50.0, "cached": False}
    with patch(
        "app.api.convert_currency", AsyncMock(return_value=mock_result)
    ) as mock_convert:
        response = client.get("/convert?from_currency=USD&to_currency=USD&amount=50")
        assert response.status_code == 200
        assert response.json() == {"converted_amount": mock_result}
        mock_convert.assert_called_once_with("USD", "USD", 50.0)


@pytest.mark.asyncio
async def test_convert_endpoint_large_amount():
    mock_result = {"converted_amount": 1000000.0, "cached": False}
    with patch(
        "app.api.convert_currency", AsyncMock(return_value=mock_result)
    ) as mock_convert:
        response = client.get(
            "/convert?from_currency=USD&to_currency=EUR&amount=1000000"
        )
        assert response.status_code == 200
        assert response.json() == {"converted_amount": mock_result}
        mock_convert.assert_called_once_with("USD", "EUR", 1000000.0)


@pytest.mark.asyncio
async def test_convert_endpoint_network_error():
    with patch(
        "app.api.convert_currency",
        AsyncMock(side_effect=ConnectionError("Network error")),
    ) as mock_convert:
        response = client.get("/convert?from_currency=USD&to_currency=EUR&amount=50")
        assert response.status_code == 400
        assert response.json() == {"detail": "Network error"}
        mock_convert.assert_called_once_with("USD", "EUR", 50.0)


@pytest.mark.asyncio
async def test_convert_endpoint_missing_params():
    response = client.get("/convert")
    assert response.status_code == 422  # Validation error
