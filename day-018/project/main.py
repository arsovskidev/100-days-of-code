import turtle as t
import random
from color_extraction import colors

screen = t.Screen()
screen.setup(width=550, height=600)

turtle = t.Turtle()
t.colormode(255)
turtle.shape("circle")
turtle.speed("fastest")
turtle.hideturtle()
turtle.penup()
turtle.goto(-230, -250)

for _ in range(0, 10):
    for _ in range(0, 10):
        turtle.dot(20, random.choice(colors))
        turtle.forward(50)

    turtle.backward(500)
    turtle.setheading(90)
    turtle.forward(50)
    turtle.setheading(0)


turtle.goto(-230, -250)
screen.exitonclick()
