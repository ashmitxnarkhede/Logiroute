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
    
    heading: float

    # Fuel
    fuel_level_percent: float
    odometer_km: float
    eta_minutes: float

    # State
    engine_status: str
    vehicle_status: str
    driving_style: str
    
    

    weather: str

    cargo_weight_kg: float

    battery_voltage: float
    engine_temperature: float
# Analytics
    remaining_distance_km: float = 0
    # Simulator state
    current_waypoint_index: int = 0
    progress_to_next_waypoint: float = 0.0
    
    waiting_at_signal: bool = False
    signal_wait_time: int = 0
    
    