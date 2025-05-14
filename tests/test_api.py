from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_conversion():
    response = client.get("/convert?from_currency=USD&to_currency=EUR&amount=100")
    assert response.status_code == 200
    assert "converted_amount" in response.json()
