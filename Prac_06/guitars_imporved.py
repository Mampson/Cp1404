"""
Guitars program
by
Matthew Sampson
"""

from Prac_06.guitar import Guitar


def main():
    """Get Guitar objects in list until blank entry """

    guitars = []

    name = input("Enter guitar name: ")

    while name != "":
        year = int(input("Year made: "))
        cost = float(input("Cost: "))
        next_guitar_add = Guitar(name, year, cost)
        guitars.append(next_guitar_add)
        print(next_guitar_add, "Added to Guitars")
        name = input("Enter guitar name: ")

    guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))
    guitars.append(Guitar("Fender Stratocaster", 2014, 765.40))
    guitars.append(Guitar("Sampson Special A8", 1990, 2800.00))

    print("My Guitars: ")

    if guitars is not None:

        for i, guitar in enumerate(guitars):
            vintage_y_or_n = ("This is a Vintage Guitar" if guitars[i].is_vintage() else "")
            # Ternary operator

            print("Guitar {0}: {1.name:<20} ({1.year}), Cost: $ {1.cost:10.2f}  {2}".format(i + 1, guitar,
                                                                                            vintage_y_or_n))


main()
