from models.driver import Driver
from models.vehicle import Vehicle
from models.delivery import Delivery

from services.route_loader import RouteLoader


class FleetInitializer:

    def __init__(self, fleet_manager):
        self.fleet_manager = fleet_manager

    def initialize(self):
        
        route = RouteLoader.load("R001")

        driver = Driver(
            driver_id="D001",
            name="Rahul Sharma",
            phone_number="9876543210",
            license_number="MH12DL12345",
            experience_years=5,
            status="AVAILABLE"
        )

        delivery = Delivery(
            delivery_id="DEL001",
            customer_name="Amazon",
            pickup_location="Pune Warehouse",
            destination="Mumbai Hub",
            cargo_weight_kg=850,
            priority="HIGH",
            status="ASSIGNED"
        )

        vehicle = Vehicle(
            vehicle_id="VH001",
            driver_id=driver.driver_id,
            delivery_id=delivery.delivery_id,
            route_id=route.route_id,

            latitude=route.waypoints[0][0],
            longitude=route.waypoints[0][1],

            speed_kmph=40,
            target_speed_kmph=40,
            heading=0,

            fuel_level_percent=95,
            odometer_km=12000,

            engine_status="ON",
            vehicle_status="MOVING",

            weather="CLEAR",

            cargo_weight_kg=850,

            battery_voltage=12.6,
            engine_temperature=88
        )
        self.fleet_manager.add_driver(driver)
        self.fleet_manager.add_delivery(delivery)
        self.fleet_manager.add_vehicle(vehicle)