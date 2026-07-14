from models.vehicle import Vehicle
from telemetry import build_telemetry_event
from producer import publish
from config import KAFKA_TOPIC


truck = Vehicle(
    vehicle_id="TRUCK-0001",
    driver_id="DRV-0001",
    delivery_id="DEL-0001",
    route_id="R001",

    latitude=18.5913,
    longitude=73.7389,

    speed_kmph=42.5,
    target_speed_kmph=40,
    heading=135,

    fuel_level_percent=98.7,
    odometer_km=12453.6,

    engine_status="ON",
    vehicle_status="MOVING",

   
    weather="CLEAR",

    cargo_weight_kg=850.0,

    battery_voltage=12.4,
    engine_temperature=87.2,
)

event = build_telemetry_event(truck)

publish(KAFKA_TOPIC, event)