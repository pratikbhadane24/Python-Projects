import requests

OWM_Enpoint = "https://api.openweathermap.org/data/2.5/onecall"

api_key = "0b9eafc9b73df8a5d448528e3b09c714"
weather_params = {
    "lat": 19.075983,
    "lon": 72.877655,
    "appid": api_key,
    "exclude": "current,minutely,daily"
}

response = requests.get(url=OWM_Enpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
will_rain = False

for n in range(0, 13):
    if weather_data["hourly"][n]["weather"][0]["id"] < 700:
        will_rain = True

if will_rain:
    print("Bring Umbrella!")
