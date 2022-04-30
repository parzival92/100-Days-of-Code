"""
This module will create Shapes(triangle,square,pentagon,hexagon etc) line from turtle graphics
"""

from turtle import Turtle,Screen
import random

color = ["red","green","blue","CornflowerBlue","orange","IndianRed","LightSeaGreen","wheat","SeaGreen"]

parzival_tutle = Turtle()

def draw_shape(num_sides):
    """
    This module will create dashed line from turtle graphics
    """
    for _ in range(num_sides):
        angle = 360/num_sides
        parzival_tutle.forward(100)
        parzival_tutle.right(angle)
        

for _ in range(3,11):
    rand_color = random.choice(color)
    parzival_tutle.color(rand_color)
    draw_shape(_)


myscreen = Screen()
myscreen.exitonclick()
