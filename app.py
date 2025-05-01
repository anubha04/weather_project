import os
import requests
from flask import Flask, render_template, request
from dotenv import load_dotenv

# Load API key from .env file
load_dotenv()
API_KEY = os.getenv("WEATHER_API_KEY")

app = Flask(__name__)

def get_weather(city):
    """Fetches weather data from OpenWeather API and handles errors."""
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    data = response.json()
    
    # 🔹 Debugging: Print the API response to check if it's correct
    print("API Response:", data)

    if response.status_code != 200:
        return None  # Return None if API request fails

    return data

@app.route("/", methods=["GET", "POST"])
def index():
    weather_data = None
    error_message = None

    if request.method == "POST":
        city = request.form.get("city")
        weather_data = get_weather(city)

        if weather_data is None:
            error_message = "City not found. Please enter a valid city name."

    return render_template("index.html", weather=weather_data, error=error_message)

if __name__ == "__main__":
    app.run(debug=True)
