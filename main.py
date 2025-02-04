import requests
import json

latitude = "59.4370"
longitude = "24.7535"
url = f"https://api.met.no/weatherapi/locationforecast/2.0/compact?lat={latitude}&lon={longitude}"

headers = {
    "User": "WeatherApp"
}

response = requests.get(url, headers=headers)
data = response.json()

first_time = data["properties"]["timeseries"][0]["time"]
last_time = data["properties"]["timeseries"][-1]["time"]
print(f"Ilmaennustused alates {first_time} kuni {last_time}\n")

for timeseries in data["properties"]["timeseries"]:
    time = timeseries["time"]
    temperature = timeseries["data"]["instant"]["details"]["air_temperature"]
    print(f"{time} {temperature}C")
