from unreliable_car import UnreliableCar

car_one = UnreliableCar("Toyota", 200, 3)
car_two = UnreliableCar("BMW", 200, 94)
car_one.random_reliability(50)
car_two.random_reliability(50)
print(car_one)
print(car_two)
