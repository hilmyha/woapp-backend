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