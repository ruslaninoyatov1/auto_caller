from fastapi import Header, HTTPException, status
from config import API_KEY, API_KEY_NAME

def verify_api_key(x_api_key: str = Header(...)):
    if x_api_key != API_KEY:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="API key is invalid"
        )
