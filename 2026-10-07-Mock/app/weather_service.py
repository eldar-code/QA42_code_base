# this is the code I DO want to test
import app.api_client as api

def get_city_temp(city):
    data = api.get_weather(city)
    return data["temp"]

