weather = {
    "Jerusalem": 33,
    "Tel Aviv": 35,
    "Beer Sheva": 47,
    "Ako": 25,
}

city = input("Enter city: ")

if city in weather:
    print(f"In {city} temperature is {weather[city]}")
else:
    print(f"city {city} doesn't exist!")