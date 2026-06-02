#imports
from turtle import Screen
from paddles_ball import Paddle
from ball import Ball
from score import Score
import time

#objects
screen = Screen()
screen.tracer(0)
paddle = Paddle()
ball = Ball()
score = Score()




#screen Detail
screen.title("PONY GAME")
screen.setup(800,600)
screen.bgcolor('orange')


#listen
screen.listen()

#for picking keys
#right pad
screen.onkey(paddle.right_up , "Up")
screen.onkey(paddle.right_down , "Down")
#left pad
screen.onkey(paddle.left_up , "w")
screen.onkey(paddle.left_down , "s")

#start game
Game = True
while Game:
    screen.update()
    time.sleep(ball.speed)
    ball.ball_move()
    score.clear()
    score.r_score()
    score.l_score()
    


    #wall
    if ball.ycor() > 280 or ball.ycor() < - 280:
        ball.ball_bounce_y()


    #paddle
    if (ball.distance(paddle.paddle_right)<50 and ball.xcor() > 349) or (ball.distance(paddle.paddle_left)<50 and ball.xcor() < -350):
        ball.ball_bounce_x()

    #miss
    if ball.xcor() > 390: 
        ball.reset()
        score.left_score +=1


    if ball.xcor() < -390:
        ball.reset()
        score.right_score +=1


#listen
screen.listen()

#for picking keys
#right pad
screen.onkey(paddle.right_up() , "w")
screen.onkey(paddle.right_down() , "s")
#left pad
screen.onkey(paddle.left_up() , "Up")
screen.onkey(paddle.left_down() , "Down")


#Close the Screen When click on Screen
screen.exitonclick()
