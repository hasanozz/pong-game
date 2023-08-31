from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.setheading(90)
        self.penup()
        self.goto(position)
    
    def paddle_up(self):
        self.fd(20)

    def paddle_down(self):
        self.backward(20)