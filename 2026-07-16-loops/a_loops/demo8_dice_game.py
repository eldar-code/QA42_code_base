import random

while True:
    print(random.randint(1, 6))
    user_input = input("Enter q to quite: ")
    if user_input == "q":
        break # exit the loop
print("END")
