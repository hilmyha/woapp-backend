from fastapi import APIRouter

from app.modules.users.user_schema import UserCreate, UserUpdate, UserResponse
from app.modules.users.user_service import add_user, get_users, get_user, update_user, delete_user

router = APIRouter(prefix="/users", tags=["users"])

@router.post("/", response_model=UserResponse)
async def create_user(user: UserCreate):
  return add_user(user)

@router.get("/", response_model=list[UserResponse])
async def get_all_users():
  return get_users()

@router.get("/{id}", response_model=UserResponse)
async def get_user_by_id(id: int):
  return get_user(id)

@router.patch("/{id}", response_model=UserResponse)
async def update_user_by_id(id: int, user: UserUpdate):
  return update_user(id, user)

@router.delete("/{id}", response_model=str)
async def delete_user_by_id(id: int):
  return delete_user(id)