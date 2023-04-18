import requests

url = "http://127.0.0.1:8000/predict"

data = {
    "MedInc": 8.3252,
    "HouseAge": 41.0,
    "AveRooms": 6.98412698,
    "AveBedrms": 1.02380952,
    "Population": 322.0,
    "AveOccup": 2.55555556,
    "Latitude": 37.88,
    "Longitude": -122.23
}

response = requests.post(url, json=data)

print(response.json())
