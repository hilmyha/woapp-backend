from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from app.db.db import Base

class WorkoutSetModel(Base):
  __tablename__ = "workout_sets"

  id = Column(Integer, primary_key=True, index=True)
  reps = Column(Integer)
  weight = Column(Integer)
  workout_exercise_id = Column(Integer, ForeignKey("workout_exercises.id"))
  
  workout_exercise = relationship("WorkoutExerciseModel", back_populates="sets")