from fastapi import HTTPException

from app.modules.workouts.workout_schema import WorkoutCreate, WorkoutUpdate

def add_workout(workout: WorkoutCreate):
  return "A new workout will be created here."

def get_workouts():
  return "List of workouts will be returned here."

def get_workout(id: int):
  if id < 0:
    raise HTTPException(status_code=404, detail="Workout not found")
  return f"Details of workout with ID {id} will be returned here."

def update_workout(id: int, workout: WorkoutUpdate):
  get_workout(id)
  return f"Workout with ID {id} will be updated here."

def delete_workout(id: int):
  get_workout(id)
  return f"Workout with ID {id} will be deleted here."