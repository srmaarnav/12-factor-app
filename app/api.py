from fastapi import APIRouter, HTTPException
from app.services import convert_currency

router = APIRouter()


@router.get("/convert")
async def convert(from_currency: str, to_currency: str, amount: float):
    try:
        result = await convert_currency(from_currency, to_currency, amount)
        return {"converted_amount": result}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
