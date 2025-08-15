import json
import requests


response = requests.get("https://jsonplaceholder.typicode.com/users/1")

person = {"name":"alice", "age" : 30}
json_string = json.dumps(person)
print(json_string)

# data = {"name" : "bob", "age" : 25}
# person_dict = json.loads(data)
# print(f'Nome {person_dict["name"]}')

data = response.json()
print(f"nome: {data['name']}")
print(f"Email: {data['email']}")

def get_weather():
    city = input("Enter your city: ")
    print(f"Fetching weather for {city}...")

    weather_data = {
        "Delhi" : {"temp":"32•c", "condition":"Sunny"},
        "Mumbai": {"temp":"28•", "condition":"Rainy"},
    }

    if city in weather_data:
        info = weather_data[city]
        print(f"Temperature: {info['temp']}, Condition: {info['condition']}")
    else:
        print("Sorry, no data available.")


get_weather()

