import os
from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Ubuntu", 20, "normal")
PATH = os.path.dirname(os.path.abspath(__file__)) + "/score.txt"


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = self.get_highscore()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0, 250)
        self.update()

    def update(self):
        self.clear()
        self.write(
            f"Score: {self.score} High Score: {self.high_score}",
            align=ALIGNMENT,
            font=FONT,
        )

    def increase_score(self):
        self.score += 1
        self.update()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.set_highscore()
        self.score = 0
        self.update()

    def get_highscore(self):
        score = 0
        with open(PATH, mode="r") as file:
            score = file.read()
        if score != None:
            return int(score)
        return 0

    def set_highscore(self):
        with open(PATH, mode="w") as file:
            file.write(str(self.score))
