import random

temperatures = [random.randint(5, 27)]
coldest = temperatures[0]
warmest = temperatures[0]

for day in range(29):
    temp = random.randint(5, 27)
    temperatures.append(temp)
    if temp < coldest:
        coldest = temp
    if temp > warmest:
        warmest = temp

# print the data
print(temperatures)

# print the results
print(f"Warmest is {warmest}, coldest is {coldest}")
