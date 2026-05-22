from pydantic import BaseModel

class User(BaseModel):
    name: str

class UserCreate(User):
    pass

class UserUpdate(BaseModel):
    name: str | None = None

class UserResponse(User):
    id: int

    # allow population by attribute name (e.g. from ORM objects)
    model_config = {
        "from_attributes": True
    }