from turtle import Turtle

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.snake = []
        for i in range(3):
            new_segment = Turtle("square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(0-20*i, 0)
            self.snake.append(new_segment)
        self.head = self.snake[0]


    def move(self):
        for segment in range(len(self.snake)-1, 0, -1):
            new__x = self.snake[segment-1].xcor()
            new_y = self.snake[segment-1].ycor()
            self.snake[segment].goto(new__x, new_y)
        self.snake[0].forward(MOVE_DISTANCE)
     
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)


    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def add_new_segment(self):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        self.snake.append(new_segment)
        