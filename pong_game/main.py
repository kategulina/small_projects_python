from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong game")
screen.tracer(0)

r_paddle = Paddle(350, 0)
l_paddle = Paddle(-350, 0)
scoreboard = Scoreboard()

ball = Ball()

screen.listen()
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")

game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collition with walls
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce('y')

    # Detect collisions with paddle
    if ball.distance(l_paddle) < 50 and ball.xcor() < -340 or ball.distance(r_paddle) < 50 and ball.xcor() > 340:
        ball.bounce('x')

    # Detect a score, right side
    if ball.xcor() > 370:
        ball.reset_position()
        scoreboard.increase_score('right')
    
    # Detect a score, left side
    if ball.xcor() < -370:
        ball.reset_position()
        scoreboard.increase_score('left')

screen.exitonclick()
