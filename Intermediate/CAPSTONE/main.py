from turtle import Screen
import time 
from cars import Cars
from score import Score
from player import Player



#setup Screen
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)


#making objects
cars = Cars()
score = Score()
player = Player()

#screen listening
screen.listen()
screen.onkey(player.move,"w")

is_game = True
while is_game:
    screen.update()
    time.sleep(0.1)
    
    cars.car()
    cars.move()

    if player.ycor() > 285:
        player.position()
        cars.speed += 5
        score.score += 1
        score.clear()
        score.scores()


    for car in cars.all_cars:
        if car.distance(player) < 20 :
            score.game_over()
            is_game = False


#ecit on click
screen.exitonclick()
