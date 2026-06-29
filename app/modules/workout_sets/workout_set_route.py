from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session
from app.db.db import get_db

from app.dependencies.auth import get_current_user

from app.modules.workout_sets.workout_set_schema import SetCreate, SetResponse
from app.modules.workout_sets.workout_set_service import add_set_to_exercise, get_sets_per_exercise

router = APIRouter(prefix="/workouts-exercises/{workout_exercise_id}/sets", tags=["workout_sets"], dependencies=[Depends(get_current_user)])

@router.get("/", response_model=list[SetResponse])
async def get_sets(workout_exercise_id: int, db: Session = Depends(get_db)):
  return get_sets_per_exercise(db, workout_exercise_id)

@router.post("/", response_model=SetResponse)
async def create_set(workout_exercise_id: int, set: SetCreate, db: Session = Depends(get_db)):
  return add_set_to_exercise(db, workout_exercise_id ,set)