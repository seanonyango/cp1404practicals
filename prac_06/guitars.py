from guitar import Guitar

print("My Guitars!")
my_guitars = []
name = input("Name: ")
while not name == "":
    year = int(input("Year: "))
    cost = float(input("Cost: "))
    guitar = Guitar(name, year, cost)
    my_guitars.append(guitar)
    print(f"{guitar} added")
    name = input("Name: ")
print("These are my guitars:")

for i, guitar in enumerate(my_guitars):
    print(f" Guitar {i + 1}: {guitar}")
