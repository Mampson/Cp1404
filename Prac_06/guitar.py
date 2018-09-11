"""
Guitar Class
by Matthew Sampson
"""
PRESENT_YEAR = 2018
VINTAGE_AGE = 50


class Guitar:
    """Guitar Object"""

    def __init__(self, name="", year=0, cost=0):
        """Initialize Guitar Object

            name = string
            year = int
            cost = $ float
        """

        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return string of Guitar information"""
        return "{} ( {} ) : {} ".format(self.name, self.year, self.cost)

    def get_age(self):
        """Give age of Guitar"""
        return PRESENT_YEAR - self.year

    def is_vintage(self):
        """"Determine if ages in vintage range"""
        return self.get_age() >= VINTAGE_AGE



