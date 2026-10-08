# this is core class definition. From it we can create objects
class Car:
    # init runs one - when we create the Car object
    def __init__(self, number: int, year: int, color: str):
        self.number = number
        self.year = year
        self.color = color
        self.speed = 0

    # regular methods can run many times
    def drive(self, speed: int):
        if 1 <= speed <= 200:
            self.speed = speed

    def stop(self):
        self.speed = 0


# define a convenience function for printing cars
def print_car(car: Car):
    print(f"Car number={car.number}, year={car.year}, color={car.color}, speed={car.speed}")
