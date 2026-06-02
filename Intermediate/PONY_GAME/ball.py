from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        
        self.shape("circle")
        self.penup()
        self.color("black")
        self.goto(0,0)
        self.x_side = 10
        self.y_side = 10
        self.speed = 0.1
    
    def ball_move(self):
        x = self.xcor() + self.x_side
        y = self.ycor() + self.y_side
        self.goto(x,y)

    def ball_bounce_y(self):
        self.y_side *= -1

    def ball_bounce_x(self):
        self.x_side *= -1
        self.speed *= 0.9

    def reset(self):
        self.goto(0,0)
        self.speed = 0.1
        self.ball_bounce_x()
        self.ball_bounce_y()