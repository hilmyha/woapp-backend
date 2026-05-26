from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session
from app.db.db import get_db

from app.modules.users.user_schema import UserCreate, UserUpdate, UserResponse
from app.modules.users.user_service import add_user, get_users, get_user, update_user, delete_user

router = APIRouter(prefix="/users", tags=["users"])

@router.post("/", response_model=UserResponse)
async def create_user(user: UserCreate, db: Session = Depends(get_db)):
  return add_user(db, user)

@router.get("/", response_model=list[UserResponse])
async def get_all_users(db: Session = Depends(get_db)):
  return get_users(db)

@router.get("/{id}", response_model=UserResponse)
async def get_user_by_id(id: int, db: Session = Depends(get_db)):
  return get_user(db, id)

@router.patch("/{id}", response_model=UserResponse)
async def update_user_by_id(id: int, user: UserUpdate, db: Session = Depends(get_db)):
  return update_user(db, id, user)

@router.delete("/{id}", response_model=str)
async def delete_user_by_id(id: int, db: Session = Depends(get_db)):
  return delete_user(db, id)