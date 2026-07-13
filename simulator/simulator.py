import time

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

    speed_kmph=40,
    heading=90,

    fuel_level_percent=100,
    odometer_km=0,

    engine_status="ON",
    vehicle_status="MOVING",

    traffic_signal="GREEN",
    traffic_density="LOW",

    weather="CLEAR",

    cargo_weight_kg=850,

    battery_voltage=12.4,
    engine_temperature=85
)


while True:

    event = build_telemetry_event(truck)

    publish(KAFKA_TOPIC, event)

    time.sleep(1)