from turtle import Turtle
FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 1
        self.color("black")
        self.penup()
        self.hideturtle()
        self.goto(-280,260)
        self.write(arg=f"Level: {self.level}", font=FONT)

    def increase_level(self):
        self.level += 1
        self.clear()
        self.write(arg=f"Level: {self.level}", font=FONT)

    def end_game(self):
        self.clear()
        self.goto(0, 0)
        self.write(arg="GAME OVER", font=FONT, align="center")
