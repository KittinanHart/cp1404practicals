
def main():
    user_score = None
    while True:
        print_menu()
        choice = input("Enter a choice:").upper()

        if choice == "G":
            return get_valid_score()
        elif choice == "P":
            if user_score is not None:
                print_result(user_score)
            else:
                print("Please enter valid score.")
        elif choice == "S":
            if user_score is not None:
                show_stars(user_score)
            else:
                print("Please enter valid score.")
        elif choice == "Q":
            print("Farewell!")
            break
        else:
            print("Please enter valid option!")


def print_menu():
    print("Menu:")
    print("(G)et a valid score")
    print("(P)rint result")
    print("(S)how stars")
    print("(Q)uit")


def show_stars(score):
    print("Stars: " + "*" * int(score))


def print_result(score):
    result = grade_score(score)
    print(f"Result: {result}")


def get_valid_score():
    while True:
        try:
            score = float(input("Enter a score (0-100): "))
            if 0 <= score <= 100:
                return score
            else:
                print("score must be between 0 and 100.")
        except ValueError:
            print("Invalid input. Please enter a real number")


def grade_score(score):
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


main()
