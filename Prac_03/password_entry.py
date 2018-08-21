"""Masking Password program Matthew Sampson"""

MIN_LENGTH = 9


def main():
    password = get_password()

    if len(password) > MIN_LENGTH:
        return True
    else:
        print("Invalid password length.")
        password = input("Please input a password great than {} characters: ".format(MIN_LENGTH))

    print_mask_password(password)



def get_password():
    """Get password input"""
    return input("Please input a password great than {} characters: ".format(MIN_LENGTH))


def print_mask_password(password):
    """Print masked password"""
    print("*" * len(password))
    print("\n")


main()
