from score import get_valid_score, determine_score_result

MENU = "G - Get valid score\nP - Print result from latest score\nS- show stars\nQ - quit"


def main():
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "G":
            number_score = get_valid_score()
        elif choice == "P":
            result = determine_score_result(number_score)
            print(f"A score of {number_score} is {result}")

        elif choice == "S":
            print("*" * int(number_score))
        else:
            print("Invalid input")
        print(MENU)
        choice = input(">>> ").upper()
    print("Farewell")


main()
