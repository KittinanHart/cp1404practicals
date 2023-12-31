"""
CP1404/CP5632 - Practical
Pseudocode for temperature conversion
"""


def main():

    print_menu()
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            celsius = float(input("Celsius: "))
            fahrenheit = celsius_to_fahrenheit(celsius)
            print(f"Result: {fahrenheit:.2f} F")
        elif choice == "F":
            fahrenheit = float(input(" Fahrenheit: "))
            celsius = fahrenheit_to_celsius(fahrenheit)
            print(f"Result: {celsius:.2f} C")
        else:
            print("Invalid option")
        print_menu()
        choice = input(">>> ").upper()
    print("Thank you.")


def print_menu():
    print('C - Convert Celsius to Fahrenheit')
    print('F - Convert Fahrenheit to Celsius')
    print('Q - Quit')


def fahrenheit_to_celsius(fahrenheit):
    return 5 / 9 * (fahrenheit - 32)


def celsius_to_fahrenheit(celsius):
    return celsius * 9.0 / 5 + 32


main()
