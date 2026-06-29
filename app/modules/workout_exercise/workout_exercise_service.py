from fastapi import HTTPException

from sqlalchemy.orm import Session

from app.modules.users.user_model import UserModel

from app.modules.workout_exercise.workout_exercise_schema import CreateWorkoutExercise
from app.modules.workout_exercise.workout_exercise_model import WorkoutExerciseModel

from app.core.guards.owned_workout import get_owned_workout

def create_workout_exercise(workout_id: int, exercise: CreateWorkoutExercise, user: UserModel, db: Session):
  workout = get_owned_workout(workout_id, user, db)

  exist = db.query(WorkoutExerciseModel).filter(WorkoutExerciseModel.workout_id == workout.id, WorkoutExerciseModel.exercise_id == exercise.exercise_id).first()

  if exist:
      raise HTTPException(status_code=400, detail="Already exists")

  payload = WorkoutExerciseModel(**exercise.model_dump())

  db.add(payload)
  db.commit()
  db.refresh(payload)

  return payload

def find_all_workout_exercise(workout_id: int, user: UserModel, db: Session):
  workout = get_owned_workout(workout_id, user, db)

  exercise = db.query(WorkoutExerciseModel).filter(WorkoutExerciseModel.workout_id == workout.id).all()

  if not exercise:
    raise HTTPException(status_code=404, detail=f"Workout exercise with ID {id} not found")

  return exercise

def find_one_workout_exercise(id: int, workout_id: int, user: UserModel, db: Session):
  workout = get_owned_workout(workout_id, user, db)

  exercise = db.query(WorkoutExerciseModel).filter(WorkoutExerciseModel.workout_id == workout.id, WorkoutExerciseModel.id == id).first()

  if not exercise:
    raise HTTPException(status_code=404, detail=f"Workout exercise with ID {id} not found")

  return exercise

def update_workout_exercise(id: int, workout_id: int, user: UserModel, exercise: CreateWorkoutExercise, db: Session):
  data = find_one_workout_exercise(id, workout_id, user, db)

  payload = exercise.model_dump(exclude_unset=True)

  for key, value in payload.items():
    if value is not None:
      setattr(data, key, value)

  db.commit()
  db.refresh(data)

  return data

def delete_workout_exercise(id: int, workout_id: int, user: UserModel, db: Session):
  data = find_one_workout_exercise(id, workout_id, user, db)

  if not data:
    raise HTTPException(status_code=404, detail=f"Workout exercise with ID {id} not found")

  db.delete(data)
  db.commit()

  return {"detail": f"Workout exercise with ID {id} has been deleted."}