from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__("square")
        self.shapesize(5, 1, 1)
        self.color("white")
        self.penup()
        self.starting_position = position
        self.goto(self.starting_position)

    def up(self):
        if self.ycor() < 230:
            self.goto(self.xcor(), self.ycor() + 20)

    def down(self):
        if self.ycor() > -230:
            self.goto(self.xcor(), self.ycor() - 20)

    def reset(self):
        self.goto(self.starting_position)
