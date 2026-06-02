#snake Gane.......
from turtle import Turtle , Screen
screen = Screen()
from Food import Food



#Make object of Turtle (snake) and give it shape of square
snake_position = [(0,0) , (-20 , 0) , (-40 , 0)]
class Snake():
    def __init__(self):
        self.snakes = []
        self.create_snake()
        self.head = self.snakes[0]

    def create_snake(self):
        for index in snake_position:
            self.snake_piece(index)

    def reset(self):
        for snake in self.snakes:
            snake.goto(1000,1000)
        self.snakes.clear()
        self.create_snake()
        self.head = self.snakes[0]


    def snake_piece(self, index):
        my_snake = Turtle(shape="square")
        my_snake.penup()
        my_snake.color("black")
        my_snake.goto(index)
        self.snakes.append(my_snake)


    def extend(self):
        self.snake_piece(self.snakes[-1].position())

    #Movement of snake (only left to right)
    #Ror Right
    def turn_right(self):
        if self.head.heading() != 180:
            self.snakes[0].setheading(0)
    #For Left
    def turn_left(self):
        if self.head.heading() != 0:
            self.snakes[0].setheading(180)

    #Movement of snake (only up to down)
    #Ror Up
    def turn_up(self):
        if self.head.heading() != 270:
            self.snakes[0].setheading(90)
    #For Left
    def turn_down(self):
        if self.head.heading() != 90:                  
            self.snakes[0].setheading(270)


    #Move Forward
    def move(self):
        for new_position in range(len(self.snakes)-1 , 0 , -1):
            x = self.snakes[new_position - 1].xcor()
            y = self.snakes[new_position - 1].ycor()
            self.snakes[new_position].goto(x , y)
        self.snakes[0].forward(20)


    #Input for Level (Easy , Hard , Difficult) and Given speed by seeing level
    def level(self):
        level = True
        while level:
            level_select = screen.textinput("Enter the Level" , "'E' for Easy , 'H' for Hard , 'D' for Difficult").lower()
            if level_select == "e":
                self.snakes.speed(1)
                level = False 
            elif level_select == "h":
                self.snakes.speed(1.5)
                level = False
            elif level_select == "d":
                self.snakes.speed(2.5)
                level = False


