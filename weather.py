import os
import requests


OWM_Endpoint = "https://api.openweathermap.org/data/2.5/weather"
api_key = "weather_api_key"

def weather_api(city):
    request_url = f"{OWM_Endpoint}?q={city}&appid={api_key}"
    response = requests.get(request_url)
    print(response.status_code)

    if response.status_code == 200:
        data = response.json()
        weather = data['weather'][0]['description']
        print("The weather is currently", weather)
        temperature = round(1.8 * (data['main']['temp'] - 273) + 32, 2)
        print("The temperature is:", temperature, "fahrenheit")

        return f"The weather is currently {weather} and the temperature is {temperature} fahrenheit"
    else:
        print("An error has occurred.")





