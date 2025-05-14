import hashlib

import httpx
import redis.asyncio as redis

from app.config import settings

try:
    redis_client = redis.from_url(
        f"redis://{settings.redis_host}:{settings.redis_port}"
    )
except Exception as e:
    raise ValueError(f"Redis connection error: {e}")


async def convert_currency(from_currency: str, to_currency: str, amount: float) -> dict:
    # Construct a cache key based on request parameters.
    cache_key = f"convert:{from_currency.upper()}:{to_currency.upper()}:{amount}"

    # Check for cached conversion result.
    cached_result = await redis_client.get(cache_key)
    if cached_result is not None:
        return {"converted_amount": float(cached_result), "cached": True}

    # If not cached, call the external API.
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
            result = data["result"]
            # Cache the result for 300 seconds (5 minutes).
            await redis_client.set(cache_key, result, ex=300)
            return {"converted_amount": result, "cached": False}
        raise ValueError("Invalid response from currency API.")
