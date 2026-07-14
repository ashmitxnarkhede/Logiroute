from dataclasses import dataclass


@dataclass
class Vehicle:
    # Identity
    vehicle_id: str
    driver_id: str
    delivery_id: str
    route_id: str

    # GPS
    latitude: float
    longitude: float

    # Movement
    speed_kmph: float
    target_speed_kmph: float
    heading: float

    # Fuel
    fuel_level_percent: float
    odometer_km: float

    # State
    engine_status: str
    vehicle_status: str

    

    weather: str

    cargo_weight_kg: float

    battery_voltage: float
    engine_temperature: float

    # Simulator state
    current_waypoint_index: int = 0
    progress_to_next_waypoint: float = 0.0