import requests

parameters = {
    "lat": "36.7201600",
    "lng": "-4.4203400",
    "formatted": "0",
}

response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters, verify=False)
response.raise_for_status()
data = response.json()

print(data)
sunrise_time = data["results"]["sunrise"]
print(sunrise_time)
