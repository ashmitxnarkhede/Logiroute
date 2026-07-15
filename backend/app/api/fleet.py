from fastapi import APIRouter

from app.services.telemetry_service import TelemetryService

router = APIRouter(prefix="/fleet", tags=["Fleet"])


@router.get("/live")
def get_live_fleet():
    return TelemetryService.get_latest()