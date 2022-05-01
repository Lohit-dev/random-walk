# Author : Lohit Sharma
# Purpose : Random Walk
# This code makes uses random module and turtle module to make a random patter. It changes color at every interation


import random
import turtle
from turtle import Turtle, Screen  # import screen and Turtle modules

screen = Screen()  # created a screen object
screen.setup(width=600, height=600)  # set the width and height of the screen
screen.title("My Random Walk")  # Give screen a title
screen.colormode(255)  # make colormode


lavi = Turtle() #make a turtle object
lavi.width(10) #set the width of pen
angles = [0, 90, 180, 360] # make a list of angles


def random_color(): #this function generates and return random combination of red green and blue
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rgb = (r, g, b)
    return rgb


for x in range(100): # iterate pen over 100 times
    lavi.color(random_color()) #change color every iteration
    lavi.forward(30) # move forward 30 pixels
    lavi.right(random.choice(angles)) # move at different random angles

screen.exitonclick()  # exit screen on click
