from turtle import Screen
from paddle import Paddle
from ball import Ball
import time


screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("pong")
screen.tracer(0)

#creating the paddle
rpaddle = Paddle((350, 0))
lpaddle = Paddle((-350, 0))
ball = Ball()


game_is_on = True
while game_is_on:
    screen.update()
    #moving the ball
    ball.move()
    time.sleep(ball.move_speed)

    time.sleep(0.1)
    #moving the paddle
    screen.listen()
    screen.onkey(rpaddle.go_up, "Up")
    screen.onkey(rpaddle.go_down, "Down")
    screen.onkey(lpaddle.go_up, "w")
    screen.onkey(lpaddle.go_down, "s")


#placing a pause to see the black screen
screen.exitonclick()