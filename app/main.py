import time

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.db.db import engine

from app.db.db import SessionLocal
from app.db.seed import seed_categories, seed_exercises

# Auth
from app.modules.auths.auth_route import router as auth_router

# User
from app.modules.users.user_route import router as user_router
from app.modules.users.user_model import UserModel

# Exercises
from app.modules.exercises.exercise_route import router as exercise_router
from app.modules.exercises.exercise_model import ExerciseModel

# Workouts
from app.modules.workouts.workout_route import router as workout_router
from app.modules.workouts.workout_model import WorkoutModel

# Workout Exercises
from app.modules.workout_exercise.workout_exercise_route import router as workout_exercise_router
from app.modules.workout_exercise.workout_exercise_model import WorkoutExerciseModel

# Workout Sets
from app.modules.workout_sets.workout_set_route import router as workout_set_router
from app.modules.workout_sets.workout_set_model import WorkoutSetModel


app = FastAPI()

# Allow CORS for all origins, methods, and headers
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Create database tables
UserModel.metadata.create_all(bind=engine)
ExerciseModel.metadata.create_all(bind=engine)
WorkoutModel.metadata.create_all(bind=engine)
WorkoutExerciseModel.metadata.create_all(bind=engine)
WorkoutSetModel.metadata.create_all(bind=engine)

# Root endpoint for health check or basic response
@app.get("/")
def health_check():
    return f"Health checked at {int(time.time() * 1000)} ms"

# Include routers from different modules
app.include_router(auth_router)
app.include_router(user_router)
app.include_router(exercise_router)
app.include_router(workout_router)
app.include_router(workout_exercise_router)
app.include_router(workout_set_router)

@app.on_event("startup")
def startup():
    db = SessionLocal()

    seed_categories(db)
    seed_exercises(db)

    db.close()