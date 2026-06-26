from fastapi import HTTPException

from sqlalchemy.orm import Session
from app.modules.workout_sets.workout_set_model import WorkoutSetModel

from app.modules.workout_sets.workout_set_schema import SetCreate

def add_set_to_exercise(db: Session, workout_exercise_id: int, set: SetCreate):
  payload = WorkoutSetModel(
      **set.model_dump(),
      workout_exercise_id=workout_exercise_id,
  )

  db.add(payload)
  db.commit()
  db.refresh(payload)

  return payload

def get_sets_per_exercise(db: Session, workout_exercise_id: int):
  sets = db.query(WorkoutSetModel).filter(WorkoutSetModel.workout_exercise_id == workout_exercise_id).all()

  if not sets:
    raise HTTPException(status_code=404, detail="No sets found")

  return sets