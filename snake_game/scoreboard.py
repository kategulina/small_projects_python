from turtle import Turtle

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0,270)
        self.write(arg=f"Score: {self.score}", move=False, align="center", font=("Ariel", 20, "normal"))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.write(arg=f"Score: {self.score}", move=False, align="center", font=("Ariel", 20, "normal"))
    
    def end_game(self):
        self.goto(0, 0)
        self.write("Game over", 20, "center", ("Ariel", 20, "normal"))
