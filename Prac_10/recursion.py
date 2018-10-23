"""
CP1404/CP5632 Practical
Recursion
"""


def do_it(n):
    """Do... it."""
    if n <= 0:
        return 0
    return n % 2 + do_it(n - 1)
# n % 2 = remainder 1 then do_it(4) = 0 then repeat until n < = 0
# gives 1 + 0 + 1 + 0 + 1 = 3

# TODO: 1. write down what you think the output of this will be,
# first i assumed the answer would be 1 , as not expecting the recursion of do_it until n <=0
# TODO: 2. use the debugger to step through and see what's actually happening
#print(do_it(5))


def do_something(n):
    """Print the squares of positive numbers from n down to 0."""
    if n > 0:
        print(n ** 2)
        do_something(n - 1)
    else:
        return

# TODO: 3. write down what you think the output of do_something(4) will be,
# assume that nothing will print until the value of n becomes -1 and then prints will return the n squared until
# manually stopped
# TODO: 4. use the debugger to step through and see what's actually happening
do_something(4)

# TODO: 5. fix do_something() so that it works according to the docstring


def do_something(n):
    """Print the squares of positive numbers from n down to 0."""
    if n > 0:
        print(n ** 2)
        do_something(n - 1)
    else:
        return

# TODO do_something backwards
def do_something_backwards(n):
    """Print the squares of positive numbers from 0 to n """
    while 0 <= n :
        print(n ** 2)
        do_something(n +1)

#do_something_backwards(4)

# Build pyramid

def build_pyramid():
    """Return required blocks for number of rows high 2d pyramid"""

    number_of_rows = int(input("Enter the number of rows you wish to build: "))
    print("For a pyramid {} rows high you will need {} bricks. ".format(number_of_rows,
                                                                        get_total_bricks(number_of_rows)))
def get_total_bricks(rows):

    if rows < 0:
        return 0
    else:
        return rows + get_total_bricks(rows - 1)

build_pyramid()



