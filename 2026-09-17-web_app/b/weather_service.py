# DATA LAYER
# sample data (in=memory)
weather = [
    {"city": "Tel Aviv", "temp": 28},
    {"city": "Jerusalem", "temp": 19},
    {"city": "Yerucham", "temp": 35},
    {"city": "Haifa", "temp": 25},
]


# APPLICATION LAYER
# errors
class CityNotFoundError(Exception): pass


def get_weather(city):
    for w in weather:
        if w["city"] == city:
            return w
    raise CityNotFoundError(f"Weather for city {city} not found")


if __name__ == "__main__":
    try:
        print(get_weather(input("Enter City: ")))
    except CityNotFoundError as e:
        print(e)
