import random

# create the data randomly
temperatures = []
for day in range(30):
    temperatures.append(random.randint(5, 27))

# print the data
print(temperatures)

# find the coldest and warmest days
coldest = temperatures[0]
warmest = temperatures[0]

for temp in temperatures:
    if temp < coldest:
        coldest = temp
    if temp > warmest:
        warmest = temp

# print the results
print(f"Warmest is {warmest}, coldest is {coldest}")
