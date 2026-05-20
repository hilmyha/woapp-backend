from sqlalchemy import Column, Integer, String
from app.db.db import Base

# define workout model
class WorkoutModel(Base):
    __tablename__ = "workouts"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    reps = Column(Integer)