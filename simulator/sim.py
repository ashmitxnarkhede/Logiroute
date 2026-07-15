import time

from services.fleet_manager import FleetManager
from services.fleet_initializer import FleetInitializer

from services.vehicle_simulator import VehicleSimulator
from telemetry import build_telemetry_event
from producer import publish
from config import KAFKA_TOPIC


fleet = FleetManager()
initializer = FleetInitializer(fleet)
initializer.initialize()

from services.route_loader import RouteLoader

routes = {
    "R001": RouteLoader.load("R001")
}

vehicle_simulator = VehicleSimulator(routes)


while True:

    for vehicle in fleet.get_all_vehicles():

        vehicle_simulator.update(vehicle)

        event = build_telemetry_event(vehicle)

        publish(KAFKA_TOPIC, event)

    time.sleep(1)