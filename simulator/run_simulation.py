from services.fleet_manager import FleetManager
from services.fleet_initializer import FleetInitializer
from services.route_engine import RouteEngine
from services.simulation_engine import SimulationEngine

from routes import PUNE_TO_MUMBAI


def main():

    fleet = FleetManager()

    initializer = FleetInitializer(fleet)
    initializer.initialize()

    route_engine = RouteEngine(PUNE_TO_MUMBAI)

    simulation = SimulationEngine(
        fleet_manager=fleet,
        route_engine=route_engine
    )

    print("Starting LogiRoute Fleet Simulation...\n")

    simulation.start()


if __name__ == "__main__":
    main()