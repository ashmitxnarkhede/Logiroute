from dataclasses import dataclass


@dataclass
class Vehicle:
    # Identity
    vehicle_id: str
    driver_id: str
    delivery_id: str
    route_id: str

    # GPS Location
    latitude: float
    longitude: float

    # Vehicle Movement
    speed_kmph: float
    heading: float

    # Fuel & Distance
    fuel_level_percent: float
    odometer_km: float

    # Vehicle State
    engine_status: str
    vehicle_status: str

    # Road Conditions
    traffic_signal: str
    traffic_density: str

    # Environment
    weather: str

    # Cargo
    cargo_weight_kg: float

    # Vehicle Health
    battery_voltage: float
    engine_temperature: float