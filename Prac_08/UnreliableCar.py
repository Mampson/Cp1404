"""
Cp 1404
Unreliable sub class of Car
by Matthew Sampson
"""

from Prac_08.car import Car
from random import randint


class UnreliableCar(Car):

    def __init__(self, name, fuel, reliability):
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        if randint(1, 100) >= self.reliability:
            distance = 0

        drive_distance = super().drive(distance)
        return drive_distance
