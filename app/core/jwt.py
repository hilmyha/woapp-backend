import os

from dotenv import load_dotenv
from datetime import datetime, timedelta, timezone
from jose import jwt, JWTError


load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES = 30

def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()

    expire = datetime.now(timezone.utc) + (expires_delta or timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))

    to_encode.update({"exp": expire})

    return jwt.encode(to_encode, SECRET_KEY or "", algorithm=ALGORITHM or "")

def decode_access_token(token: str):
    try:
        return jwt.decode(
            token,
            SECRET_KEY or "",
            algorithms=[ALGORITHM or ""]
        )
    except JWTError:
        return None