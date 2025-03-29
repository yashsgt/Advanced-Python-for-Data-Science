import os
import requests
import pyttsx3

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Prompt the user for city input
city = input("Enter the name of the city: ")

# Your WeatherAPI key (replace with your actual API key)
api_key = "b13989793f184149a91141538230103"

# Build the API URL
url = f"https://api.weatherapi.com/v1/current.json?key={api_key}&q={city}"

try:
    # Fetch the weather data
    response = requests.get(url)
    response.raise_for_status()  # Check for HTTP request errors
    weather_data = response.json()  # Convert response to JSON

    # Extract the temperature in Celsius
    temp_c = weather_data["current"]["temp_c"]

    # Print and say the weather information
    print(f"The current weather in {city} is {temp_c} degrees Celsius.")
    engine.say(f"The current weather in {city} is {temp_c} degrees Celsius.")
    engine.runAndWait()

except requests.exceptions.RequestException as e:
    print(f"Error fetching data: {e}")
except KeyError:
    print("Error: Could not retrieve weather information. Please check the city name.")