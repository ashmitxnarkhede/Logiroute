from app.services.route_service import RouteService
from app.services.route_converter import RouteConverter


osrm_route = RouteService.get_route(
    start=(73.8567, 18.5204),
    end=(72.8777, 19.0760)
)

route = RouteConverter.convert(
    osrm_response=osrm_route,
    route_id="R001",
    source="Pune",
    destination="Mumbai",
    sample_rate=8
)

RouteConverter.save(
    route,
    "../simulator/routes/R001.json"
)

print("Route created successfully.")
print(f"Waypoints: {len(route['waypoints'])}")