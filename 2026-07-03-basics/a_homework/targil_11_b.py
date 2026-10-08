number = float(input("Enter a number: "))
# 1. remove the decimal part
number = int(number)
# print(number)
# 2. add 1 to the number
number = number + 1
# print(number)
# 3. add 1 if necessary (when odd)
number = number + number % 2
print(number)
