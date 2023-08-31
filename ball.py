from turtle import Turtle

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.goto(0, 0)
        self.step_x = 10
        self.step_y = 10

    def move(self):
        # movement of the ball
        new_x = self.xcor() + self.step_x
        new_y = self.ycor() + self.step_y
        self.goto(new_x, new_y)

    def ball_goes_out(self):
        # if the ball goes out refresh the ball's place and change the direction of movement
        self.goto(0, 0)
        self.step_x *= -1