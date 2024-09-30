def main():
    number_of_items = get_valid_number(9999999, 0, "Number of items: ")
    total_price = 0
    for i in range(number_of_items):
        price = float(input(f"Price of item {i+1}: "))
        total_price += price
    print(f"Total price for {number_of_items} items is {total_price}")


def get_valid_number(upper_limit, lower_limit, prompt):
    number = int(input(prompt))
    while (number) < lower_limit or (number) > upper_limit:
        print(f"{number} is not a valid number. Try again.")
        number = int(input(prompt))
    return number
main()