from services.route_engine import RouteEngine
from services.driver_engine import DriverEngine
from services.eta_engine import ETAEngine


class VehicleSimulator:

    def __init__(self, routes):
        self.routes = routes

    def update(self, vehicle):

        route = self.routes[vehicle.route_id]

        DriverEngine.update(vehicle)
        RouteEngine(route).move_vehicle(vehicle)
        ETAEngine.update(vehicle)

        # Mark vehicle as arrived
        if vehicle.remaining_distance_km <= 0:
            vehicle.remaining_distance_km = 0
            vehicle.eta_minutes = 0
            vehicle.speed_kmph = 0
            vehicle.vehicle_status = "ARRIVED"
            vehicle.engine_status = "OFF"

        if vehicle.vehicle_status != "ARRIVED":
            self.update_fuel(vehicle)
            self.update_engine_temperature(vehicle)

        return vehicle

    def update_fuel(self, vehicle):

        vehicle.fuel_level_percent -= 0.02

        vehicle.fuel_level_percent = max(
            vehicle.fuel_level_percent,
            0
        )

    def update_engine_temperature(self, vehicle):

        import random

        vehicle.engine_temperature += random.uniform(-0.5, 0.5)

        vehicle.engine_temperature = max(
            80,
            min(vehicle.engine_temperature, 100)
        )