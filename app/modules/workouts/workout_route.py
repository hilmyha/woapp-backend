from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session
from app.db.db import get_db

from app.dependencies.auth import CurrentUser

from app.modules.workouts.workout_schema import WorkoutCreate, WorkoutUpdate, WorkoutResponse
from app.modules.workouts.workout_service import get_workouts, get_workout, add_workout, update_workout, delete_workout

router = APIRouter(prefix="/workouts", tags=["workouts"])

@router.post("/", response_model=WorkoutResponse)
async def create_workout(workout: WorkoutCreate, user: CurrentUser, db: Session = Depends(get_db)):
  return add_workout(db, user, workout)

@router.get("/", response_model=list[WorkoutResponse])
async def get_all_workouts(user: CurrentUser,db: Session = Depends(get_db)):
  return get_workouts(db, user)

@router.get("/{id}", response_model=WorkoutResponse)
async def get_workout_by_id(id: int, user: CurrentUser, db: Session = Depends(get_db)):
  return get_workout(db, user, id)

@router.put("/{id}", response_model=WorkoutResponse)
async def update_workout_by_id(id: int, workout: WorkoutUpdate, user: CurrentUser, db: Session = Depends(get_db)):
  return update_workout(db, id, user, workout)

@router.delete("/{id}", response_model=str)
async def delete_workout_by_id(id: int, user: CurrentUser, db: Session = Depends(get_db)):
  return delete_workout(db, user, id)