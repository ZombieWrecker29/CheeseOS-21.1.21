import json
print("Welcome to the CheeseOS setup!")
print("Choose a username:")
user = input()
print("Choose a password:")
password = input()
data = {
    "userdata": {
        "username": user,
        "password": password,
        "setupcomplete": int(1)
    }
}
with open("data_file.json", "w") as write_file:
    json.dump(data, write_file)
games = {
    "plays": {
        "pong": 0,
        "draw": 0
    }
}
with open("gamecenter_data.json", "w") as write_file:
    json.dump(games, write_file)
import importlib
import login
importlib.reload(login)
import login