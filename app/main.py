import time

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.db.db import engine

# Auth
from app.modules.auths.auth_route import router as auth_router

# User
from app.modules.users.user_route import router as user_router
from app.modules.users.user_model import UserModel

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

# Root endpoint for health check or basic response
@app.get("/")
def health_check():
    return f"Health checked at {int(time.time() * 1000)} ms"

# Include routers from different modules
app.include_router(auth_router)
app.include_router(user_router)