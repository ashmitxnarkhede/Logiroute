from services.fleet_manager import FleetManager
from services.fleet_initializer import FleetInitializer

fleet = FleetManager()

initializer = FleetInitializer(fleet)

initializer.initialize()

print(fleet.get_all_vehicles())