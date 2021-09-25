from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
bet = screen.textinput(
    "Make your bet", "Which turtle will win  the race? Enter a color:"
)

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtles = []
y = -100


def create_turtle(y, color):
    turtle = Turtle("turtle")
    turtle.color(colors[color])
    turtle.penup()
    turtle.goto(x=-230, y=y)
    all_turtles.append(turtle)


racing = True

for index in range(0, 6):
    y += 30
    create_turtle(y, index)


while racing:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            winner = turtle.pencolor()
            racing = False
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

if winner == bet:
    print(f"You've won! The {winner} turtle is the winner!")
else:
    print(f"You've lost! The {winner} turtle is the winner!")
screen.exitonclick()
