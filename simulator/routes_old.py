from models.route import Route

PUNE_TO_MUMBAI = Route(
    route_id="R001",
    source="Pune",
    destination="Mumbai",
    waypoints=[
        (18.5204, 73.8567),
        (18.6500, 73.9000),
        (18.8500, 73.9800),
        (19.0760, 72.8777)
    ]
)

PUNE_TO_NASHIK = Route(
    route_id="R002",
    source="Pune",
    destination="Nashik",
    waypoints=[
        (18.5204, 73.8567),
        (18.7600, 73.9200),
        (19.2000, 73.9500),
        (19.9975, 73.7898)
    ]
)

PUNE_TO_AHMEDNAGAR = Route(
    route_id="R003",
    source="Pune",
    destination="Ahmednagar",
    waypoints=[
        (18.5204, 73.8567),
        (18.7500, 74.0500),
        (18.9500, 74.3000),
        (19.0952, 74.7496)
    ]
)

ROUTES = {
    PUNE_TO_MUMBAI.route_id: PUNE_TO_MUMBAI,
    PUNE_TO_NASHIK.route_id: PUNE_TO_NASHIK,
    PUNE_TO_AHMEDNAGAR.route_id: PUNE_TO_AHMEDNAGAR,
}