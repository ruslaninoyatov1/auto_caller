from fastapi import FastAPI
from routes import debtors

app = FastAPI()

app.include_router(debtors.router)
