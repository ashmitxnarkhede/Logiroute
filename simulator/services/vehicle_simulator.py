from services.route_engine import RouteEngine




class VehicleSimulator:
    
    def __init__(self, routes):
        self.routes = routes

    def update(self, vehicle):

        route = self.routes[vehicle.route_id]

        RouteEngine(route).move_vehicle(vehicle)

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