import random

from services.route_engine import RouteEngine
from routes import ROUTES


class VehicleSimulator:

    def update(self, vehicle):

        route = ROUTES[vehicle.route_id]

        RouteEngine(route).move_vehicle(vehicle)

        self.update_speed(vehicle)
        self.update_fuel(vehicle)
        self.update_engine_temperature(vehicle)

        return vehicle

    def update_speed(self, vehicle):

        change = random.randint(-3, 3)

        vehicle.speed_kmph += change

        vehicle.speed_kmph = max(20, min(vehicle.speed_kmph, 80))

    def update_fuel(self, vehicle):

        vehicle.fuel_level_percent -= 0.02

        vehicle.fuel_level_percent = max(
            vehicle.fuel_level_percent,
            0
        )

    def update_engine_temperature(self, vehicle):

        vehicle.engine_temperature += random.uniform(-0.5, 0.5)

        vehicle.engine_temperature = max(
            80,
            min(vehicle.engine_temperature, 100)
        )