print("Welcome to CheeseOS! Please wait while the OS loads up...")
import json
with open("data_file.json", "r") as read_file:
    data = json.load(read_file)
setup = (data['userdata']['setupcomplete'])
print("This is a CheeseOS based operating system.")
if setup == 0:
    print("Files loaded. Starting setup...")
    import importlib
    import setup
    importlib.reload(setup)
    import setup
if setup == 1:
    import importlib
    import login
    importlib.reload(login)
    import login