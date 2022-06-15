from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.l_score = 0
        self.r_score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0,260)
        self.write(arg=f"{self.l_score} : {self.r_score}", move=False, align="center", font=("Ariel", 30, "normal"))

    def increase_score(self, winner):
        if winner == 'left':
            self.l_score += 1
            self.clear()
            self.write(arg=f"{self.l_score} : {self.r_score}", move=False, align="center", font=("Ariel", 30, "normal"))

        elif winner == 'right':
            self.r_score += 1
            self.clear()
            self.write(arg=f"{self.l_score} : {self.r_score}", move=False, align="center", font=("Ariel", 30, "normal"))
