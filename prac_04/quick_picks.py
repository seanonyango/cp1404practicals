import random

NUMBERS_PER_LINE = 6
MINIMUM_NUMBER = 1
MAXIMUM_NUMBER = 45

number_of_quick_picks = int(input("How many quick picks? "))
for i in range(number_of_quick_picks):
    picks = []
    for j in range(NUMBERS_PER_LINE):
        number = (random.randint(MINIMUM_NUMBER, MAXIMUM_NUMBER))
        while number in picks:
            number = (random.randint(MINIMUM_NUMBER, MAXIMUM_NUMBER))
        picks.append(number)
    print(" ".join(f"{number:2}" for number in picks))


