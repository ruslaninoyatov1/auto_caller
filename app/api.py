from fastapi import APIRouter
from typing import List
from app.schemas import ClientData
import datetime

router = APIRouter()

@router.post("/call-debtors")
async def call_debtors(clients: List[ClientData]):
    # Hozircha log qilamiz, keyinchalik bazaga yoki queuega yuboramiz
    for client in clients:
        print(f"[{datetime.datetime.now()}] Kelgan: {client.client_name}, {client.phone_number}, qarz: {client.debt}")
    
    return {
        "status": "success",
        "calls_scheduled": len(clients)
    }
