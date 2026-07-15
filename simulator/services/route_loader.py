import json

from models.route import Route


class RouteLoader:

    @staticmethod
    def load(route_id: str):

        filepath = f"routes/{route_id}.json"

        with open(filepath, "r") as file:
            data = json.load(file)

        return Route(
            route_id=data["route_id"],
            source=data["source"],
            destination=data["destination"],
            waypoints=data["waypoints"]
        )