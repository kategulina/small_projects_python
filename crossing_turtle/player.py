from turtle import Turtle

STARTING_POSITION = (0, -230)
MOVE_DISTANCE = 10

class Player(Turtle):
    
    def __init__(self):
        super().__init__()
        self.setheading(90)
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.goto_start()

    def move(self):
        self.goto(0,self.ycor()+MOVE_DISTANCE)

    def goto_start(self):
        self.goto(STARTING_POSITION)
