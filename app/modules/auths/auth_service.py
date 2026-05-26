from fastapi import HTTPException

from app.modules.auths.auth_schema import UserLogin, UserRegister

def register_user(user: UserRegister):
  # Here you would typically add logic to save the user to the database
  # For demonstration, we will just return the user data
  return {"message": "User registered successfully", "user": user}

def login_user(user: UserLogin):
  # Here you would typically add logic to verify the user's credentials
  # For demonstration, we will just return the user data
  return {"message": "User logged in successfully", "user": user}