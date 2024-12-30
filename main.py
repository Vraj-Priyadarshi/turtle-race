from turtle import Turtle, Screen
import random



is_race_on = False
screen = Screen()
screen.setup(500,400)
screen.colormode(255)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race ? Enter a color: ")
colors = ["red","orange","yellow","green","blue","purple"]
y = 125
all_turtles = []
for i in range(6):
    random_color = random.choice(colors)
    colors.remove(random_color)
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(random_color)
    new_turtle.penup()
    new_turtle.goto(x=-238, y=y)
    all_turtles.append(new_turtle)
    y -= 50

if user_bet:
    is_race_on = True
while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color==user_bet:
                print(f"You've Won !! The {winning_color} turtle is the winner ")
            else:
                print(f"You've LOST !! The {winning_color} turtle is the winner ")
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

























screen.exitonclick()