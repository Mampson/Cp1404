"""
CP 1404
Taxi sub class test
by Matthew Sampson

Created on 02/10/18

"""

from Prac_08.silver_service_taxi import SilverServiceTaxi


def main():
    """Test taxi (car subclass) features"""

    new_fancy_taxi = SilverServiceTaxi("Hummer", 100, 2)
    new_fancy_taxi.drive(18)
    print(new_fancy_taxi.get_fare())
    print(new_fancy_taxi)
    new_fancy_taxi.start_fare()
    new_fancy_taxi.drive(100)
    print(new_fancy_taxi)


main()
