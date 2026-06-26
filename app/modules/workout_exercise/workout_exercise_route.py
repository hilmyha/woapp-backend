from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session
from app.db.db import get_db

from app.dependencies.auth import CurrentUser

from app.modules.workout_exercise.workout_exercise_schema import WorkoutExerciseResponse
from app.modules.workout_exercise.workout_exercise_service import add_exercise_to_workout, get_workout_exercises, remove_exercise_from_workout

router = APIRouter(prefix="/workouts/{workout_id}/exercises", tags=["workout_exercises"])

@router.get("/", response_model=list[WorkoutExerciseResponse])
async def get_all_workout_exercises(workout_id: int, user: CurrentUser, db: Session = Depends(get_db)):
  return get_workout_exercises(db, user, workout_id)

@router.post("/", response_model=WorkoutExerciseResponse)
async def create_exercise_to_workout(exercise_id: int, workout_id: int, user: CurrentUser, db: Session = Depends(get_db)):
  return add_exercise_to_workout(workout_id, exercise_id, user, db)

@router.delete("/{id}", response_model=str)
async def delete_exercise_from_workout(id: int, workout_id: int, user: CurrentUser, db: Session = Depends(get_db)):
  return remove_exercise_from_workout(db, workout_id, user, id)