print("Welcome to the CheeseOS Launchpad. This is a Beta version of the Application and only works on macOS.")
print("Type the Full Name of the Application you would like to open. For example, if you would like to open Zoom, you would need to type 'zoom.us'")
print("You can type 'exit' to exit Launchpad.")
application = input()
if application == "exit":
    import desktop
    import importlib
    importlib.reload(desktop)
    import desktop
import os
os.system("open /Applications/" + application + ".app")