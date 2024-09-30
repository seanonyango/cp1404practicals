def main():
    password = get_password()
    print_asterisks(password)


def print_asterisks(password):
    print("*" * len(password))


def get_password():
    minimum_password_length = int(input('Enter minimum password length: '))
    password = input("Enter your password: ")
    while len(password) < minimum_password_length:
        print('Password must be at least ', minimum_password_length, "characters")
        password = input("Enter your password: ")
    return password


main()
