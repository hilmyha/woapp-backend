from fastapi import HTTPException

from sqlalchemy.orm import Session
from app.modules.users.user_model import UserModel

from app.modules.users.user_schema import UserCreate, UserUpdate

def add_user(db: Session, user: UserCreate):
  data = UserModel(**user.dict())

  db.add(data)
  db.commit()
  db.refresh(data)
  
  return data

def get_users(db: Session):
  if db.query(UserModel).count() == 0:
    raise HTTPException(status_code=404, detail="No users found")

  return db.query(UserModel).all()

def get_user(db: Session, id: int):
  user = db.query(UserModel).filter(UserModel.id == id).first()
  
  if not user:
    raise HTTPException(status_code=404, detail=f"User with ID {id} not found")
  
  return user

def update_user(db: Session, id: int, user: UserUpdate):
  data = get_user(db, id)

  for key, value in user.dict().items():
    if value is not None:
      setattr(data, key, value)

  db.commit()
  db.refresh(data)

  return data

def delete_user(db: Session, id: int):
  data = get_user(db, id) 
  
  db.delete(data)
  db.commit()

  return {"detail": f"User with ID {id} has been deleted."}