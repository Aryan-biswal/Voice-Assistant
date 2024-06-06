import requests


def get_weather(city):
    api_key = "opeanweather api key"
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = base_url + "q=" + city + "&appid=" + api_key
    response = requests.get(complete_url)
    data = response.json()

    if data["cod"] != "404":
        main = data["main"]
        weather = data["weather"][0]["description"]
        temperature = main["temp"]
        temp_celsius = temperature - 273.15
        return f"The weather in {city} is {weather} with a temperature of {temp_celsius:.2f}°C."
    else:
        return "City not found."
