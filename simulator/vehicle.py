class Vehicle:

    def __init__(self, vehicle_id, route):

        self.vehicle_id = vehicle_id

        self.route = route

        self.current_index = 0

        self.speed = 40

        self.fuel = 100

        self.status = "Moving"