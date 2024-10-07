out_file = open("name.txt", "w")
name = input("Enter your name: ")
print(name, file=out_file)
out_file.close()

in_file = open("name.txt", "r")
name = in_file.read().strip()
print(f"Hi {name}!")
in_file.close()

with open("numbers.txt","r") as file:
    sum_of_numbers = 0
    for i in range(2):
        sum_of_numbers += int(file.readline().strip())
    print(f"The result of the first two numbers is {sum_of_numbers}")

with open("numbers.txt", "r") as file:
    sum_of_all_numbers = 0
    for line in file:
        sum_of_all_numbers = sum_of_all_numbers + int(line)
    print(f"The sum of the numbers is {sum_of_all_numbers}")
