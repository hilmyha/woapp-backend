from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.db.db import Base

class WorkoutExerciseModel(Base):
  __tablename__ = "workout_exercises"

  id = Column(Integer, primary_key=True, index=True)
  exercise_id = Column(Integer, ForeignKey("exercises.id"))
  workout_id = Column(Integer, ForeignKey("workouts.id"))
  
  workout = relationship("WorkoutModel", back_populates="exercises")
  exercise = relationship("ExerciseModel", back_populates="workouts")
  sets = relationship("WorkoutSetModel", back_populates="workout_exercise", cascade="all, delete-orphan")