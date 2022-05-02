from turtle import Turtle,Screen

timmy = Turtle()
screen = Screen()

def move_forward():
    """Method to move turtle forward"""
    timmy.forward(10)

def move_backward():
    """Method to move turtle backward"""
    timmy.backward(10)

def turn_left():
    """Method to move turtle left direction"""
    timmy.left(10)

def turn_right():
    """Method to move turtle in right direction"""
    timmy.right(10)

def clear():
    """Method to clear screen"""
    timmy.clear()
    timmy.penup()
    timmy.home()
    timmy.pendown()

screen.listen()
screen.onkey(move_forward,"w")
screen.onkey(move_backward,"s")
screen.onkey(turn_left,"a")
screen.onkey(turn_right,"d")
screen.onkey(clear,"c")
screen.exitonclick()