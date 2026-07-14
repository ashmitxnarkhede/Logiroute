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

vehicle_simulator = VehicleSimulator()


vehicle_simulator = VehicleSimulator()

while True:

    for vehicle in fleet.get_all_vehicles():

        vehicle_simulator.update(vehicle)

        event = build_telemetry_event(vehicle)

        publish(KAFKA_TOPIC, event)

    time.sleep(1)