#snake Gane.......
from turtle import Turtle ,Screen
import time
from Snake import Snake
from Food import Food
from Score import Score 

new_snakes = Snake()
my_food = Food()
my_score = Score()

new_snake = new_snakes.snakes


#Make object of Screen
screen = Screen()
screen.tracer(0)


#Give height & width to screen & Background color
screen.setup(height=600 , width=600)
screen.colormode(255)
screen.bgcolor(	144, 238, 144)


#Screen Title
screen.title("Welcome to 3310 Snake Game")
screen.update()

#Levels
# new_snakes.level()


#For listneing of screen
screen.listen()

#For picking key
screen.onkey(new_snakes.turn_right , "d")
screen.onkey(new_snakes.turn_left , "a")
screen.onkey(new_snakes.turn_up , "w")
screen.onkey(new_snakes.turn_down , "s")



#Start game until Highest score or Clash with wall or tail
game_start = True
while game_start: 
    screen.update()
    time.sleep(0.1)
    new_snakes.move()

    if new_snakes.head.distance(my_food) < 15 :
        my_food.refresh()
        new_snakes.extend()
        my_score.add_score()


    if new_snakes.head.xcor() > 280 or new_snakes.head.xcor() < -280 or new_snakes.head.ycor() > 280 or new_snakes.head.ycor() < -280: 
        # game_start = False
        my_score.highscore_set()
        new_snakes.reset()
        # my_score.over()

    #Without Slicing
    # for i in new_snakes.snakes:
    #     if i == new_snakes.head:
    #         pass
    #     elif new_snakes.head.distance(i) < 10:
    #         game_start = False
    #         my_score.over()

    #Without Slicing
    for i in new_snakes.snakes[1:]:
        if new_snakes.head.distance(i) < 10:
            # game_start = False
            my_score.highscore_set()
            new_snakes.reset()

            # my_score.over()

#When click on screen close the screen
screen.exitonclick()
