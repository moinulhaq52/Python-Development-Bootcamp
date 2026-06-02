from turtle import Turtle

class Paddle:
    def __init__(self):

        #left padle
        self.paddle_left = Turtle("square")
        self.paddle_left.penup()
        self.paddle_left.color("black")
        self.paddle_left.shapesize(4 , 1)
        self.paddle_left.goto( -380.0, 0)

        #right padle
        self.paddle_right = Turtle("square")
        self.paddle_right.penup()
        self.paddle_right.color("black")
        self.paddle_right.shapesize(4 , 1)
        self.paddle_right.goto( 375.0, 0) 
        

#Also block after at one point
    #right up
    def right_up(self):
        new_position = self.paddle_right.ycor() + 20
        if new_position < 280:
            self.paddle_right.goto(self.paddle_right.xcor() , new_position)
    #right down
    def right_down(self):
        new_position = self.paddle_right.ycor() - 20
        if new_position > - 280:
            self.paddle_right.goto(self.paddle_right.xcor() , new_position)
    #left up
    def left_up(self):
        new_position = self.paddle_left.ycor() + 20
        if new_position < 280:
            self.paddle_left.goto(self.paddle_left.xcor() , new_position)
    #left down
    def left_down(self):
        new_position = self.paddle_left.ycor() - 20
        if new_position > - 280:
            self.paddle_left.goto(self.paddle_left.xcor() , new_position)
        