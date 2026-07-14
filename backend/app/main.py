from fastapi import FastAPI
from sqlalchemy import text

from app.database.database import engine
from app.api.telemetry import router as telemetry_router

app = FastAPI(
    title="LogiRoute API",
    version="1.0.0"
)

app.include_router(telemetry_router)


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