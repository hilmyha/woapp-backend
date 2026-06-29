from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.modules.workouts.workout_model import WorkoutModel
from app.modules.users.user_model import UserModel

def get_owned_workout( workout_id: int, user: UserModel, db: Session):
    workout = (
        db.query(WorkoutModel)
        .filter(
            WorkoutModel.id == workout_id,
            WorkoutModel.user_id == user.id
        )
        .first()
    )

    if not workout:
        raise HTTPException(status_code=404, detail="Workout not found")

    return workout