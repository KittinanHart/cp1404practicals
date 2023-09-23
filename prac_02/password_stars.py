
"""Module docstring"""


# imports
# CONSTANTS

def main():
    """Function docstring"""
    password = get_password()

    print_asterisks(password)


def print_asterisks(password):
    asterisks = '*' * len(password)
    print(asterisks)


def get_password():
    password = input("Enter password: ")
    return password


main()
