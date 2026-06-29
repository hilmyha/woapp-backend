from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session
from app.db.db import get_db

from app.dependencies.auth import get_current_user

from app.modules.workout_sets.workout_set_schema import SetCreate, SetResponse
from app.modules.workout_sets.workout_set_service import create_set_exercise, find_all_set_exercise

router = APIRouter(prefix="/workouts-exercises/{workout_exercise_id}/sets", tags=["workout_sets"], dependencies=[Depends(get_current_user)])

@router.post("/", response_model=SetResponse)
async def create(workout_exercise_id: int, set: SetCreate, db: Session = Depends(get_db)):
  return create_set_exercise(workout_exercise_id, set, db)

@router.get("/", response_model=list[SetResponse])
async def find_all(workout_exercise_id: int, db: Session = Depends(get_db)):
  return find_all_set_exercise(workout_exercise_id, db)