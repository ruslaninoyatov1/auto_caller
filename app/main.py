from fastapi import FastAPI
from app.api import router

app = FastAPI(
    title="Auto Caller API",
    version="1.0.0",
)

app.include_router(router, prefix="/api/v1")
