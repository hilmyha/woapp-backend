from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from app.db.db import Base

class WorkoutModel(Base):
  __tablename__ = "workouts"

  id = Column(Integer, primary_key=True, index=True)
  name = Column(String)
  date = Column(DateTime, default=datetime.now())
  user_id = Column(Integer, ForeignKey("users.id"))

  user = relationship("UserModel", back_populates="workouts")