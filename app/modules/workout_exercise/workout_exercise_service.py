from fastapi import HTTPException

from sqlalchemy.orm import Session
from app.modules.users.user_model import UserModel
from app.modules.workout_exercise.workout_exercise_model import WorkoutExerciseModel

def add_exercise_to_workout(workout_id: int, exercise_id: int, user: UserModel, db: Session):
  exist = db.query(WorkoutExerciseModel).filter(
      WorkoutExerciseModel.workout_id == workout_id,
      WorkoutExerciseModel.exercise_id == exercise_id
  ).first()

  if exist:
      raise HTTPException(status_code=400, detail="Already exists")

  payload = WorkoutExerciseModel(
      workout_id=workout_id,
      exercise_id=exercise_id,
      user_id=user.id
  )

  db.add(payload)
  db.commit()
  db.refresh(payload)

  return payload

def get_workout_exercises(db: Session, user: UserModel, id: int):
  exercise = db.query(WorkoutExerciseModel).filter(WorkoutExerciseModel.workout_id == id, WorkoutExerciseModel.workout.user_id == user.id).all()

  if not exercise:
    raise HTTPException(status_code=404, detail=f"Workout exercise with ID {id} not found")

  return exercise

def remove_exercise_from_workout(db: Session, workout_id: int, user: UserModel, id: int):
  data = db.query(WorkoutExerciseModel).filter(WorkoutExerciseModel.workout_id == workout_id, WorkoutExerciseModel.id == id, WorkoutExerciseModel.workout.user_id == user.id).first()
  
  if not data:
    raise HTTPException(status_code=404, detail=f"Workout exercise with ID {id} not found")
  
  db.delete(data)
  db.commit()

  return {"detail": f"Workout exercise with ID {id} has been deleted."}