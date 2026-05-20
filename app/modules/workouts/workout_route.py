from fastapi import APIRouter

from app.modules.workouts.workout_schema import WorkoutCreate, WorkoutUpdate, WorkoutResponse
from app.modules.workouts.workout_service import add_workout, get_workouts, get_workout, update_workout, delete_workout

router = APIRouter(prefix="/workouts", tags=["workouts"])

@router.post("/")
async def create_workout(workout: WorkoutCreate):
  return add_workout(workout)

@router.get("/")
async def get_all_workouts():
  return get_workouts()

@router.get("/{id}")
async def get_workout_by_id(id: int):
  return get_workout(id)

@router.patch("/{id}")
async def update_workout_by_id(id: int, workout: WorkoutUpdate):
  return update_workout(id, workout)

@router.delete("/{id}")
async def delete_workout_by_id(id: int):
  return delete_workout(id)