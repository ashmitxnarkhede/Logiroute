from models.vehicle import Vehicle
from models.route import Route

from utils.geo import haversine_distance, interpolate


class RouteEngine:

    def __init__(self, route: Route):
        self.route = route

    def move_vehicle(self, vehicle: Vehicle):

        waypoints = self.route.waypoints

        if vehicle.current_waypoint_index >= len(waypoints) - 1:
            vehicle.vehicle_status = "ARRIVED"
            vehicle.engine_status = "OFF"
            vehicle.speed_kmph = 0
            return vehicle

        start = waypoints[vehicle.current_waypoint_index]
        end = waypoints[vehicle.current_waypoint_index + 1]

        segment_distance = haversine_distance(
            start[0], start[1],
            end[0], end[1]
        )

        distance_this_second = vehicle.speed_kmph / 3600

        progress_increment = distance_this_second / segment_distance

        vehicle.progress_to_next_waypoint += progress_increment

        while vehicle.progress_to_next_waypoint >= 1:

            vehicle.progress_to_next_waypoint -= 1
            vehicle.current_waypoint_index += 1

            if vehicle.current_waypoint_index >= len(waypoints) - 1:
                vehicle.latitude = waypoints[-1][0]
                vehicle.longitude = waypoints[-1][1]
                vehicle.vehicle_status = "ARRIVED"
                vehicle.engine_status = "OFF"
                vehicle.speed_kmph = 0
                return vehicle

            start = waypoints[vehicle.current_waypoint_index]
            end = waypoints[vehicle.current_waypoint_index + 1]

            segment_distance = haversine_distance(
                start[0], start[1],
                end[0], end[1]
            )

            progress_increment = distance_this_second / segment_distance

        vehicle.latitude, vehicle.longitude = interpolate(
    start,
    end,
    vehicle.progress_to_next_waypoint
)

        vehicle.odometer_km += distance_this_second

        # Calculate remaining distance
        remaining = haversine_distance(
            vehicle.latitude,
            vehicle.longitude,
            end[0],
            end[1]
        )

        for i in range(vehicle.current_waypoint_index + 1, len(waypoints) - 1):
            remaining += haversine_distance(
                waypoints[i][0],
                waypoints[i][1],
                waypoints[i + 1][0],
                waypoints[i + 1][1]
            )

        vehicle.remaining_distance_km = round(remaining, 2)

        return vehicle