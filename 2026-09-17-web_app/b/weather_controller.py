from flask import Flask, jsonify
from weather_service import get_weather, CityNotFoundError

# Flask object for configuring paths and run the app
app = Flask(__name__)


@app.get("/api/weather/<city>")
def get_weather_endpoint(city):
    try:
        weather_data = get_weather(city)
        # return str(weather_data["temp"])
        return jsonify(weather_data)
    except CityNotFoundError as e:
        # return str(e), 404
        return jsonify({"error": str(e)}), 404

app.run(debug=True)
