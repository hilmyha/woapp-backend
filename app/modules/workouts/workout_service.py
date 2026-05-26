from fastapi import HTTPException

from sqlalchemy.orm import Session
from app.modules.workouts.workout_model import WorkoutModel

from app.modules.workouts.workout_schema import WorkoutCreate, WorkoutUpdate

def add_workout(db: Session, workout: WorkoutCreate):
  data = WorkoutModel(**workout.dict())

  db.add(data)
  db.commit()
  db.refresh(data)
  
  return data

def get_workouts(db: Session):
  if db.query(WorkoutModel).count() == 0:
    raise HTTPException(status_code=404, detail="No workouts found")

  return db.query(WorkoutModel).all()

def get_workout(db: Session, id: int):
  data = db.query(WorkoutModel).filter(WorkoutModel.id == id).first()
  
  if data is None:
    raise HTTPException(status_code=404, detail=f"Workout with ID {id} not found")
  
  return data

def update_workout(db: Session, id: int, workout: WorkoutUpdate):
  data = get_workout(db, id)
  
  for key, value in workout.dict(exclude_unset=True).items():
    setattr(data, key, value)
  db.commit()
  db.refresh(data)
  
  return data

def delete_workout(db: Session, id: int):
  data = get_workout(db, id)
  
  db.delete(data)
  db.commit()
  
  return {"detail": f"Workout with ID {id} has been deleted."}