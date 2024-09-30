"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

import random


def main():
    score = float(input("Enter score: "))
    result = determine_score_result(score)
    print(f"Your score of {score} is {result}")
    random_score = random.randint(1, 101)
    random_result = determine_score_result(random_score)
    print(f"A  score of {random_score} is {random_result}")


def determine_score_result(score):
    if score < 0 or score > 100:
        result = "Invalid score"
    elif score <= 50:
        result = "Bad"
    elif score <= 90:
        result = "Passable"
    elif score > 90:
        result = "Excellent"
    return result


main()
