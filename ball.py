from turtle import Turtle
import time

class Ball(Turtle):
    def __init__(self,image):
        super().__init__()
        self.screen.register_shape(image)
        self.shape(image)
        self.penup()
        self.goto(0, 0)
        self.x_move = 5
        self.y_move = 5
        self.move_speed = 0.05
        self.last_bounce_x = 0  # Time of last x bounce
        self.last_bounce_y = 0  # Time of last y bounce

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        current_time = time.time()
        # Only allow a bounce if enough time has passed since the last y bounce
        if current_time - self.last_bounce_y > 0.1:
            self.y_move *= -1
            self.last_bounce_y = current_time  # Update the time of the last y bounce

    def bounce_x(self):
        current_time = time.time()
        # Only allow a bounce if enough time has passed since the last x bounce
        if current_time - self.last_bounce_x > 0.1:
            self.x_move *= -1
            self.move_speed *= 0.9
            self.last_bounce_x = current_time  # Update the time of the last x bounce

    def reset_position(self):
        self.goto(0, 0)
        self.move_speed = 0.1
        self.bounce_x()