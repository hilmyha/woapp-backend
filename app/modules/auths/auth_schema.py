from pydantic import BaseModel, EmailStr

class UserBase(BaseModel):
    email: EmailStr
    password: str

class UserLogin(UserBase):
    pass

class UserRegister(UserBase):
    name: str

class UserResponse(UserBase):
    id: int

    # allow population by attribute name (e.g. from ORM objects)
    model_config = {
        "from_attributes": True
    }

class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"
    user: UserResponse