import turtle
from turtle import *

wn = Screen()
wn.setup(700, 700)
wn.title('white')
wn.bgcolor('black')

# Create Player
player = Turtle('triangle')
player.speed('fastest')
player.color('white')
print("Welcome to the drawing game!")
print("The controls are:")
print("To look around use the right and left arrow keys")
print("To move around use the up arrow")
print("Other controls are")
print("Put Pen Down: w")
print("Put Pen Up: a")
print("Start Erasing: s")
print("Start Drawing: d")
print("Exit: e")
def forward():
    player.forward(20)

def left():
    player.left(90)

def right():
    player.right(90)

def draw():
  player.pendown()
def stop():
  player.penup()
def erase():
  player.pencolor("black")
def write():
  player.pencolor("white")
def exit():
  import importlib
  import gamecenter
  importlib.reload(gamecenter)
  import gamecenter
wn.onkey(forward, 'Up')
wn.onkey(left, 'Left')
wn.onkey(right, 'Right')
wn.onkey(draw,"w")
wn.onkey(stop,"a")
wn.onkey(erase,"s")
wn.onkey(write,"d")
wn.onkey(exit,"e")
wn.listen()
wn.mainloop()