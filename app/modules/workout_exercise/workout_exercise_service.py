from fastapi import HTTPException

from sqlalchemy.orm import Session

from app.modules.users.user_model import UserModel

from app.modules.workout_exercise.workout_exercise_schema import CreateWorkoutExercise
from app.modules.workout_exercise.workout_exercise_model import WorkoutExerciseModel

from app.core.guards.owned_workout import get_owned_workout

def add_exercise_to_workout(workout_id: int, exercise: CreateWorkoutExercise, user: UserModel, db: Session):
  workout = get_owned_workout(db, user, workout_id)

  exist = db.query(WorkoutExerciseModel).filter(WorkoutExerciseModel.workout_id == workout.id, WorkoutExerciseModel.exercise_id == exercise.exercise_id).first()

  if exist:
      raise HTTPException(status_code=400, detail="Already exists")

  payload = WorkoutExerciseModel(**exercise.model_dump())

  print(payload)

  db.add(payload)
  db.commit()
  db.refresh(payload)

  return payload

def get_workout_exercises(db: Session, user: UserModel, id: int):
  workout = get_owned_workout(db, user, id)

  exercise = db.query(WorkoutExerciseModel).filter(WorkoutExerciseModel.workout_id == workout.id).all()

  if not exercise:
    raise HTTPException(status_code=404, detail=f"Workout exercise with ID {id} not found")

  return exercise

def get_workout_exercise(db: Session, workout_id: int, user: UserModel, id: int):
  workout = get_owned_workout(db, user, workout_id)

  exercise = db.query(WorkoutExerciseModel).filter(WorkoutExerciseModel.workout_id == workout.id, WorkoutExerciseModel.id == id).first()

  if not exercise:
    raise HTTPException(status_code=404, detail=f"Workout exercise with ID {id} not found")

  return exercise

def update_workout_exercise(db: Session, workout_id: int, user: UserModel, id: int, exercise: CreateWorkoutExercise):
  data = get_workout_exercise(db, workout_id, user, id)

  payload = exercise.model_dump(exclude_unset=True)

  for key, value in payload.items():
    if value is not None:
      setattr(data, key, value)

  db.commit()
  db.refresh(data)

  return data

def remove_exercise_from_workout(db: Session, workout_id: int, user: UserModel, id: int):
  data = get_workout_exercise(db, workout_id, user, id)

  if not data:
    raise HTTPException(status_code=404, detail=f"Workout exercise with ID {id} not found")

  db.delete(data)
  db.commit()

  return {"detail": f"Workout exercise with ID {id} has been deleted."}