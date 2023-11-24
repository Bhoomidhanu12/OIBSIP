import urllib.request
import json

def get_weather(api_key, location):
    base_url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}"
    
    try:
        with urllib.request.urlopen(base_url) as response:
            data = response.read()
            weather_info = json.loads(data)
            return weather_info
    except urllib.error.HTTPError as e:
        print(f"Error: {e.code} - {e.reason}")
        return None
    except urllib.error.URLError as e:
        print(f"Error: {e.reason}")
        return None

def display_weather(weather_data):
    if weather_data is not None:
        temperature = weather_data["main"]["temp"]
        humidity = weather_data["main"]["humidity"]
        description = weather_data["weather"][0]["description"]

        print(f"Temperature: {temperature} K")
        print(f"Humidity: {humidity}%")
        print(f"Description: {description}")
    else:
        print("Unable to fetch weather data.")

def main():
    api_key = "85e7e651d48b32a3acac5f9fb9524941"  # Replace with your API key
    location = input("Enter city or ZIP code: ")

    weather_data = get_weather(api_key, location)
    display_weather(weather_data)

if __name__ == "__main__":
    main()
