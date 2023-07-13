from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import winsound
import random
import time


screen = Screen()
screen.setup(width=800, height=600)
screen.bgpic("bg.gif")
screen.title("pong")
screen.tracer(0)


#creating the paddle
rpaddle = Paddle((300, 0), "right_paddle.gif")
lpaddle = Paddle((-300, 0), "left_paddle.gif")
ball = Ball("balls.gif")
ball2 = None
bounce_count = 0
scoreboard = Scoreboard()
slaps = ["1.wav","2.wav","3.wav","4.wav"]
message = ["#CROFam","NO FUD", "BAD little whale","STFU", "HODL", "DIAMOND HANDS", "TO THE MOON", "Binance Puppy", "CROFam > Magnus" ]

game_is_on = True
while game_is_on:
    rpaddle.move()
    lpaddle.move()
    rnd_msg = random.choice(message)
    rnd_snd = random.choice(slaps)
    screen.update()
    #moving the ball
    ball.move()
    #detecting collision with the wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    #detecting collision with the paddle
    if ball.distance(rpaddle) < 50 and ball.xcor() > 320:
        rpaddle.display_message(rnd_msg)
        ball.bounce_x()
        bounce_count += 1
        winsound.PlaySound(rnd_snd, winsound.SND_ASYNC)
    if ball.distance(lpaddle) < 50 and ball.xcor() < -320:
        lpaddle.display_message(rnd_msg)
        ball.bounce_x()
        bounce_count += 1
        winsound.PlaySound(rnd_snd, winsound.SND_ASYNC)
        # If there have been 5 bounces and the second ball doesn't exist, create it
    if bounce_count >= 5 and ball2 is None:
        ball2 = Ball("balls2.gif")
        # You can customize the starting position, speed, etc. of the second ball here if you want

    # If the second ball exists, move it
    if ball2 is not None:
        ball2.move()
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
    screen.onkeypress(rpaddle.go_up, "Up")
    screen.onkeypress(rpaddle.go_down, "Down")
    screen.onkeyrelease(rpaddle.stop_moving, "Up")
    screen.onkeyrelease(rpaddle.stop_moving, "Down")

    screen.onkeypress(lpaddle.go_up, "w")
    screen.onkeypress(lpaddle.go_down, "s")
    screen.onkeyrelease(lpaddle.stop_moving, "w")
    screen.onkeyrelease(lpaddle.stop_moving, "s")


#placing a pause to see the black screen
screen.exitonclick()