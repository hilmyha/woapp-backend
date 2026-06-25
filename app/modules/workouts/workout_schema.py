from pydantic import BaseModel

class Workout(BaseModel):
    name: str

class WorkoutCreate(Workout):
    pass

class WorkoutUpdate(BaseModel):
    name: str | None = None
    date: str | None = None

class WorkoutResponse(Workout):
    id: int

    # allow population by attribute name (e.g. from ORM objects)
    model_config = {
        "from_attributes": True
    }