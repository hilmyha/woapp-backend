from fastapi import Request
from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

from app.core.jwt import decode_access_token

from sqlalchemy.orm import Session
from app.db.db import get_db

from app.modules.users.user_model import UserModel

auth_scheme = HTTPBearer()

def get_current_user(
    request: Request,
    token: HTTPAuthorizationCredentials = Depends(auth_scheme),
    db: Session = Depends(get_db)
):
    payload = decode_access_token(token.credentials)

    if not payload or "user_id" not in payload:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials"
        )

    user = db.get(UserModel, payload["user_id"])

    if not user:
        raise HTTPException(
            status_code=401,
            detail="User not found"
        )

    request.state.user = user
    return user