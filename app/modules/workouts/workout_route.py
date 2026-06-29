from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session
from app.db.db import get_db

from app.dependencies.auth import CurrentUser

from app.modules.workouts.workout_schema import WorkoutCreate, WorkoutUpdate, WorkoutResponse
from app.modules.workouts.workout_service import create_workout, find_all_workout, find_one_workout, update_workout, delete_workout

router = APIRouter(prefix="/workouts", tags=["workouts"])

@router.post("/", response_model=WorkoutResponse)
async def create(workout: WorkoutCreate, user: CurrentUser, db: Session = Depends(get_db)):
  return create_workout(workout, user, db)

@router.get("/", response_model=list[WorkoutResponse])
async def find_all(user: CurrentUser,db: Session = Depends(get_db)):
  return find_all_workout(user, db)

@router.get("/{id}", response_model=WorkoutResponse)
async def find_one(id: int, user: CurrentUser, db: Session = Depends(get_db)):
  return find_one_workout(id, user, db)

@router.patch("/{id}", response_model=WorkoutResponse)
async def update(id: int, workout: WorkoutUpdate, user: CurrentUser, db: Session = Depends(get_db)):
  return update_workout(id, workout, user, db)

@router.delete("/{id}", response_model=dict)
async def delete(id: int, user: CurrentUser, db: Session = Depends(get_db)):
  return delete_workout(id, user, db)