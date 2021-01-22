# Step 1
Open your Terminal or Command Prompt and enter the following commands. 'd' is the directory that you want to install CheeseOS in.
  cd d
  git clone https://github.com/ZombieWrecker29/CheeseOS-21.1.21
If you get something along the lines of: 

  Cloning into 'CheeseOS-21.1.21'...
  remote: Enumerating objects: 34, done.
  remote: Counting objects: 100% (34/34), done.
  remote: Compressing objects: 100% (30/30), done.
  remote: Total 34 (delta 0), reused 0 (delta 0), pack-reused 0
  Unpacking objects: 100% (34/34), done.

Then you're good to go. If not, then follow these instructions for each operating system:
  MacOS:
    Type the following commands in terminal:
      git
    It will open an installer and follow the instructions. After it is installed, type the following commands in terminal:
      cd d
      git clone https://github.com/ZombieWrecker29/CheeseOS-21.1.21
  Windows:
    Go to https://git-scm.com/book/en/v2/Getting-Started-Installing-Git and follow the instructions in the installer. After that, run the following commands in the Command Prompt:
      cd d
      git clone https://github.com/ZombieWrecker29/CheeseOS-21.1.21
  Linux:
    Type the following commands in terminal:
      sudo apt-get update
      sudo apt-get install git
      cd d
      git clone https://github.com/ZombieWrecker29/CheeseOS-21.1.21

# Step 2
In your terminal type the following commands:
  python --version
If the output is:
  Python 3.9.1
Then you're good to go. If it is something else, go to https://www.python.org/downloads/release/python-391/ and download the installer for your operating system. Run the installer and continue to the next step.

# Step 3
Run the following commands in terminal:
  cd d
  cd CheeseOS-21.1.21
Now if you are a first-time user of CheeseOS, then do Step 4a. If you are upgrading to CheeseOS 21, then do Step 4b.

# Step 4a
Run the following commands in terminal:
  cd CheeseOS_Release_21.1.21
  python3 main.py
And you're good to go! The CheeseOS setup should start up. Hope you enjoy CheeseOS 21!

# Step 4b
Open 2 windows in your file browser. One window for your old copy of CheeseOS and one for your new copy of CheeseOS. In your old Copy of CheeseOS, drag ALL files that end in '.json' to the new copy of CheeseOS. If it says a file with that name already exists, then click replace whenever it asks you to. Now, go back to your terminal and run the following commands:
  cd CheeseOS_Release_21.1.21
  python3 main.py
And your CheeseOS login should pop up! Hope you have a good time using CheeseOS 21!
