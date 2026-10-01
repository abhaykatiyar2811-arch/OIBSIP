"""Basic Weather App - Beginner Tier (Command-Line Version).

Asks the user for a city name or ZIP code, calls the OpenWeatherMap
current-weather API, parses the JSON response and prints the temperature
(in Celsius and Fahrenheit), condition, humidity and wind speed.

The API key is never stored in this file. It is read from the
OPENWEATHER_API_KEY environment variable.
"""

import json
import os

import requests

# OpenWeatherMap "Current Weather" endpoint.
API_URL = "https://api.openweathermap.org/data/2.5/weather"

# Name of the environment variable that holds the personal API key.
API_KEY_ENV_VAR = "OPENWEATHER_API_KEY"

# The app gives up on a slow request after this many seconds
# instead of hanging forever.
REQUEST_TIMEOUT = 10


class WeatherAppError(Exception):
    """A problem we can explain to the user in a friendly way.

    Raising this instead of letting a raw requests/JSON error escape
    keeps tracebacks out of normal program output.
    """


def get_api_key():
    """Return the OpenWeatherMap API key, or None if it is not configured.

    The key is read from an environment variable so that no secret ever
    has to be written inside this source file.
    """
    # ("" if the variable is missing) then .strip() removes stray spaces,
    # so a blank value is treated the same as a missing one.
    api_key = (os.getenv(API_KEY_ENV_VAR) or "").strip()

    if api_key:
        return api_key

    return None


def get_location():
    """Ask for a city name or ZIP code and keep asking until one is given.

    Empty input and whitespace-only input are both rejected.
    """
    while True:
        # .strip() removes spaces, so "   " is treated as empty input.
        location = input("Enter city name or ZIP code: ").strip()

        if not location:
            print("Invalid input. Please enter a city name or ZIP code.")
        else:
            return location


def celsius_to_fahrenheit(celsius):
    """Convert degrees Celsius to degrees Fahrenheit."""
    return (celsius * 9 / 5) + 32


def fetch_weather(location, api_key):
    """Request the current weather for a location and return the JSON data.

    Any problem is converted into a WeatherAppError that carries a message
    the user can understand. The API key is never included in that message.
    """
    # requests builds the query string and escapes the location for us.
    params = {
        "q": location,      # city name or ZIP/postal code
        "appid": api_key,   # personal API key
        "units": "metric",  # report temperature in Celsius, wind in m/s
    }

    try:
        response = requests.get(API_URL, params=params, timeout=REQUEST_TIMEOUT)
    except requests.exceptions.Timeout:
        raise WeatherAppError(
            "The weather service took too long to respond. Please try again later."
        )
    except requests.exceptions.ConnectionError:
        raise WeatherAppError(
            "Unable to connect to the weather service. "
            "Please check your internet connection."
        )
    except requests.exceptions.RequestException:
        raise WeatherAppError(
            "Unable to connect to the weather service. "
            "Please check your internet connection."
        )

    # Turn HTTP status codes into friendly messages.
    if response.status_code == 404:
        raise WeatherAppError(
            "Location not found. Please check the city name or ZIP code and try again."
        )

    if response.status_code in (401, 403):
        raise WeatherAppError(
            "Invalid API key. Please check your OpenWeatherMap API key."
        )

    if response.status_code == 429:
        raise WeatherAppError(
            "Too many requests were sent to the weather service. Please wait a moment."
        )

    if response.status_code >= 500:
        raise WeatherAppError(
            "Weather service is temporarily unavailable. Please try again later."
        )

    if not response.ok:
        raise WeatherAppError(
            "Unable to read weather information. Please try again later."
        )

    # Convert the response body (a JSON string) into a Python dictionary.
    try:
        return json.loads(response.text)
    except ValueError:
        raise WeatherAppError(
            "Unable to read weather information. Please try again later."
        )


def extract_weather(data):
    """Pull the values we need out of the JSON response.

    Raises WeatherAppError if anything expected is missing, so an
    unexpected response cannot crash the program.
    """
    try:
        temperature_c = float(data["main"]["temp"])
        humidity = float(data["main"]["humidity"])
        condition = str(data["weather"][0]["description"])
        wind_speed = float(data["wind"]["speed"])
        location_name = str(data.get("name") or "Unknown")
        country_code = str(data.get("sys", {}).get("country") or "")
    except (AttributeError, IndexError, KeyError, TypeError, ValueError):
        raise WeatherAppError(
            "Unable to read weather information. Please try again later."
        )

    return {
        "location": location_name,
        "country": country_code,
        "temperature_c": temperature_c,
        "humidity": humidity,
        "condition": condition,
        "wind_speed": wind_speed,
    }


def display_weather(weather):
    """Print the weather information in a clean, aligned layout."""
    # Show the country code too when the API provides one: "Kanpur, IN"
    location = weather["location"]
    if weather["country"]:
        location = "{}, {}".format(location, weather["country"])

    # Turn "partly cloudy" into "Partly Cloudy" for a neater display.
    condition = weather["condition"].strip().title()

    temperature_c = round(weather["temperature_c"], 1)
    temperature_f = round(celsius_to_fahrenheit(weather["temperature_c"]), 1)

    print("----------------------------------------")
    print("Weather Information")
    print("----------------------------------------")
    print()
    print("Location      : {}".format(location))
    print("Temperature   : {:.1f}°C / {:.1f}°F".format(temperature_c, temperature_f))
    print("Condition     : {}".format(condition))
    print("Humidity      : {:.0f}%".format(weather["humidity"]))
    print("Wind Speed    : {:.1f} m/s".format(weather["wind_speed"]))
    print()
    print("----------------------------------------")
    print()


def ask_another_location():
    """Ask whether to search again. Returns True for yes, False for no."""
    question = "Do you want to check another location? (y/n): "

    while True:
        # .strip().lower() lets the user type " Y " or "N".
        answer = input(question).strip().lower()

        if answer in ("y", "yes"):
            return True

        if answer in ("n", "no"):
            return False

        print("Invalid input. Please enter 'y' or 'n'.")


def main():
    """Run the weather app until the user chooses to exit."""
    print("========================================")
    print("          BASIC WEATHER APP")
    print("========================================")
    print()

    api_key = get_api_key()

    if api_key is None:
        # Stop early with setup help instead of failing later with a 401.
        print("OpenWeatherMap API key is not configured.")
        print("Please set the OPENWEATHER_API_KEY environment variable.")
        print("See README.md for step-by-step setup instructions.")
        return

    while True:
        location = get_location()

        print()
        print("Fetching weather data...")
        print()

        try:
            data = fetch_weather(location, api_key)
            weather = extract_weather(data)
        except WeatherAppError as error:
            print(str(error))
        else:
            display_weather(weather)

        if not ask_another_location():
            break

    print()
    print("Thank you for using the Basic Weather App!")


if __name__ == "__main__":
    # Ctrl+C or Ctrl+Z should still end the program politely.
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print()
        print("Thank you for using the Basic Weather App!")