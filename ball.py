from turtle import Turtle


#ball class
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.screen.register_shape("balls.gif")
        self.shape("balls.gif")
        self.penup()
        #self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(0, 0)
        self.x_move = 5
        self.y_move = 5
        self.move_speed = 0.05


    #moving the ball
    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        #self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(new_x, new_y)

    #detecting collision with the wall
    def bounce_y(self):
        self.y_move *= -1

    #detecting collision with the paddle
    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.9

    #resetting the ball
    def reset_position(self):
        self.goto(0, 0)
        self.move_speed = 0.1
        self.bounce_x()