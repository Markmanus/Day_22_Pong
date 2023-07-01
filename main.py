from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
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
scoreboard = Scoreboard()

game_is_on = True
while game_is_on:
    screen.update()
    #moving the ball
    ball.move()
    #detecting collision with the wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    #detecting collision with the paddle
    if ball.distance(rpaddle) < 50 and ball.xcor() > 320 or ball.distance(lpaddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    #detecting when the ball goes out of bounds
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.lpoint()
        ball.bounce_x()
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.rpoint()
        ball.bounce_x()


    time.sleep(ball.move_speed)
    #moving the paddle
    screen.listen()
    screen.onkey(rpaddle.go_up, "Up")
    screen.onkey(rpaddle.go_down, "Down")
    screen.onkey(lpaddle.go_up, "w")
    screen.onkey(lpaddle.go_down, "s")


#placing a pause to see the black screen
screen.exitonclick()