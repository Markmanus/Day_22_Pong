from turtle  import Turtle
import threading
import time

class Paddle(Turtle):
    def __init__(self, position,image):
        super().__init__()
        self.screen.register_shape(image)
        self.shape(image)
        self.shapesize(stretch_wid=10, stretch_len=2)
        self.penup()
        self.goto(position)
        self.move_speed = 10
        self.moving_up = False
        self.moving_down = False

    def go_up(self):
        self.moving_up = True
        self.moving_down = False

    def go_down(self):
        self.moving_down = True
        self.moving_up = False

    def stop_moving(self):
        self.moving_up = False
        self.moving_down = False

    def move(self):
        if self.moving_up:
            self.sety(self.ycor() + self.move_speed)
        if self.moving_down:
            self.sety(self.ycor() - self.move_speed)

    def display_message(self, message):
        message_turtle = Turtle()
        message_turtle.penup()
        message_turtle.hideturtle()
        message_turtle.color("red")

        # Positioning the message near the paddle
        x_cor = self.xcor() - 150 if self.xcor() > 0 else self.xcor() + 150
        message_turtle.goto(x_cor, self.ycor())

        message_turtle.write(message, align="center", font=("Comic", 26, "bold"))

        self.screen.ontimer(lambda: self.clear_message(message_turtle), 1000)

    def clear_message(self, message_turtle):
        # Clear the message
         message_turtle.clear()

