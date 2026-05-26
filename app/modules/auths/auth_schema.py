from pydantic import BaseModel

class UserLogin(BaseModel):
    email: str
    password: str

class UserRegister(UserLogin):
    name: str

class UserResponse(UserLogin):
    id: int
    name: str
    email: str

    # allow population by attribute name (e.g. from ORM objects)
    model_config = {
        "from_attributes": True
    }