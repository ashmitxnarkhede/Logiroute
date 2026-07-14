from fastapi import APIRouter

from app.services.telemetry_service import TelemetryService

router = APIRouter(
    prefix="/telemetry",
    tags=["Telemetry"]
)


@router.get("/latest")
def latest(limit: int = 20):

    return TelemetryService.get_latest(limit)