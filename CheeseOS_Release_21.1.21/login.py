import json
with open("data_file.json", "r") as read_file:
  data = json.load(read_file)
username = (data['userdata']['username'])
password = (data['userdata']['password'])
print(username + ", please enter your password:")
passat = input()
if passat == password:
  print("Access granted.")
  import importlib
  import desktop
  importlib.reload(desktop)
  import desktop
else:
  print("Wrong password. Try again.")
  import importlib
  import login
  importlib.reload(login)
  import login