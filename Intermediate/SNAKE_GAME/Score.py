from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        
        self.score = 0
        #self.highscore= 0
        with open("Intermediate\SNAKE_GAME\data.txt", mode="r")as highscores:
            self.highscore = int(highscores.read())
        self.hideturtle()
        self.penup()
        self.shape()
        self.goto(0,275)
        self.update()

    def update(self):
        self.clear()
        self.write(f"Score : {self.score} Highest Score : {self.highscore}" , align= "center" , font=("Arial" ,12 , "normal"))

    def add_score(self):
        self.score += 1
        self.update()

    def highscore_set(self):
        if self.highscore < self.score:
            self.highscore = self.score
            with open("Intermediate\SNAKE_GAME\data.txt" ,mode="w") as score_text:
                score_text.write(f"{self.highscore}")
        self.score = 0
        
        self.update()

    

    # def over(self):
    #     self.clear()
    #     self.write(f"Game Over. Your Score is {self.score}" , align= "center" , font=("Arial" ,12 , "normal"))
    
