import random
from core.cars import Car, print_car

car = Car(111, 2020, "Red")
car.drive(int(input("Enter speed: ")))
print_car(car)
