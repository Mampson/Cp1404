"""for i in range(1, 21, 2):
    print(i, end=' ')
print()"""


def listA():
    print("List A: " + "\n")
    for i in range(0, 100, 10):
        print(i, end=' ')
    print()


def listB():
    print("List B: " + "\n")

    for i in range(20, 0, -1):
        print(i, end=' ')
    print()


def stars():
    num_stars = int(input("please enter the number of desired stars: " + "\n"))

    for i in range(0, num_stars, 1):
        print("*", end=' ')
    else:
        if num_stars <= 0:
            print("sorry that was invalid input, please try again." + "\n")
            stars()


def starsIncrease():
    num_stars = int(input("please enter the number of desired stars: " + "\n"))

    for i in range(0, num_stars, 1):
        print("*", end='\n')

    else:
        if num_stars <= 0:
            print("sorry that was invalid input, please try again." + "\n")
            stars()


def main():
    listA()
    listB()
    stars()
    starsIncrease()


main()
