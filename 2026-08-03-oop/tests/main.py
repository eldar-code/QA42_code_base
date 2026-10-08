# import the Car class
from core.cars import Car, print_car

# create Car objects
car1 = Car(111, 1980, "RED")
car2 = Car(222, 2020, "GREEN")
car3 = Car(333, 2026, "BLUE")





# print the state of each Car object
print_car(car1)
print_car(car2)
print_car(car3)
print("=" * 60)
car1.drive(80)
print_car(car1)
car1.drive(35)
print_car(car1)
car1.stop()
print_car(car1)

