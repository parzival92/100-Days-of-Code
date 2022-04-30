"""
This module will spirowalk line from turtle graphics
"""

from turtle import Turtle,Screen
import random
import turtle as t

t.colormode(255)
color = ["red","green","blue","CornflowerBlue",
        "orange","IndianRed","LightSeaGreen","wheat","SeaGreen"]


parzival_tutle = Turtle()
parzival_tutle.pensize(1)
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

def draw_spirograph(size_of_gap):
    """
    This module will spirowalk line from turtle graphics
    """
    for _ in range(int(360 / size_of_gap)):

        parzival_tutle.color(random_color())
        parzival_tutle.circle(100)
        parzival_tutle.setheading(parzival_tutle.heading() + 10)


    

draw_spirograph(5)  


myscreen = Screen()
myscreen.exitonclick()
