from pydantic import BaseModel

class WorkoutExercise(BaseModel):
  exercise_id: int
  workout_id: int

class ExerciseMini(BaseModel):
    id: int
    name: str

    model_config = {
        "from_attributes": True
    }

class WorkoutExerciseResponse(WorkoutExercise):
  id: int
  exercise: ExerciseMini

  model_config = {
    "from_attributes": True
  }