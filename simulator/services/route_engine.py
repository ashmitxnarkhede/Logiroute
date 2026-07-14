from models.vehicle import Vehicle
from models.route import Route


class RouteEngine:

    def __init__(self, route: Route):
        self.route = route

    def move_vehicle(self, vehicle: Vehicle):

        if vehicle.current_waypoint_index >= len(self.route.waypoints) - 1:
            vehicle.vehicle_status = "ARRIVED"
            return vehicle

        start_lat, start_lon = self.route.waypoints[
            vehicle.current_waypoint_index
        ]

        end_lat, end_lon = self.route.waypoints[
            vehicle.current_waypoint_index + 1
        ]

        step = 0.02

        vehicle.progress_to_next_waypoint += step

        if vehicle.progress_to_next_waypoint >= 1.0:

            vehicle.current_waypoint_index += 1
            vehicle.progress_to_next_waypoint = 0.0

            vehicle.latitude = end_lat
            vehicle.longitude = end_lon

        else:

            p = vehicle.progress_to_next_waypoint

            vehicle.latitude = start_lat + (end_lat - start_lat) * p
            vehicle.longitude = start_lon + (end_lon - start_lon) * p

        return vehicle