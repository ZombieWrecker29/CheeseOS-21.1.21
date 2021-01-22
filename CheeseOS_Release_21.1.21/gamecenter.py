import turtle
turtle.clearscreen()
import json
with open("gamecenter_data.json", "r") as read_file:
  datar = json.load(read_file)
print("Welcome to CheeseOS Game Center! Please select a game from the list below!")
print("1. Pong by Arnav")
print("Played " + str(datar['plays']['pong']) + " times.")
print("2. Drawing Game by Arnav")
print("Played " + str(datar['plays']['draw']) + " times.")
print("3. Exit Game Center")
game = input()
if game == "1":
  (datar['plays']['pong']) += 1
  with open("gamecenter_data.json", "w") as write_file:
    json.dump(datar, write_file)
  import importlib
  import pong
  importlib.reload(pong)
  import pong
elif game == "2":
  (datar['plays']['draw']) += 1
  with open("gamecenter_data.json", "w") as write_file:
    json.dump(datar, write_file)
  import importlib
  import draw
  importlib.reload(draw)
  import draw
elif game =="3":
  import importlib
  import desktop
  importlib.reload(desktop)
  import desktop
else:
  import importlib
  import gamecenter
  importlib.reload(gamecenter)
  import gamecenter