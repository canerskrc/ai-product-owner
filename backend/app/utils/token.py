from jose import JWTError, jwt
from fastapi import HTTPException, Request, Depends
from datetime import datetime, timedelta

from app.core.config import settings

SECRET_KEY = "your-secret-key"  # Gerçekte .env'den alınmalı
ALGORITHM = "HS256"

def create_access_token(data: dict, expires_delta: timedelta = timedelta(hours=1)):
    to_encode = data.copy()
    expire = datetime.utcnow() + expires_delta
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def verify_token(token: str = Depends(lambda request: request.headers.get("Authorization").split(" ")[1])):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid or expired token")
