"""
Car Driving Simulator
by

Matthew Sampson
"""
from Prac_06.car import Car

STARTING_FUEL = 100
MENU = """Menu
d) drive
r) refuel
q) quit
Enter your choice: """


def main():
    """Simulate driving of car object"""

    print("Lets Drive!")
    car_name = get_name()
    my_car = Car(car_name, STARTING_FUEL)
    menu_choice = str(display_menu()).lower()

    while menu_choice != "q":

        if menu_choice == "d":
            print("How many km's do you wish to drive? ")
            drive_distance = get_int_entry()
            if my_car.fuel - drive_distance > 0:
                print("Your car drove {} kms ".format(drive_distance))
                my_car.odometer = my_car.odometer + drive_distance
                my_car.fuel = my_car.fuel - drive_distance
                print("Your car has travelled {} kms today".format(my_car.odometer))

            else:
                print("Your car doesn't have enough fuel!")

            print(my_car)
            menu_choice = display_menu()

        elif menu_choice == "r":
            print("How many units of fuel do you wish to add to the car? ")
            amount_to_refuel = get_int_entry()

            print("Added {} units to the car".format(amount_to_refuel))
            print(my_car)
            menu_choice = display_menu()

        else:
            print("Invalid menu choice, please try again.")
            menu_choice = display_menu()

    print("Good by the {} 's driver! ".format(my_car.name))


def get_int_entry():
    """ Get integer input from user"""

    is_int = False

    while not is_int:
        try:
            entry = int(input())
            if entry > 0:
                is_int = True
                return entry

            else:
                print("Number must be > 0 ")

        except ValueError:
            print("Invalid input; enter a valid number")


def display_menu():
    """Display menu"""

    print(MENU)
    entry = input()
    return entry


def get_name():
    """Prompt for name input"""

    name = input("Enter your car name: ")

    return name


main()
