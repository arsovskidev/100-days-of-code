from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.l_score = 0
        self.r_score = 0

        self.update()

    def update(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, align="center", font=("Ubuntu", 40, "normal"))
        self.goto(100, 200)
        self.write(self.r_score, align="center", font=("Ubuntu", 40, "normal"))

    def add_l_point(self):
        self.l_score += 1
        self.update()

    def add_r_point(self):
        self.r_score += 1
        self.update()
