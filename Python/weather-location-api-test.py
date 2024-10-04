import requests
import json
from datetime import datetime

my_API_key = "(hidden)"

def get_weather(city):
    response = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={my_API_key}')
    return response.json()

def main():
    city = input("Enter city: ")
    details = get_weather(city)

    if details.get('cod') != 200:
        print("Error:", details.get('message', 'Could not retrieve weather data.'))
        return

    # Print table header
    print("Weather Details:")
    print("-----------------")
    print("City:", details['name'])
    print("Country:", details['sys']['country'])

    # Convert temperatures from Kelvin to Celsius
    temperature = details['main']['temp'] - 273.15
    feels_like = details['main']['feels_like'] - 273.15
    print(f"Temperature: {temperature:.2f} °C")
    print(f"Feels Like: {feels_like:.2f} °C")
    print("Humidity:", details['main']['humidity'], "%")
    print("Description:", details['weather'][0]['description'])
    print("Wind Speed:", details['wind']['speed'], "m/s")
    print("Cloudiness:", details['clouds']['all'], "%")

    # Convert sunrise and sunset from Unix timestamp to readable format
    sunrise = datetime.fromtimestamp(details['sys']['sunrise']).strftime('%Y-%m-%d %H:%M:%S')
    sunset = datetime.fromtimestamp(details['sys']['sunset']).strftime('%Y-%m-%d %H:%M:%S')
    print("Sunrise:", sunrise)
    print("Sunset:", sunset)
    print("-----------------")
    

if __name__ == "__main__":
    main()
