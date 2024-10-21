"""
CP1404/CP5632 Practical
State names in a dictionary
File needs reformatting
"""


CODE_TO_NAME = {"QLD": "Queensland", "NSW": "New South Wales", "NT": "Northern Territory", "WA": "Western Australia",
                "ACT": "Australian Capital Territory", "VIC": "Victoria", "TAS": "Tasmania", "SA": "South Australia"}
for code in CODE_TO_NAME:
    print(f"{code:<3} is {CODE_TO_NAME[code]}")


# state_code = input("Enter short state: ").upper()
# while state_code != "":
#     if state_code in CODE_TO_NAME:
#         print(state_code, "is", CODE_TO_NAME[state_code])
#     else:
#         print("Invalid short state")
#     state_code = input("Enter short state: ").upper()
#
state_code = input("Enter a short state: ").upper()
try:
    print(state_code, "is", CODE_TO_NAME[state_code])
except KeyError:
    print("Invalid short state")
    state_code = input("Enter a short state: ").upper()


