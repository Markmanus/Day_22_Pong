from turtle  import Turtle

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)

    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)

    def display_message(self, message):
        message_turtle = Turtle()
        message_turtle.penup()
        message_turtle.hideturtle()
        message_turtle.color("white")

        # Positioning the message near the paddle
        x_cor = self.xcor() - 40 if self.xcor() > 0 else self.xcor() + 40
        message_turtle.goto(x_cor, self.ycor())

        message_turtle.write(message, align="center", font=("Arial", 24, "normal"))

