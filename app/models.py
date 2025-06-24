from sqlalchemy import Column, Integer, String, Float, DateTime
from database import Base
from datetime import datetime

class CallLog(Base):
    __tablename__ = "call_logs"
    id = Column(Integer, primary_key=True, index=True)
    client_name = Column(String)
    phone_number = Column(String)
    contract_object = Column(String)
    debt = Column(Float)
    due_date = Column(String)
    status = Column(String, default="pending")
    created_at = Column(DateTime, default=datetime.utcnow)
