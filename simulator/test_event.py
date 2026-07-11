from models.vehicle import Vehicle
from telemetry import build_telemetry_event

truck = Vehicle(
    vehicle_id="TRUCK-0001",
    driver_id="DRV-0001",
    delivery_id="DEL-0001",
    route_id="R001",

    latitude=18.5913,
    longitude=73.7389,

    speed=42.5,
    fuel_level=98.7,

    status="MOVING"
)

event = build_telemetry_event(truck)

import json

print(json.dumps(event, indent=4))