from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session
from app.db.db import get_db

from app.dependencies.auth import CurrentUser

from app.modules.workout_exercise.workout_exercise_schema import  CreateWorkoutExercise, WorkoutExerciseResponse
from app.modules.workout_exercise.workout_exercise_service import create_workout_exercise, find_all_workout_exercise, find_one_workout_exercise, update_workout_exercise, delete_workout_exercise

router = APIRouter(prefix="/workouts/{workout_id}/exercises", tags=["workout_exercises"])

@router.post("/", response_model=WorkoutExerciseResponse)
async def create(workout_id: int, exercise: CreateWorkoutExercise, user: CurrentUser, db: Session = Depends(get_db)):
  print(exercise)
  return create_workout_exercise(workout_id, exercise, user, db)

@router.get("/", response_model=list[WorkoutExerciseResponse])
async def find_all(workout_id: int, user: CurrentUser, db: Session = Depends(get_db)):
  return find_all_workout_exercise(workout_id, user, db)

@router.get("/{id}", response_model=WorkoutExerciseResponse)
async def find_one(id: int, user: CurrentUser, workout_id: int, db: Session = Depends(get_db)):
  return find_one_workout_exercise(id, workout_id, user, db)

@router.patch("/{id}", response_model=WorkoutExerciseResponse)
async def update(id: int, exercise: CreateWorkoutExercise, user: CurrentUser, workout_id: int, db: Session = Depends(get_db)):
  return update_workout_exercise(id, workout_id, user, exercise, db)

@router.delete("/{id}", response_model=dict)
async def delete(id: int, workout_id: int, user: CurrentUser, db: Session = Depends(get_db)):
  return delete_workout_exercise(id, workout_id, user, db)