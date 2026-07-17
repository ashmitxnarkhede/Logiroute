import uuid
from datetime import datetime, timezone


def build_telemetry_event(vehicle):
    """
    Convert a Vehicle object into a telemetry event dictionary.
    """

    return {
        "metadata": {
            "event_id": str(uuid.uuid4()),
            "event_type": "vehicle.telemetry",
            "event_version": "2.0",
            "timestamp": datetime.now(timezone.utc).isoformat()
        },

        "payload": {

            "vehicle_id": vehicle.vehicle_id,
            "driver_id": vehicle.driver_id,
            "delivery_id": vehicle.delivery_id,
            "route_id": vehicle.route_id,

            "latitude": vehicle.latitude,
            "longitude": vehicle.longitude,

            "speed_kmph": vehicle.speed_kmph,
            "heading": vehicle.heading,

            "fuel_level_percent": vehicle.fuel_level_percent,
            "odometer_km": vehicle.odometer_km,
            "remaining_distance_km": vehicle.remaining_distance_km,
            "eta_minutes": vehicle.eta_minutes,
            "engine_status": vehicle.engine_status,
            "vehicle_status": vehicle.vehicle_status,

            

            "weather": vehicle.weather,

            "cargo_weight_kg": vehicle.cargo_weight_kg,

            "battery_voltage": vehicle.battery_voltage,
            "engine_temperature": vehicle.engine_temperature
        }
    }