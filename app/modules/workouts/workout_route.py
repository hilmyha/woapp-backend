from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session
from app.db.db import get_db

from app.modules.workouts.workout_schema import WorkoutCreate, WorkoutUpdate, WorkoutResponse
from app.modules.workouts.workout_service import add_workout, get_workouts, get_workout, update_workout, delete_workout

router = APIRouter(prefix="/workouts", tags=["workouts"])

@router.post("/", response_model=WorkoutResponse)
async def create_workout(workout: WorkoutCreate, db: Session = Depends(get_db)):
  return add_workout(db, workout)

@router.get("/", response_model=list[WorkoutResponse])
async def get_all_workouts(db: Session = Depends(get_db)):
  return get_workouts(db)

@router.get("/{id}", response_model=WorkoutResponse)
async def get_workout_by_id(id: int, db: Session = Depends(get_db)):
  return get_workout(db, id)

@router.patch("/{id}", response_model=WorkoutResponse)
async def update_workout_by_id(id: int, workout: WorkoutUpdate, db: Session = Depends(get_db)):
  return update_workout(db, id, workout)

@router.delete("/{id}", response_model=WorkoutResponse)
async def delete_workout_by_id(id: int, db: Session = Depends(get_db)):
  return delete_workout(db, id)