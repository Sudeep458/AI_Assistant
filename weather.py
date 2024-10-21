import requests
import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

class Weather:
    def __init__(self):
        self.api_key = os.getenv('WEATHER_API_KEY')  # Get API key from environment variable
        self.url = 'https://api.openweathermap.org/data/2.5/weather'

    def get_weather(self, city):
        """Fetch weather data for the specified city."""
        parameters = {
            'q': city,
            'appid': self.api_key,
            'units': 'metric'  # Use 'imperial' for Fahrenheit
        }
        response = requests.get(self.url, params=parameters)
        
        if response.status_code == 200:
            data = response.json()
            return data
        else:
            print("Failed to fetch weather data:", response.status_code)
            return None

    def create_weather_html(self, weather_data):
        """Create an HTML file to display the fetched weather information."""
        if not weather_data:
            return
        
        city = weather_data['name']
        temp = weather_data['main']['temp']
        description = weather_data['weather'][0]['description']
        
        html_content = f"""
        <html>
        <head><title>Weather in {city}</title></head>
        <body>
            <h1>Weather in {city}</h1>
            <p>Temperature: {temp} °C</p>
            <p>Description: {description}</p>
        </body>
        </html>
        """
        
        # Write the HTML content to a file
        with open("weather_info.html", "w") as file:
            file.write(html_content)