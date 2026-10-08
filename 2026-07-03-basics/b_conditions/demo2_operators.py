n = 10

print(n < 100)
print(n > 100)
print(n < 10)
print(n <= 10)
print(n > 10)
print(n >= 10)
print(n != 10)
print(n != 30)
print("=" * 50)
print(True)
print(False)
print("=" * 50)
print(not True)
print(not False)
print("=" * 50)

age = int(input("Enter age: "))
print(f"age is {age}")
# legal age is 18 - 120
if not (18 <= age <= 120):
    print("Not Legal")
