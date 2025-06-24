from pydantic import BaseModel
from datetime import date

class ClientData(BaseModel):
    client_name: str
    phone_number: str
    contract_object: str
    debt: float
    due_date: date
