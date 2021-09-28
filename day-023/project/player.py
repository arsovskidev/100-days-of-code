from turtle import Turtle


STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10


class Player(Turtle):
    def __init__(self):
        super().__init__("turtle")
        self.color("black")
        self.penup()
        self.setheading(90)
        self.goto(STARTING_POSITION)

    def move(self):
        self.forward(MOVE_DISTANCE)
        print(f"X COR: {self.xcor()}")
        print(f"Y COR: {self.ycor()}")

    def up(self):
        self.setheading(90)
        if self.ycor() < 280:
            self.move()

    def down(self):
        self.setheading(270)
        if self.ycor() > -270:
            self.move()

    def left(self):
        self.setheading(180)
        if self.xcor() > -280:
            self.move()

    def right(self):
        self.setheading(0)
        if self.xcor() < 270:
            self.move()

    def reset(self):
        self.goto(STARTING_POSITION)
