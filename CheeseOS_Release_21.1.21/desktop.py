print("What would you like to do/open?")
print("1. Log Out")
print("2. Game Center")
print("3. Recovory Utility")
print("4. File Explorer")
print("5. Launchpad")
app = input()
if app == "1":
  import importlib 
  import login
  importlib.reload(login)
  import login
elif app == "2":
  import importlib
  import gamecenter
  importlib.reload(gamecenter)
  import gamecenter
elif app == "3":
  import importlib
  import recovory
  importlib.reload(recovory)
  import recovory
elif app == "4":
  import importlib
  import files
  importlib.reload(files)
  import files
elif app == "5":
  import importlib
  import launchpad
  importlib.reload(launchpad)
  import launchpad
else:
  import importlib
  import desktop
  importlib.reload(desktop)
  import desktop