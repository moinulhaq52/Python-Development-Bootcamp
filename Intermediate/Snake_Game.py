#snake Gane.......
from turtle import Turtle , Screen
import random
import time

#Make object of Turtle (snake) and give it shape of square
snake_position = [(0,0) , (-20 , 0) , (-40 , 0)]
snakes = []

#Make object of Screen
screen = Screen()
screen.tracer(0)


for index in snake_position:
    my_snake = Turtle(shape="square")
    my_snake.penup()
    my_snake.color("black")
    my_snake.goto(index)
    snakes.append(my_snake)


#Give height & width to screen & Background color
screen.setup(height=600 , width=700)
screen.colormode(255)
screen.bgcolor(	144, 238, 144)

#Screen Title
screen.title("Welcome to 3310 Snake Game")
screen.update()


#Movement of snake (only left to right)
#Ror Right
def turn_right():
    for snake in snakes:
        snake.right(90)
#For Left
def turn_left():
    for snake in snakes:
        snake.left(90)

#Input for Level (Easy , Hard , Difficult) and Given speed by seeing level
level = True
while level:
    level_select = screen.textinput("Enter the Level" , "'E' for Easy , 'H' for Hard , 'D' for Difficult").lower()
    if level_select == "e":
        my_snake.speed(1)
        level = False 
    elif level_select == "h":
        my_snake.speed(1.5)
        level = False
    elif level_select == "d":
        my_snake.speed(2.5)
        level = False



#For listneing of screen
screen.listen()

#For picking key
screen.onkey(turn_right , "d")
screen.onkey(turn_left , "a")


#Start game until Highest score or Clash with wall or tail
game_start = True
while game_start: 
    screen.update()
    time.sleep(0.1)
    for snake in snakes:
        snake.forward(10)

#When click on screen close the screen
screen.exitonclick()
