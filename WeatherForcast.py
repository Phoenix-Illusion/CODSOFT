import requests

def get_weather_data(api_key, location):
    # Construct the API URL with the API key and user's location input
    url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=metric"

    # Make an API request
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print("Error fetching data from the API.")
        return None

def display_weather(data):
    if data:
        # Extract relevant weather information
        temperature = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        description = data["weather"][0]["description"]

        # Display the weather information
        print(f"Temperature: {temperature}°C")
        print(f"Humidity: {humidity}%")
        print(f"Description: {description.capitalize()}")
    else:
        print("No weather data available.")

def main():
    # Get the user's API key and location input
    api_key = input("Enter your OpenWeatherMap API key: ")
    location = input("Enter a city name or zip code: ")

    # Get weather data from the API
    weather_data = get_weather_data(api_key, location)

    # Display the weather information
    display_weather(weather_data)

if __name__ == "__main__":
    main()
