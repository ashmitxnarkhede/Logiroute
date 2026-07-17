class ETAEngine:

    @staticmethod
    def update(vehicle):

        if vehicle.speed_kmph <= 0:
            vehicle.eta_minutes = 0
            return

        vehicle.eta_minutes = (
            vehicle.remaining_distance_km /
            vehicle.speed_kmph
        ) * 60