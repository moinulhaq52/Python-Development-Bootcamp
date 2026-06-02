import random
from turtle import Turtle

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5,stretch_wid=0.5)
        self.color("green")
        self.speed("fastest")
        self.refresh()


    def refresh(self):
        x = random.randint(-288,288)
        y = random.randint(-288,288)
        self.goto(x,y)