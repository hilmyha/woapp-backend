from pydantic import BaseModel

class Workout(BaseModel):
    name: str
    reps: int

class WorkoutCreate(Workout):
    pass

class WorkoutUpdate(BaseModel):
    name: str | None = None
    reps: int | None = None

class WorkoutResponse(Workout):
    id: int

    # allow population by attribute name (e.g. from ORM objects)
    model_config = {
        "from_attributes": True
    }