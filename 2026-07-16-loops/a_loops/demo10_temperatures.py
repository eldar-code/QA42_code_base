import random

# create the data randomly
temperatures = []
for day in range(30):
    temperatures.append(random.randint(5, 27))

# print the data
print(temperatures)

# find the coldest and warmest days
coldest = temperatures[0]
coldest_day = 1
warmest = temperatures[0]
warmest_day = 1

current_day = 1
for temp in temperatures:
    if temp < coldest:
        coldest = temp
        coldest_day = current_day
    if temp > warmest:
        warmest = temp
        warmest_day = current_day
    current_day += 1

# print the results
print(f"Warmest is {warmest} ({warmest_day}), coldest is {coldest} ({coldest_day})")
