from fastapi import APIRouter
import json
from pathlib import Path

router = APIRouter(prefix="/routes", tags=["Routes"])


@router.get("/{route_id}")
def get_route(route_id: str):

    route_file = (
        Path(__file__).resolve().parents[3]
        / "simulator"
        / "routes"
        / f"{route_id}.json"
    )

    with open(route_file, "r") as f:
        return json.load(f)