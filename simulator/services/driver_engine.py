import random


class DriverEngine:

    @staticmethod
    def update(vehicle):

        change = random.randint(-3, 3)

        vehicle.speed_kmph += change

        vehicle.speed_kmph = max(
            15,
            min(vehicle.speed_kmph, 80)
        )