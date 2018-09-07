"""
Guitar class Test program

by
Matthew Sampson
"""

from Prac_06.guitar import Guitar


def main():
    """Test program for Guitar objects """

    guitars = []

    guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))
    guitars.append(Guitar("Fender Stratocaster", 2014, 765.40))
    guitars.append(Guitar("Sampson Special A8", 1990, 2800.00))

    guitar_list_print(guitars)


def guitar_list_print(guitars):

    for i in range(len(guitars)):
        print(" {} get_age() - Expected {} . Got: {} ".format(guitars[i].name, 96,
                                                              guitars[i].get_age()))

        print(" {} is_vintage() - Expected {} . Got: {} ".format(guitars[i].name, 2018 - guitars[i].year,
                                                                 guitars[i].is_vintage()))


main()
