from pydantic import BaseModel
from typing import List

class ClientData(BaseModel):
    client_name: str
    phone_number: str
    contract_object: str
    debt: float
    due_date: str
