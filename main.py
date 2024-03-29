from turtle import Screen
from snake import Snake
from snake_food import Food
import time
from scoreboard import Scoreboard
screen = Screen()
screen.setup(width=600, height=600)
screen.title("Snake Xenia")
screen.bgcolor("black")
screen.tracer(0)


snake = Snake()
food = Food()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(snake.down, "Down")
screen.onkey(snake.up, "Up")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")
screen.listen()


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.08)
    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        scoreboard.re_set()
        snake.re_set()

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.re_set()
            snake.re_set()

screen.exitonclick()
