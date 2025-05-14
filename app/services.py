import httpx
from app.config import settings


async def convert_currency(
    from_currency: str, to_currency: str, amount: float
) -> float:
    url = f"{settings.api_base_url}/convert"
    params = {
        "access_key": settings.api_key,
        "from": from_currency.upper(),
        "to": to_currency.upper(),
        "amount": amount,
    }

    async with httpx.AsyncClient() as client:
        response = await client.get(url, params=params)
        data = response.json()
        if "result" in data:
            return data["result"]
        raise ValueError("Invalid response from currency API.")
