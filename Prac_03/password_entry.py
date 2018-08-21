"""Masking Password program Matthew Sampson"""

MIN_LENGTH = 9


def main():
    valid = False
    password = get_password()

    while not valid:
        if len(password) > MIN_LENGTH:
            mask_password(password)
            valid = True
        else:
            print("Invalid password length.")
            password = input("Please input a password great than {} characters: ".format(MIN_LENGTH))


def get_password():
    """Get password input"""
    return input("Please input a password great than {} characters: ".format(MIN_LENGTH))


def mask_password(password):
    """Print masked password"""
    print("*" * len(password))
    print("\n")


main()
