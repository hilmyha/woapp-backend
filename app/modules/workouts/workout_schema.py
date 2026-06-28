from datetime import datetime
from pydantic import BaseModel

from app.modules.workout_exercise.workout_exercise_schema import WorkoutExerciseResponse

class Workout(BaseModel):
    name: str

class WorkoutCreate(Workout):
    pass

class WorkoutUpdate(BaseModel):
    name: str | None = None
    date: datetime | None = None

class WorkoutResponse(Workout):
    id: int
    date: datetime
    exercises: list[WorkoutExerciseResponse]

    # allow population by attribute name (e.g. from ORM objects)
    model_config = {
        "from_attributes": True
    }