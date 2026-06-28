from pydantic import BaseModel

from app.modules.exercises.exercise_schema import ExerciseResponse
from app.modules.workout_sets.workout_set_schema import SetResponse

class WorkoutExercise(BaseModel):
  workout_id: int
  exercise_id: int

class CreateWorkoutExercise(WorkoutExercise):
  pass

class UpdateWorkoutExercise(WorkoutExercise):
  pass

class WorkoutExerciseResponse(WorkoutExercise):
  id: int
  exercise: ExerciseResponse
  sets: list[SetResponse]

  model_config = {
    "from_attributes": True
  }