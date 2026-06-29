from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session
from app.db.db import get_db

from app.modules.users.user_schema import UserCreate, UserUpdate, UserResponse
from app.modules.users.user_service import create_user, find_all_user, find_one_user, update_user, delete_user

router = APIRouter(prefix="/users", tags=["users"])

@router.post("/", response_model=UserResponse)
async def create(user: UserCreate, db: Session = Depends(get_db)):
  return create_user(user, db)

@router.get("/", response_model=list[UserResponse])
async def find_all(db: Session = Depends(get_db)):
  return find_all_user(db)

@router.get("/{id}", response_model=UserResponse)
async def find_one(id: int, db: Session = Depends(get_db)):
  return find_one_user(id, db)

@router.patch("/{id}", response_model=UserResponse)
async def update(id: int, user: UserUpdate, db: Session = Depends(get_db)):
  return update_user(id, user, db)

@router.delete("/{id}", response_model=dict)
async def delete(id: int, db: Session = Depends(get_db)):
  return delete_user(id, db)