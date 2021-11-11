from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 11, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.write_score()

    def add_point(self):
        self.score = self.score + 1
        self.clear()
        self.write_score()

    def write_score(self):
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.write(f"Score: {self.score}", False, ALIGNMENT, font=FONT)
