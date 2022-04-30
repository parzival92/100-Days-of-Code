"""
This module will create dashed line from turtle graphics
"""

from turtle import Turtle,Screen

parzival_tutle = Turtle()

for item in range(50):
    parzival_tutle.forward(10)
    parzival_tutle.penup()
    parzival_tutle.forward(10)
    parzival_tutle.pendown()

myscreen = Screen()
myscreen.exitonclick()
