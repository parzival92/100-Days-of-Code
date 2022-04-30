"""
This module will random walk with random color line from turtle graphics
"""

from turtle import Turtle,Screen
import random
import turtle as t

t.colormode(255)
color = ["red","green","blue","CornflowerBlue",
        "orange","IndianRed","LightSeaGreen","wheat","SeaGreen"]
direction = [0,90,180,270]

parzival_tutle = Turtle()
parzival_tutle.pensize(10)
parzival_tutle.speed("fastest")




def random_color():
    color_list = []
    r = random.randint(0,255)
    color_list.append(r)
    g = random.randint(0,255)
    color_list.append(g)
    b = random.randint(0,255)
    color_list.append(b)
    return color_list

for _ in range(200):

    parzival_tutle.color(random_color())
    parzival_tutle.forward(30)
    parzival_tutle.setheading(random.choice(direction))
    


myscreen = Screen()
myscreen.exitonclick()
