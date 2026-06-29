from fastapi import HTTPException

from sqlalchemy.orm import Session
from app.modules.users.user_model import UserModel
from app.modules.workouts.workout_model import WorkoutModel

from app.core.guards.owned_workout import get_owned_workout

from app.modules.workouts.workout_schema import WorkoutCreate, WorkoutUpdate

def create_workout(workout: WorkoutCreate, user: UserModel, db: Session):
  payload = WorkoutModel(**workout.model_dump(), user_id=user.id)

  db.add(payload)
  db.commit()
  db.refresh(payload)

  return payload

def find_all_workout(user: UserModel, db: Session):
  workouts = db.query(WorkoutModel).filter(WorkoutModel.user_id == user.id).all()

  if not workouts:
    raise HTTPException(status_code=404, detail="No workouts found")

  return workouts

def find_one_workout(id: int, user: UserModel, db: Session):
  workout = get_owned_workout(id, user, db)
  
  if not workout:
    raise HTTPException(status_code=404, detail=f"Workout with ID {id} not found")
  
  return workout

def update_workout( id: int, workout: WorkoutUpdate, user: UserModel, db: Session):
  data = find_one_workout(id, user, db)

  payload = workout.model_dump(exclude_unset=True)

  for key, value in payload.items():
    if value is not None:
      setattr(data, key, value)

  db.commit()
  db.refresh(data)

  return data

def delete_workout(id: int, user: UserModel, db: Session):
  data = find_one_workout(id, user, db) 
  
  db.delete(data)
  db.commit()

  return {"detail": f"Workout with ID {id} has been deleted."}