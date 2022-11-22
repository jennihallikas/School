# Ex 12 part 1
import requests
import json

request = "https://api.chucknorris.io/jokes/random"
try:
    response = requests.get(request)
    if response.status_code==200:
        json_response = response.json()
        print(json_response['value'])

except requests.exceptions.RequestException as e:
    print("Request could not be completed.")


# 2
municipality= input("Write the name of the municipality: ")
key = "775da9134e40aa434e6d0656a7b27954"
request = "https://api.openweathermap.org/data/2.5/weather?q=" + municipality + "&appid=" + key + "&units=metric"

try:
    response = requests.get(request)
    response_data = response.json()
    print(f"The weather in {municipality} is {response_data['weather']} and the temperature is {response_data['main']['temp']} c degrees")

except requests.exceptions.RequestException as e:
    print("Request could not be completed.")

