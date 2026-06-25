from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.db.db import Base

# deefine category model
class CategoryModel(Base):
  __tablename__ = "categories"

  id = Column(Integer, primary_key=True, index=True)
  name = Column(String, unique=True)

  exercises = relationship("ExerciseModel", back_populates="category", cascade="all, delete-orphan")

# define exercise model
class ExerciseModel(Base):
  __tablename__ = "exercises"

  id = Column(Integer, primary_key=True, index=True)
  name = Column(String, unique=True)
  category_id = Column(Integer, ForeignKey("categories.id"))

  category = relationship("CategoryModel", back_populates="exercises")