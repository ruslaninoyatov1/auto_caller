# routes/debtors.py

from fastapi import APIRouter, Depends
from typing import List
from auth import verify_api_key
from pydantic import BaseModel

router = APIRouter()

class ClientData(BaseModel):
    client_name: str
    phone_number: str
    contract_object: str
    debt: float
    due_date: str

@router.post("/api/v1/call-debtors", dependencies=[Depends(verify_api_key)])
async def call_debtors(data: List[ClientData]):
    # Ma'lumotlar bilan ishlovchi kod
    for item in data:
        print(f"Calling {item.client_name} on {item.phone_number}...")
        # Bu yerda qo‘ng‘iroq qilish logikasi bo‘ladi
    return {"message": "Calls scheduled", "total": len(data)}
