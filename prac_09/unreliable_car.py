from car import Car
import random


class UnreliableCar(Car):
    def __init__(self, name, fuel, reliability):
        super().__init__(name, fuel)
        self.reliability = reliability

    def random_reliability(self, distance):
        """Evaluates reliability against random number from 0 to 100 to decide whether to drive"""
        random_number = random.randint(1, 101)
        if random_number <= self.reliability:
            distance_driven = self.drive(distance)
        else:
            distance_driven = 0
        return distance_driven
