print("Welcome to the CheeseOS File Explorer!")
print("What would you like to do?")
print("1. Create a file")
print("2. Open a file")
print("3. Exit CheeseOS File Explorer")
action1 = input()
if action1 == "1":
    print("What is the name of the file you would like to create?")
    filename = input()
    print("What data would you like to keep in " + filename + "?")
    filedata = input()
    print("Creating file...")
    import json
    fileit = {
        filename: {
            "data": filedata
        }
    }
    with open(filename + "_userdata.json", "w") as write_file:
        json.dump(fileit, write_file)
    print("Created file.")
    import importlib
    import files
    importlib.reload(files)
    import files
elif action1 == "2":
    print("Please keep the name of the file you would like to open.")
    openfile = input()
    print("Opening " + openfile + "...")
    import json
    with open(openfile + "_userdata.json", "r") as read_file:
        filedataforsale = json.load(read_file)
    print(openfile + ":")
    print(filedataforsale[openfile]["data"])
    print("What would you like to do?")
    print("1. Modify File")
    print("2. Exit File")
    action2 = input()
    if action2 == "1":
        print("What would you like to change the file too?")
        overwrite_data = input()
        overwite_table = {
            openfile: {
                "data": overwrite_data
            }
        }
        with open(openfile + "_userdata.json", "w") as write_file:
            json.dump(overwite_table, write_file)
        print("File updated.")
    elif action2 == "2":
        import importlib
        import desktop
        importlib.reload(desktop)
        import desktop
    else:
        print("Sorry, I didn't understand that.")
    import importlib
    import files
    importlib.reload(files)
    import files
elif action1 == "3":
    import importlib
    import desktop
    importlib.reload(desktop)
    import desktop
else:
    import importlib
    import files
    importlib.reload(files)
    import files