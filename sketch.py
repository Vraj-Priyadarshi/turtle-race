
from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()
cloc = 5

def move():
    tim.forward(10)

def backward():
    tim.back(10)

def clockwise():
    new_heading = tim.heading() + 10
    tim.setheading(new_heading)


def anticlockwise():
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)

def clear():
    tim.clear()
    tim.penup()
    tim.setposition(0, 0)
    tim.pendown()

screen.listen()
screen.onkeypress(key="w", fun=move)
screen.onkeypress(fun=backward, key="s")
screen.onkeypress(fun=clockwise, key="d")
screen.onkeypress(fun=anticlockwise, key="a")
screen.onkeypress(fun=clear, key="c")

screen.exitonclick()