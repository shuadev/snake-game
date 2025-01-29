import time
from turtle import Screen
from snake import Snake
from scoreboard import Scoreboard
from food import Food

DARK_PINK = '#961b3c'
LIGHT_PINK = '#f7aab2'
BG_COLOUR = '#48091a'

scoreboard = Scoreboard()
snake = Snake()
food = Food()

# screen setup
s = Screen()
s.setup(width=600, height=600)
s.bgcolor(BG_COLOUR)
s.title('HISS')
s.tracer(0)

s.onkey(snake.left, "Left")
s.onkey(snake.right, "Right")
s.onkey(snake.up, "Up")
s.onkey(snake.down, "Down")
s.listen()


keep_playing = True
while keep_playing:
    s.update()
    time.sleep(0.1)
    snake.move()

    # collision with wall
    if (snake.head.xcor() > 300 or snake.head.xcor() < -300 or
            snake.head.ycor() > 300 or snake.head.ycor() < -300):
        # keep_playing = False
        scoreboard.reset_score()
        snake.reset_snake()

    # detect collision with food
    if snake.head.distance(food) < 15:
        food.new_food()
        scoreboard.increase_score()
        snake.extend()

    # detect collision with self
    for segment in snake.snake_segments[1:]:
        if snake.head.distance(segment) < 10:
            # keep_playing = False
            scoreboard.reset_score()
            snake.reset_snake()


s.exitonclick()
