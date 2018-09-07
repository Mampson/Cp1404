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

        for i in range(len(guitars)):

            if guitars[i].is_vintage():
                over_50 = "This is a vintage Guitar"
            else:
                over_50 = ""

            print("Guitar {}: {:>30} ( {} ) , costs: $ {:20.2f}  {}".format(i +1, guitars[i].name, guitars[i].year,
                                                                            guitars.cost, over_50))


main()

