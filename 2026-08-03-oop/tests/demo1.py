import random

from core.cars import Car, print_car

car = Car(111, 2020, "Red")
car.drive(random.randint(20, 100))
print_car(car)
