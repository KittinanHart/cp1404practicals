"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

import random


def main():
    score = float(input("Enter score: "))
    result = grade_score(score)
    print("Result:", result)

    random_score = random.randint(0, 100)
    random_result = grade_score(random_score)
    print(f"Random score: {random_score}")
    print("Random result:", random_result)


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
