"""
CP 1404
Taxi sub class test
by Matthew Sampson

Created on 02/10/18

"""

from Prac_08.taxi import Taxi


def main():
    """Test taxi (car subclass) features"""

    new_taxi = Taxi("Prius 1", 100)
    new_taxi.drive(40)
    print(new_taxi)
    new_taxi.start_fare()
    new_taxi.drive(100)
    print(new_taxi)


main()
