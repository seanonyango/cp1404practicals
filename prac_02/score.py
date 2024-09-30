"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

import random


def main():
    score = get_valid_score()
    result = determine_score_result(score)
    print(f"Your score of {score} is {result}")
    random_score = random.randint(1, 101)
    random_result = determine_score_result(random_score)
    print(f"A  score of {random_score} is {random_result}")


def get_valid_score():
    score = float(input("Enter score: "))
    while score < 0 or score > 100:
        print("Score must be between 0 and 100")
        score = float(input("Enter score: "))
    return score


def determine_score_result(score):
    if score <= 50:
        result = "Bad"
    elif score <= 90:
        result = "Passable"
    elif score > 90:
        result = "Excellent"
    return result


if __name__ == "__main__":
    main()
