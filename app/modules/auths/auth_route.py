from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session
from app.db.db import get_db

from app.modules.auths.auth_schema import UserLogin, UserRegister, UserResponse, TokenResponse
from app.modules.auths.auth_service import register_user, login_user

from app.middleware.auth import get_current_user

router = APIRouter(prefix="/auth", tags=["auth"])

@router.post("/register", response_model=UserResponse)
async def register(user: UserRegister, db: Session = Depends(get_db)):
  return register_user(db, user)

@router.post("/login", response_model=TokenResponse)
async def login(user: UserLogin, db: Session = Depends(get_db)):
  return login_user(db, user)

@router.get("/me", response_model=UserResponse)
async def me(user = Depends(get_current_user)):
  return user