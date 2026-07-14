import time

from services.fleet_manager import FleetManager
from services.fleet_initializer import FleetInitializer
from services.route_engine import RouteEngine

from routes import ROUTES

from telemetry import build_telemetry_event
from producer import publish
from config import KAFKA_TOPIC


fleet = FleetManager()
initializer = FleetInitializer(fleet)
initializer.initialize()


while True:

    for vehicle in fleet.get_all_vehicles():

        route = ROUTES[vehicle.route_id]
        engine = RouteEngine(route)

        engine.move_vehicle(vehicle)

        event = build_telemetry_event(vehicle)

        publish(KAFKA_TOPIC, event)

    time.sleep(1)