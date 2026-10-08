from core.persons import Person, Employee

p1 = Person(111, "David", 25)
p2 = Person(222, "Lea", 23)

p1.speak()
p2.speak()

print(p1)
print(p2)

emp1 = Employee(333, "AAA", 35, 12000)
print(emp1)
print(emp1.salary)


