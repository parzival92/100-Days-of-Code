"""
This module will create square from turtle graphics
"""

from turtle import Turtle,Screen

parzival_tutle = Turtle()

for item in range(4):
    parzival_tutle.forward(100)
    parzival_tutle.left(90)

myscreen = Screen()

myscreen.exitonclick()
