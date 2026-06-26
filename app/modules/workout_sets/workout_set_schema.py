from pydantic import BaseModel

class Set(BaseModel):
  reps: int
  weight: float

class SetCreate(Set):
  pass

class SetUpdate(BaseModel):
  reps: int
  weight: float

class SetResponse(Set):
  id: int

  # allow population by attribute name (e.g. from ORM objects)
  model_config = {
      "from_attributes": True
  }