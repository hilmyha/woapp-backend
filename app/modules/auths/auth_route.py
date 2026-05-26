from fastapi import APIRouter, Depends

from app.modules.auths.auth_schema import UserLogin, UserRegister, UserResponse
from app.modules.auths.auth_service import register_user, login_user

router = APIRouter(prefix="/auth", tags=["auth"])

@router.post("/register")
async def register(user: UserRegister):
  return register_user(user)

@router.post("/login")
async def login(user: UserLogin):
  return login_user(user)