"""
CP 1404
Silver service taxi (sub class of Taxi , which is sub of Car)
by Matthew Sampson

"""

from Prac_08.taxi import Taxi


class SilverServiceTaxi(Taxi):
    """Specialised taxi sub class """

    flag_fall = 4.50

    def __init__(self, name, fuel, fanciness):
        """Initialise silver service instance"""

        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km = super().price_per_km * fanciness

    def __str__(self):
        """Override Taxi Str method to include flagfall"""
        return "{} plus flagfall of ${:.2f} ".format(super().__str__(), self.flag_fall)

    def get_fare(self):
        """Override get fare with flag fall included"""

        silver_fare = super().get_fare() + self.flag_fall
        return silver_fare
