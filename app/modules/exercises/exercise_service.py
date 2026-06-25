from fastapi import HTTPException

from sqlalchemy.orm import Session
from app.modules.exercises.exercise_model import CategoryModel, ExerciseModel

from app.modules.exercises.exercise_schema import ExerciseCreate, ExerciseUpdate

def get_categories(db: Session):
  categories = db.query(CategoryModel).all()

  if not categories:
    raise HTTPException(status_code=404, detail="No categories found")

  return categories

def get_category(db: Session, id: int):
  category = db.query(CategoryModel).filter(CategoryModel.id == id).first()
  
  if not category:
    raise HTTPException(status_code=404, detail=f"Category with ID {id} not found")
  
  return category

def get_exercises(db: Session, category_id: int | None = None, search: str | None = None):
  exercises = db.query(ExerciseModel)

  if category_id:
    exercises = exercises.filter(ExerciseModel.category_id == category_id)

  if search:
    exercises = exercises.filter(ExerciseModel.name.contains(search))

  if not exercises:
    raise HTTPException(status_code=404, detail="No exercises found")

  return exercises.all()

def get_exercise(db: Session, id: int):
  exercise = db.query(ExerciseModel).filter(ExerciseModel.id == id).first()
  
  if not exercise:
    raise HTTPException(status_code=404, detail=f"Exercise with ID {id} not found")
  
  return exercise