import random

target_val = random.randint(0, 10)
print(f"The number is {target_val}")

guess = random.randint(0, 10)
guess_counter = 1
while guess != target_val:
    print(f"Wring guess: {guess}")
    guess = random.randint(0, 10)
    guess_counter += 1

print(f"Success, guess is {guess}. you had {guess_counter} trials")