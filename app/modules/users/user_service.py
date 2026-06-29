from fastapi import HTTPException

from sqlalchemy.orm import Session
from app.modules.users.user_model import UserModel

from app.modules.users.user_schema import UserCreate, UserUpdate
from app.core.hashing import hash_password

def create_user(user: UserCreate, db: Session):
  # hash the password before saving to the database
  payload = user.dict()

  payload["password"] = hash_password(
      user.password
  )

  data = UserModel(**payload)

  db.add(data)
  db.commit()
  db.refresh(data)
  
  return data

def find_all_user(db: Session):
  if db.query(UserModel).count() == 0:
    raise HTTPException(status_code=404, detail="No users found")

  return db.query(UserModel).all()

def find_one_user(id: int, db: Session):
  user = db.query(UserModel).filter(UserModel.id == id).first()
  
  if not user:
    raise HTTPException(status_code=404, detail=f"User with ID {id} not found")
  
  return user

def update_user(id: int, user: UserUpdate, db: Session):
  data = find_one_user(id, db)

  payload = user.dict(exclude_unset=True)

  if "password" in payload:
    payload["password"] = hash_password(payload["password"])

  for key, value in payload.items():
    if value is not None:
      setattr(data, key, value)

  db.commit()
  db.refresh(data)

  return data

def delete_user(id: int, db: Session):
  data = find_one_user(id, db) 
  
  db.delete(data)
  db.commit()

  return {"detail": f"User with ID {id} has been deleted."}