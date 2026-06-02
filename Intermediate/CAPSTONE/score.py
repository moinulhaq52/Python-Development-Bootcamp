from turtle import Turtle
FONT = ("Courier", 20, "normal")



class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.scores()

    def scores(self):
        self.goto(-270,260)
        self.write(f"level : {self.score}" , font=FONT , align="left" ,move=True)

    def game_over(self):
        self.goto(-60,0)
        self.write("Game Over" , font=FONT , align="left" ,move=True)