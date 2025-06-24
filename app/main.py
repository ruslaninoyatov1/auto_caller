from fastapi import FastAPI, Depends, HTTPException
from typing import List
from app.auth import verify_api_key
from app.schemas import ClientData
from app.models import CallLog
from app.database import Base, engine, get_db
from sqlalchemy.orm import Session

app = FastAPI()

Base.metadata.create_all(bind=engine)

@app.post("/api/v1/call-debtors", dependencies=[Depends(verify_api_key)])
def call_debtors(data: List[ClientData], db: Session = Depends(get_db)):
    for item in data:
        log = CallLog(
            client_name=item.client_name,
            phone_number=item.phone_number,
            contract_object=item.contract_object,
            debt=item.debt,
            due_date=item.due_date,
            status="pending"
        )
        db.add(log)
    db.commit()
    return {"message": "Call logs saved", "total": len(data)}

if __name__ == "__main__":
    import uvicorn
    import os
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run("app.main:app", host="0.0.0.0", port=port, reload=True)
