from fastapi import APIRouter, HTTPException

from app.services import convert_currency

router = APIRouter()


@router.get("/convert")
async def convert(from_currency: str, to_currency: str, amount: float):
    try:
        # Return the service response directly instead of wrapping it
        return await convert_currency(from_currency, to_currency, amount)

    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

    except ConnectionError as ce:
        raise HTTPException(status_code=400, detail=str(ce))
