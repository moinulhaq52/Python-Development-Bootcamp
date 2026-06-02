import turtle
import pandas
import time

screen = turtle.Screen()
screen.title("US STATES GAME")
image = "./Intermediate/US_State_Game/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

game_data = pandas.read_csv("./Intermediate/US_State_Game/50_states.csv")
print(game_data)
Guessed_state = []
Missed_state = []
Total = 0
Game = True


while Game:
    answer = screen.textinput(f"{Total}/50 Guess the state" , "What's another state:")
    answer = answer.title()
    if answer == "Exit":
        Missed_state = [my_state for my_state in game_data.state if my_state not in Guessed_state]
        break
    for state in game_data.state:
        if state == answer:
            print("correct")
            Guessed_state.append(answer)
            Total += 1
            state = turtle.Turtle()
            state.penup()
            state.hideturtle()
            state_row = game_data[game_data.state == answer]
            # print(state_row)
            # print(state_row.x)
            x = int(state_row.x)
            y = int(state_row.y)
            state.goto(x ,y)
            state.write(answer)
            if Total == 50:
                Game = False
     
    time.sleep(1)


#adding missed state by seeing guessed state 
# for state in game_data.state:
#     if state not in Guessed_state:
#         Missed_state.append(state)


#Add data in csv
missing_data = pandas.DataFrame(Missed_state)
missing_data.to_csv("./Intermediate/US_State_Game/Missing_states.csv")


#for knowing coordinates on screen of turtle
# def get_coor(x,y):
#     print(x,y)
# turtle.onscreenclick(get_coor)
# turtle.mainloop()


# exit when click
# screen.exitonclick()