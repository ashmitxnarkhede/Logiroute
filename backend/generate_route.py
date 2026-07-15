from app.services.route_service import RouteService
from app.services.route_converter import RouteConverter


route_id = input("Route ID: ")

source = input("Source Name: ")
destination = input("Destination Name: ")

start_lat = float(input("Start Latitude: "))
start_lon = float(input("Start Longitude: "))

end_lat = float(input("End Latitude: "))
end_lon = float(input("End Longitude: "))


print("\nDownloading route...\n")

osrm_route = RouteService.get_route(
    start=(start_lon, start_lat),
    end=(end_lon, end_lat)
)

route = RouteConverter.convert(
    osrm_response=osrm_route,
    route_id=route_id,
    source=source,
    destination=destination,
    sample_rate=8
)

RouteConverter.save(
    route,
    f"../simulator/routes/{route_id}.json"
)

print("===================================")
print("Route Generated Successfully")
print("===================================")
print(f"Route ID   : {route_id}")
print(f"Waypoints  : {len(route['waypoints'])}")
print(f"Saved To   : simulator/routes/{route_id}.json")