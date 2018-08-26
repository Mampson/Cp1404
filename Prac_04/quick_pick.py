"""
Quick picks lottery random numbers generator
by Matthew Sampson

"""
import random

NUMBERS_PER_QUICK_PICK = 6
MIN_NUMBER = 1
MAX_NUMBER = 45


def main():
    """Generate a desired number of quick pick lines, containing random numbers"""

    picks = get_number_of_picks()
    results = get_random_quick_picks(picks)
    print_array(results, picks)


def get_random_quick_picks(number):
    """generate quick picks based on passed number/variable """

    for i in range(number):
        quick_picks = []

        for j in range(NUMBERS_PER_QUICK_PICK):
            number = random.randint(MIN_NUMBER, MAX_NUMBER)
            while number in quick_picks:
                number = random.randint(MIN_NUMBER, MAX_NUMBER)
            quick_picks.append(number)
        quick_picks.sort()

        return [quick_picks]


def print_array(array, number):
    """format input before printing"""

    for number in array:
        print(" ".join("{:2} ".format(array))


def get_number_of_picks():
    """Get user pick number input"""

    picks = input("How many Quick Picks?: ")
    return int(picks)


main()
