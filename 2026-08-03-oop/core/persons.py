# this is super class
class Person:
    def __init__(self, p_id: int, name: str, age: int):
        self.p_id = p_id
        self.name = name
        self.age = age

    def speak(self):
        print(f"{self.name} is now speaking")

    def __str__(self):
        return f"Person[id={self.p_id}, name={self.name}, age={self.age}]"

# this is sub class (inherits from the super class above)
class Employee(Person):
    def __init__(self, p_id: int, name: str, age: int,  salary: float):
        super().__init__(p_id, name, age)
        self.salary = salary
