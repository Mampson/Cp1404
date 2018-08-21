"""Matthew Sampson"""

MIN_LENGTH = 5


def main():
    get_password()


def get_password():
    valid = False
    password = input("Please input a password great than 5 characters: ")
    while not valid:
        if len(password) > MIN_LENGTH:
            mask_pass
            valid = True

        else:
            print("Invalid password length.")
            password = input("Please input a password great than 4 characters: ")


def mask_password(password):

    print("*" * len(password))
    print("\n")


main()