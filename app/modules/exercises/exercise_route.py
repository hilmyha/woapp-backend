from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session
from app.db.db import get_db

from app.modules.exercises.exercise_schema import ExerciseCreate, ExerciseUpdate, ExerciseResponse, CategoryResponse
from app.modules.exercises.exercise_service import get_exercises, get_exercise, get_categories, get_category

router = APIRouter(prefix="/exercises", tags=["exercises"])

@router.get("/categories", response_model=list[CategoryResponse])
async def get_all_categories(db: Session = Depends(get_db)):
  return get_categories(db)

@router.get("/categories/{id}", response_model=CategoryResponse)
async def get_category_by_id(id: int, db: Session = Depends(get_db)):
  return get_category(db, id)

@router.get("/", response_model=list[ExerciseResponse])
async def get_all_exercises(db: Session = Depends(get_db), category_id: int | None = None, search: str | None = None):
  return get_exercises(db, category_id=category_id, search=search)

@router.get("/{id}", response_model=ExerciseResponse)
async def get_exercise_by_id(id: int, db: Session = Depends(get_db)):
  return get_exercise(db, id)