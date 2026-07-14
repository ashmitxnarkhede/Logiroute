from models.vehicle import Vehicle
from models.driver import Driver
from models.delivery import Delivery


class FleetManager:

    def __init__(self):
        self.vehicles = {}
        self.drivers = {}
        self.deliveries = {}

    def add_vehicle(self, vehicle: Vehicle):
        self.vehicles[vehicle.vehicle_id] = vehicle

    def add_driver(self, driver: Driver):
        self.drivers[driver.driver_id] = driver

    def add_delivery(self, delivery: Delivery):
        self.deliveries[delivery.delivery_id] = delivery

    def get_all_vehicles(self):
        return list(self.vehicles.values())