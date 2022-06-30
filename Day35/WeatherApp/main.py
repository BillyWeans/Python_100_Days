import requests
import os
from pprint import pprint

api_key = os.environ.get("PY_WTHR_API_KEY")

weather_params = {
    "lat": 45.4772,
    "lon": -75.7016,
    "exclude": "current,minutely,daily",
    "APPID": api_key,
}

response = requests.get(url='https://api.openweathermap.org/data/2.5/onecall', params=weather_params, verify=True)
response.raise_for_status()

data = response.json()

hourly_weather = data['hourly']

need_umbrella = False

for weather in hourly_weather[:11]:
    weather_code = int((weather['weather'][0]['id']))
    #print(weather_code)
    if weather_code < 700:
        need_umbrella = True

if need_umbrella:
    print("Bring an umbrella")
else:
    print("It's a beautiful next 12 hours!!!")

#print(data)
#print(data['hourly'])
#print(f"Temp is: {data['hourly']}")
#print(response.status_code)