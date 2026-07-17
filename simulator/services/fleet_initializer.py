from models.driver import Driver
from models.vehicle import Vehicle
from models.delivery import Delivery

from services.route_loader import RouteLoader


class FleetInitializer:

    def __init__(self, fleet_manager):
        self.fleet_manager = fleet_manager

    def initialize(self):

        route = RouteLoader.load("R001")

        fleet_data = [
            ("VH001", "D001", "DEL001", "Rahul Sharma", 42, 95, "NORMAL"),
            ("VH002", "D002", "DEL002", "Amit Patil", 50, 88, "AGGRESSIVE"),
            ("VH003", "D003", "DEL003", "Suresh Jadhav", 30, 18, "CALM"),
            ("VH004", "D004", "DEL004", "Vikram Singh", 0, 80, "NORMAL"),
            ("VH005", "D005", "DEL005", "Rohan Deshmukh", 75, 85, "AGGRESSIVE"),
        ]

        # Starting positions on the route
        waypoint_indexes = [
            5,                              # VH001
            20,                             # VH002
            len(route.waypoints) - 3,       # VH003 (almost finished)
            len(route.waypoints) - 1,       # VH004 (destination)
            30                              # VH005
        ]

        for i, (
            vehicle_id,
            driver_id,
            delivery_id,
            driver_name,
            speed,
            fuel,
            driving_style,
        ) in enumerate(fleet_data):

            driver = Driver(
                driver_id=driver_id,
                name=driver_name,
                phone_number=f"98765432{i+10}",
                license_number=f"MH12DL12{i+10}",
                experience_years=3 + i,
                status="AVAILABLE",
                driving_style=driving_style,
            )

            delivery = Delivery(
                delivery_id=delivery_id,
                customer_name="Amazon",
                pickup_location="Pune Warehouse",
                destination="Mumbai Hub",
                cargo_weight_kg=850 + (i * 50),
                priority="HIGH",
                status="ASSIGNED",
            )

            waypoint = waypoint_indexes[i]

            vehicle = Vehicle(
                vehicle_id=vehicle_id,
                driver_id=driver.driver_id,
                delivery_id=delivery.delivery_id,
                route_id=route.route_id,

                latitude=route.waypoints[waypoint][0],
                longitude=route.waypoints[waypoint][1],

                speed_kmph=speed,
                heading=0,

                fuel_level_percent=fuel,
                odometer_km=12000 + (i * 150),

                eta_minutes=0,
                driving_style=driving_style,

                engine_status="ON",
                vehicle_status="MOVING",

                remaining_distance_km=0,

                weather="CLEAR",

                cargo_weight_kg=850 + (i * 50),

                battery_voltage=12.6,
                engine_temperature=88,

                current_waypoint_index=waypoint,
            )

            # Demo scenarios

            # VH003: Low fuel and almost at destination
            if vehicle.vehicle_id == "VH003":
                vehicle.remaining_distance_km = 1.0
                vehicle.eta_minutes = 2

            # VH004: Already arrived
            if vehicle.vehicle_id == "VH004":
                vehicle.remaining_distance_km = 0
                vehicle.eta_minutes = 0
                vehicle.vehicle_status = "ARRIVED"
                vehicle.engine_status = "OFF"

            # VH005: Overspeeding
            if vehicle.vehicle_id == "VH005":
                vehicle.speed_kmph = 75

            self.fleet_manager.add_driver(driver)
            self.fleet_manager.add_delivery(delivery)
            self.fleet_manager.add_vehicle(vehicle)