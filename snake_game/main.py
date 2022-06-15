from food import Food
from turtle import Screen
from snake import Snake
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = ScoreBoard()

screen.listen()
screen.onkey(snake.up,"w")
screen.onkey(snake.down, "s")
screen.onkey(snake.left, "a")
screen.onkey(snake.right, "d")

game_is_on = True
while game_is_on:
    snake.move()

    time.sleep(0.1)
    screen.update()

    #  Detect collision with food
    if snake.head.distance(food) < 20:
        food.refresh()
        score.increase_score()
        snake.add_new_segment()

    #  Detect collision with walls
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        score.end_game()

    # Detect collision with tail
    for segment in snake.snake[2::]:
        if snake.head.distance(segment) < 20:
            game_is_on = False
            score.end_game()

screen.exitonclick()
