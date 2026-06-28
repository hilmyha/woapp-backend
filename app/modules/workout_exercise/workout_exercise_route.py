from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session
from app.db.db import get_db

from app.dependencies.auth import CurrentUser

from app.modules.workout_exercise.workout_exercise_schema import  CreateWorkoutExercise, WorkoutExerciseResponse
from app.modules.workout_exercise.workout_exercise_service import add_exercise_to_workout, get_workout_exercises, get_workout_exercise, update_workout_exercise, remove_exercise_from_workout

router = APIRouter(prefix="/workouts/{workout_id}/exercises", tags=["workout_exercises"])


@router.get("/", response_model=list[WorkoutExerciseResponse])
async def get_all_workout_exercises(workout_id: int, user: CurrentUser, db: Session = Depends(get_db)):
  return get_workout_exercises(db, user, workout_id)

@router.post("/", response_model=WorkoutExerciseResponse)
async def create_exercise_to_workout(workout_id: int, exercise: CreateWorkoutExercise, user: CurrentUser, db: Session = Depends(get_db)):
  print(exercise)
  return add_exercise_to_workout(workout_id, exercise, user, db)

@router.get("/{id}", response_model=WorkoutExerciseResponse)
async def get_workout_exercise_by_id(id: int, user: CurrentUser, workout_id: int, db: Session = Depends(get_db)):
  return get_workout_exercise(db, workout_id, user, id)

@router.patch("/{id}", response_model=WorkoutExerciseResponse)
async def update_workout_exercise_by_id(id: int, exercise: CreateWorkoutExercise, user: CurrentUser, workout_id: int, db: Session = Depends(get_db)):
  return update_workout_exercise(db, workout_id, user, id, exercise)

@router.delete("/{id}", response_model=str)
async def delete_exercise_from_workout(id: int, workout_id: int, user: CurrentUser, db: Session = Depends(get_db)):
  return remove_exercise_from_workout(db, workout_id, user, id)