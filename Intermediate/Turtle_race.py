import random
from turtle import Turtle,Screen
Turtles = []
Turtle_distance = [0,0,0,0,0,0]
screen = Screen()
screen.setup(width=600,height=500)
color_of_player_turtle = screen.textinput("Bet on turtle","Color of Your Turtle that you thought win the race: \n red , blue , yellow , pink , purple , orange").lower()
position = [-200 , -120 , -40 , 40 , 120 , 200]
colors = ["red" , "blue" , "yellow" , "pink" , "purple" , "orange"] 
for index in range(0,6):
    T = Turtle(shape="turtle")
    T.penup()
    T.color(colors[index])
    T.goto(x=-290,y=position[index])
    T.speed("fastest")
    Turtles.append(T)
if color_of_player_turtle:
    race = True
while race:
    for index in range(0,6):
        distance = random.randint(0,10)
        Turtles[index].forward(distance)
        Turtle_distance[index] += distance
        if Turtle_distance[index] >558:
            winner_color = colors[index]
            race = False  
            
if winner_color == color_of_player_turtle:
    print("You Win")
else:
    print(f"You lose. The winning turtle is '{winner_color}' ")
# print(winner_color)

    






screen.exitonclick()