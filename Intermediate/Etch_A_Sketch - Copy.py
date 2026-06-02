from turtle import Turtle , Screen
tin = Turtle()
screen = Screen()

def move_forward():
    tin.forward(10)
def move_backward():
    tin.backward(10)
def move_right():
    tin.right(10)
def move_left():
    tin.left(10)
def screen_clear():
    tin.clear()
def reset_screen():
    screen.resetscreen()

screen.listen()
screen.onkey(move_forward , "w")
screen.onkey(move_backward , "s")
screen.onkey(move_right , "d")
screen.onkey(move_left , "a")
screen.onkey(screen_clear,"c")
screen.onkey(reset_screen,"r")





screen.exitonclick()