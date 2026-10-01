# Basic Weather App (Python Task 4 - Beginner Tier)

A simple command-line weather application written in Python 3. It asks for a
city name or ZIP code, calls the OpenWeatherMap API, and displays the current
weather information.

## Project Objective

The application retrieves real-time weather information for a user-specified
location using the OpenWeatherMap API. The JSON response is parsed and only the
useful details are printed: location, temperature in Celsius and Fahrenheit,
weather condition, humidity and wind speed. Invalid input, invalid API keys and
network problems are handled with clear messages instead of crashing.

## Features

- Accepts a city name (for example `Kanpur`, `London`, `New York`).
- Accepts a ZIP/postal code (for example `208001`).
- Fetches real-time weather data from the OpenWeatherMap API.
- Shows the current temperature in Celsius.
- Shows the current temperature in Fahrenheit, converted with `°F = (°C × 9/5) + 32`.
- Shows humidity as a percentage.
- Shows a human-readable weather condition (for example `Partly Cloudy`).
- Shows the wind speed in m/s.
- Validates input: empty input and whitespace-only input are rejected.
- Handles API errors: location not found, invalid API key, rate limit.
- Handles a network timeout and a connection failure.
- Handles unexpected or incomplete API responses safely.
- Lets the user check another location without restarting the program.
- Exits gracefully when the user answers `n`.
- Reads the API key from an environment variable, so no key is stored in code.

## Technologies

- Python
- Requests
- JSON
- OpenWeatherMap API

The only third-party dependency is `requests`.

## API Key Setup

The API key is **not** written inside `weather_app.py`. It is read from the
`OPENWEATHER_API_KEY` environment variable at runtime.

1. Go to [https://home.openweathermap.org/users/sign_up](https://home.openweathermap.org/users/sign_up)
   and create a free OpenWeatherMap account.
2. Sign in and open the **API keys** section
   ([https://home.openweathermap.org/api_keys](https://home.openweathermap.org/api_keys)).
   Generate a new key and copy it. New keys can take a short while to activate.
3. Set the `OPENWEATHER_API_KEY` environment variable on your machine using one
   of the commands below (replace `YOUR_API_KEY_HERE` with your own key).
4. Do not commit the API key to GitHub.

### Windows (Command Prompt)

```bat
set OPENWEATHER_API_KEY=YOUR_API_KEY_HERE
python weather_app.py
```

### Windows PowerShell

```powershell
$env:OPENWEATHER_API_KEY = "YOUR_API_KEY_HERE"
python weather_app.py
```

### macOS / Linux

```bash
export OPENWEATHER_API_KEY="YOUR_API_KEY_HERE"
python weather_app.py
```

To make the variable permanent on macOS/Linux, add the `export` line to your
shell profile (`~/.bashrc`, `~/.zshrc`).

If the variable is missing, the app stops with this message instead of failing
with a confusing error:

```text
OpenWeatherMap API key is not configured.
Please set the OPENWEATHER_API_KEY environment variable.
```

## Installation

Python 3 is required. Open a terminal in the project directory
(`OIBSIP/Python-Task4-BasicWeatherApp`) and install the dependency:

```bash
pip install requests
```

## Running the Application

```bash
python weather_app.py
```

On some systems the command may be:

```bash
python3 weather_app.py
```

## Example Output

The values below are only an example. The real numbers come from the live API
and will be different every time you run the program.

```text
========================================
          BASIC WEATHER APP
========================================

Enter city name or ZIP code: Kanpur

Fetching weather data...

----------------------------------------
Weather Information
----------------------------------------

Location      : Kanpur, IN
Temperature   : 28.5°C / 83.3°F
Condition     : Partly Cloudy
Humidity      : 65%
Wind Speed    : 4.2 m/s

----------------------------------------

Do you want to check another location? (y/n): n

Thank you for using the Basic Weather App!
```

## Error Handling Examples

```text
Enter city name or ZIP code:
Invalid input. Please enter a city name or ZIP code.

Enter city name or ZIP code: ThisCityDoesNotExist12345
Location not found. Please check the city name or ZIP code and try again.

Invalid API key. Please check your OpenWeatherMap API key.
The weather service took too long to respond. Please try again later.
Unable to connect to the weather service. Please check your internet connection.
Weather service is temporarily unavailable. Please try again later.
Unable to read weather information. Please try again later.
```

The API request uses a 10-second timeout, so the program never hangs waiting
for an unreachable service, and no Python traceback is shown during normal
operation.

## Project Structure

```text
OIBSIP/
└── Python-Task4-BasicWeatherApp/
    ├── weather_app.py
    ├── README.md
    └── .gitignore
```

## Code Structure

```text
get_api_key()          -> read OPENWEATHER_API_KEY from the environment
get_location()         -> validated city name or ZIP code
fetch_weather()        -> API call, returns JSON data, raises friendly errors
extract_weather()      -> pull temperature, humidity, condition, wind out of JSON
display_weather()      -> print the formatted weather information
celsius_to_fahrenheit()-> Celsius to Fahrenheit conversion
ask_another_location() -> yes/no loop control
main()                 -> program flow
```

## API Endpoint Used

```text
GET https://api.openweathermap.org/data/2.5/weather
    ?q=<city or ZIP code>
    &appid=<your API key>
    &units=metric
```

`units=metric` makes the API return the temperature in Celsius and the wind
speed in m/s, and the Fahrenheit value is calculated by this program.

## Note

This is the Beginner Tier. A Tkinter/PyQt5 GUI, weather icons, Pillow images,
hourly or 5-day forecasts, a Celsius/Fahrenheit GUI toggle, automatic IP
location detection (ipinfo.io), a database, user accounts, a login system and a
web frontend are intentionally not included.