"""
Create numbers list and peform operations
by Matthew Sampson

"""


NUMBER_OF_INPUTS = 5


def main():
    """Create list of input numbers and preform specified operations """

    numbers = []
    for i in range(NUMBER_OF_INPUTS):
        current_number = get_number()
        numbers.append(current_number)

    print(numbers)
    print("The first number in the list is : {} ".format(numbers[0]))
    print("The final number in the list is : {} ".format(numbers[-1]))
    print("The smallest number in the list is : {}".format(min(numbers)))
    print("The largest number in the list is : {} ".format(max(numbers)))
    print("The average of all elements in the list is : {} ".format(sum(numbers) / NUMBER_OF_INPUTS))


def get_number():
    return input("Please enter a number: ")


main()
