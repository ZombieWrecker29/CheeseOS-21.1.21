import json
with open("data_file.json", "r") as read_file:
    datar = json.load(read_file)
print("Welcome to the CheeseOS Recovory Utility!")
print("What would you like to do?")
print("1. Change Password")
print("2. Factory Reset")
print("3. Exit Recovory Utility")
action = input()
if action == "1":
    curpassword = (datar['userdata']['password'])
    print("Enter current password:")
    passat = input()
    if passat == curpassword:
        print("What would you like your new password to be?")
    else:
        print("Wrong password. Try again.")
        import importlib
        import recovory
        importlib.reload(recovory)
        import recovory
    import json
    newpassword = input()
    dataw = {
        "userdata": {
            "username": datar['userdata']['username'],
            "password": newpassword,
            "setupcomplete": 1
        }
    }
    with open("data_file.json", "w") as write_file:
        json.dump(dataw, write_file)
    import importlib
    import login
    importlib.reload(login)
    import login
elif action == "2":
    curpassword = (datar['userdata']['password'])
    print("Enter current password:")
    passat = input()
    if passat == curpassword:
        import importlib
        import setup
        importlib.reload(setup)
        import setup
    else:
        print("Wrong password. Try again.")
        import importlib
        import recovory
        importlib.reload(recovory)
        import recovory
elif action == "3":
    import importlib
    import desktop
    importlib.reload(desktop)
    import desktop
else:
    import importlib
    import recovory
    importlib.reload(recovory)
    import recovory