from fastapi import HTTPException

from sqlalchemy.orm import Session
from app.core.hashing import verify_password
from app.modules.users.user_model import UserModel

from app.modules.auths.auth_schema import UserLogin, UserRegister
from app.core.hashing import hash_password, verify_password
from app.core.jwt import create_access_token

def register_user(db: Session, user: UserRegister):
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

def login_user(db: Session, form_data: UserLogin):
  user_data = db.query(UserModel).filter(UserModel.email == form_data.email).first()
  
  if not user_data or not verify_password(form_data.password, str(user_data.password)):
    raise HTTPException(status_code=401, detail="Invalid email or password")

  token = create_access_token({"sub": user_data.email, "user_id": user_data.id, "name": user_data.name})

  return {"access_token": token, "token_type": "bearer", "user": user_data}