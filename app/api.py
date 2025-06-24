from fastapi import APIRouter, HTTPException
from typing import List
from app.schemas import ClientData
from app.utils import log_call_request

router = APIRouter()

@router.post("/call-debtors")
async def call_debtors(clients: List[ClientData]):
    if not clients:
        raise HTTPException(status_code=400, detail="Bo'sh ro'yxat yuborildi.")

    for client in clients:
        log_call_request(client)
        print(f"[CALL LOG] {client.client_name} ga avtomatik ogohlantirish jo'natildi.")

    return {
        "status": "success",
        "calls_scheduled": len(clients)
    }
