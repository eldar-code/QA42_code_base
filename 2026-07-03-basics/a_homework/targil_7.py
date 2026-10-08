# input a number and display third digit from right
number = int(input("Enter an Integer of 4 digits: "))
print((number // 100) % 10)
print(f"3rd digit from right of {number} is {(number // 100) % 10}")
