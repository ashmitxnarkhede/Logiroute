import requests


class RouteService:

    BASE_URL = "https://router.project-osrm.org/route/v1/driving"

    @staticmethod
    def get_route(start, end):

        url = (
            f"{RouteService.BASE_URL}/"
            f"{start[0]},{start[1]};"
            f"{end[0]},{end[1]}"
            "?overview=full&geometries=geojson"
        )

        response = requests.get(url, timeout=20)

        response.raise_for_status()

        return response.json()