# this is the code I DO NOT want to test
import requests


def get_weather(city):
    # print("\nCall an outside weather API...[do not test this one]")  # a fake call to some REST API
    # return {"city": city, "temp": 25}
    response = requests.get(f"https://api.weather.com/{city}")
    return response.json()
