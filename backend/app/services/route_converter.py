import json


class RouteConverter:

    @staticmethod
    def convert(
        osrm_response,
        route_id,
        source,
        destination,
        sample_rate=8
    ):

        coordinates = osrm_response["routes"][0]["geometry"]["coordinates"]

        waypoints = []

        for i in range(0, len(coordinates), sample_rate):

            longitude, latitude = coordinates[i]

            waypoints.append([latitude, longitude])

        # Always include the destination
        last_longitude, last_latitude = coordinates[-1]

        if waypoints[-1] != [last_latitude, last_longitude]:
            waypoints.append([last_latitude, last_longitude])

        return {
            "route_id": route_id,
            "source": source,
            "destination": destination,
            "waypoints": waypoints
        }

    @staticmethod
    def save(route, filepath):

        with open(filepath, "w") as file:
            json.dump(route, file, indent=4)