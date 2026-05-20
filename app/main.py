import time

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.db.db import engine

# Workout 
from app.modules.workouts.workout_route import router as workout_router
from app.modules.workouts.workout_model import WorkoutModel

app = FastAPI()

# Allow CORS for all origins, methods, and headers
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Create database tables
WorkoutModel.metadata.create_all(bind=engine)

# Root endpoint for health check or basic response
@app.get("/")
def health_check():
    return f"Health checked at {int(time.time() * 1000)} ms"

# Include routers from different modules
app.include_router(workout_router)