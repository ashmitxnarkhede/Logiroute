from fastapi import FastAPI
from sqlalchemy import text
from fastapi.middleware.cors import CORSMiddleware
from app.database.database import engine
from app.api.telemetry import router as telemetry_router
from app.api.fleet import router as fleet_router
app = FastAPI(
    title="LogiRoute API",
    version="1.0.0"
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(telemetry_router)
app.include_router(fleet_router)

@app.get("/")
def home():
    return {
        "message": "Welcome to LogiRoute API"
    }


@app.get("/health/database")
def database_health():

    with engine.connect() as connection:

        result = connection.execute(text("SELECT 1"))

        return {
            "database": "connected",
            "result": result.scalar()
        }