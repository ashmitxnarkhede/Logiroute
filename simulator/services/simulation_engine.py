import time

from telemetry import build_telemetry_event
from producer import publish
from config import KAFKA_TOPIC


class SimulationEngine:

    def __init__(self, fleet_manager, route_engine):
        self.fleet_manager = fleet_manager
        self.route_engine = route_engine

    def start(self):

        while True:

            for vehicle in self.fleet_manager.get_all_vehicles():

                self.route_engine.move_vehicle(vehicle)

                event = build_telemetry_event(vehicle)

                publish(KAFKA_TOPIC, event)

            time.sleep(1)