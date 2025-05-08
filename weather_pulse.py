import requests
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv('API_KEY')

def get_weather(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        temp = data['main']['temp']
        description = data['weather'][0]['description']
        humidity = data['main']['humidity']
        wind_speed = data['wind']['speed']
        
        print(f"\nWeather in {city}:")
        print(f"Temperature: {temp}°C")
        print(f"Condition: {description}")
        print(f"Humidity: {humidity}%")
        print(f"Wind Speed: {wind_speed} m/s")
    else:
        print("City not found. Please check the name.")

def main():
    print("Welcome to the Weather App")
    city = input("Enter a city name: ")
    get_weather(city)

if __name__ == "__main__":
    main()
