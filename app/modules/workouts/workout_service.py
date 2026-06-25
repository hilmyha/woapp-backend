from fastapi import HTTPException

from sqlalchemy.orm import Session
from app.modules.users.user_model import UserModel
from app.modules.workouts.workout_model import WorkoutModel

from app.modules.workouts.workout_schema import WorkoutCreate, WorkoutUpdate

def add_workout(db: Session, user: UserModel, workout: WorkoutCreate):
  payload = WorkoutModel(**workout.model_dump(), user_id=user.id)

  db.add(payload)
  db.commit()
  db.refresh(payload)

  return payload

def get_workouts(db: Session, user: UserModel):
  workouts = db.query(WorkoutModel).filter(WorkoutModel.user_id == user.id).all()

  if not workouts:
    raise HTTPException(status_code=404, detail="No workouts found")

  return workouts

def get_workout(db: Session, user: UserModel, id: int):
  workout = db.query(WorkoutModel).filter(WorkoutModel.id == id, WorkoutModel.user_id == user.id).first()
  
  if not workout:
    raise HTTPException(status_code=404, detail=f"Workout with ID {id} not found")
  
  return workout

def update_workout(db: Session, id: int, user: UserModel, workout: WorkoutUpdate):
  data = get_workout(db, user, id)

  payload = workout.model_dump(exclude_unset=True)

  for key, value in payload.items():
    if value is not None:
      setattr(data, key, value)

  db.commit()
  db.refresh(data)

  return data

def delete_workout(db: Session, user: UserModel, id: int):
  data = get_workout(db, user, id) 
  
  db.delete(data)
  db.commit()

  return {"detail": f"Workout with ID {id} has been deleted."}