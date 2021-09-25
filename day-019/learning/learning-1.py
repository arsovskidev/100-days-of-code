from turtle import Turtle, Screen

turtle = Turtle()
screen = Screen()


def move_forwards():
    turtle.forward(10)


screen.listen()
screen.onkey(move_forwards, "space")
screen.exitonclick()
