"""
Taxi simulator
By Matthew Sampson
Created on 15/10/2018
"""

from Prac_08.taxi import Taxi
from Prac_08.silver_service_taxi import SilverServiceTaxi

MENU = " q)uit, c)hoose taxi, d)rive"


def main():
    """Build list of taxi objects to choose from and simulate drive and billing"""
    print("Lets Drive! ")
    current_taxi = None
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    total_trip_cost = 0

    menu_choice = get_menu_choice()
    while menu_choice != "q":

        if menu_choice == "c":
            # list taxis
            print_taxis(taxis)
            taxi_number = get_taxi_choice(taxis)
            current_taxi = assign_taxi(taxi_number, taxis)
            print("Bill to date: ${}".format(total_trip_cost))
            menu_choice = get_menu_choice()
        elif menu_choice == "d":
            # drive taxi
            if current_taxi == None:
                print("You must choose a taxi first! ")
                menu_choice = get_menu_choice()
            else:
                print("Drive how far? ")
                desired_drive_distance = get_int_entry()
                current_taxi.drive(desired_drive_distance)
                total_trip_cost = total_trip_cost + current_taxi.get_fare()
                print("Your {} trip cost you: ${} ".format(current_taxi.name, current_taxi.get_fare()))
                print("Bill to date: {} ".format(total_trip_cost))
                menu_choice = get_menu_choice()
        else:
            print("Invalid menu choice please try again")
            menu_choice = get_menu_choice()
    # print total trip cost
    print("Total trip cost: ${} ".format(total_trip_cost))
    # re-print taxis with changed conditions
    print("Taxis are now: \n")
    print_taxis(taxis)


def assign_taxi(number, taxis):
    """assign current taxi to choose type"""
    current_taxi = taxis[number]
    return current_taxi


def get_taxi_choice(taxis):
    """Check that taxi choice is valid and return choice"""
    taxi_choice = int(input("Choose taxi: "))
    if taxi_choice in range(len(taxis)):
        return taxi_choice
    else:
        print("Invalid taxi choice, please try again")
        get_taxi_choice(taxis)


def get_menu_choice():
    """Prompt for user menu selection input"""
    print(MENU)
    user_input = input(">>> ")
    return user_input.lower()


def print_taxis(taxis):
    """print formated table of taxis """
    for i, taxi in enumerate(taxis):
        print("{} - {} ".format(i, str(taxi)))


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


def get_string_entry(string):
    """Get string input from the user"""
    entry = str(input(string))
    while entry == "":
        print("Input cannot be blank.")
        entry = input(string)
    else:
        return entry


main()
