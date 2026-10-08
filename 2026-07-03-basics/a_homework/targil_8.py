# sum of digits of 2 digit number
number = int(input("Enter an Integer of 2 digits: "))
tens = number // 10
ones = number % 10
result = tens + ones
print(f"sum of 2 digits is: {result}")

