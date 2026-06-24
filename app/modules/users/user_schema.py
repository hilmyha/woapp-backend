from pydantic import BaseModel, EmailStr

class User(BaseModel):
    name: str
    email: EmailStr
    password: str

class UserCreate(User):
    pass

class UserUpdate(BaseModel):
    name: str | None = None
    email: EmailStr | None = None
    password: str | None = None

class UserResponse(User):
    id: int

    # allow population by attribute name (e.g. from ORM objects)
    model_config = {
        "from_attributes": True
    }