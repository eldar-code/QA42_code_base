import random

grade = random.randint(-50, 150)
print(f"grade is {grade}")

# 0 - 60 Fail
# 61 - 70 Pass
# 71 - 90 Good
# 91 - 100 Excellent
# any other value is out of range and is illegal
if 0 <= grade <= 60:
    print("Fail")
elif 61 <= grade <= 70:
    print("Pass")
elif 71 <= grade <= 90:
    print("Good")
elif 91 <= grade <= 100:
    print("Excellent")
else:
    print(f"{grade} is out of range!")
