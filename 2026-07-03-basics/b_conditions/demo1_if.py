import random

grade = random.randint(30, 100)
print(f"grade is {grade}")

# pass or fail. pass is 60
if grade >= 60:
    print("Pass")
else:
    print("Fail")

