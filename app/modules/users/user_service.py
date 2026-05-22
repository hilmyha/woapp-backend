from fastapi import HTTPException

from app.modules.users.user_schema import UserCreate, UserUpdate

def add_user(user: UserCreate):
  return {"id": 1, **user.dict()}

def get_users():
  return [{"id": 1, "name": "John Doe"}]

def get_user(id: int):
  if id != 1:
    raise HTTPException(status_code=404, detail=f"User with ID {id} not found")
  
  return {"id": 1, "name": "John Doe"}

def update_user(id: int, user: UserUpdate):
  get_user(id) 
  
  updated_user = {"id": 1, "name": user.name or "John Doe"}
  return updated_user

def delete_user(id: int):
  get_user(id) 
  
  return f"User with ID {id} has been deleted."