import requests
import json

latitude = "59.4370"
longitude = "24.7535"
url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&hourly=temperature_2m"

response = requests.get(url)
data = response.json()

times = data["hourly"]["time"]
temperatures = data["hourly"]["temperature_2m"]

print(f"Ilmaennustused alates {times[0]} kuni {times[-1]}\n")

for i in range(len(times)):
    print(f"{times[i]} {temperatures[i]}C")
