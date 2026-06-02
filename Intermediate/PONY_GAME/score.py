from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.left_score = 0
        self.right_score = 0

    
    def r_score(self):
        self.goto( 30 , 260)
        self.write(self.right_score, font=("Arial" , 25 , "normal"))

    def l_score(self):
        self.goto( -30 , 260 )
        self.write(self.left_score , font=("Arial" , 25 , "normal"))
