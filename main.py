from turtle import Screen
from paddle import Paddle
import time


screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("pong")
screen.tracer(0)

#creating the paddle
paddle = Paddle((350, 0))

game_is_on = True
while game_is_on:
    screen.update()

    #moving the paddle
    screen.listen()
    screen.onkey(paddle.go_up, "Up")
    screen.onkey(paddle.go_down, "Down")


#placing a pause to see the black screen
screen.exitonclick()