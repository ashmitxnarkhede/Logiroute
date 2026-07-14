from dataclasses import dataclass


@dataclass
class Delivery:
    delivery_id: str

    customer_name: str

    pickup_location: str
    destination: str

    cargo_weight_kg: float

    priority: str

    status: str