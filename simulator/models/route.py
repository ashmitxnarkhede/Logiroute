from dataclasses import dataclass


@dataclass
class Route:
    route_id: str
    source: str
    destination: str

    # List of (latitude, longitude)
    waypoints: list[tuple[float, float]]