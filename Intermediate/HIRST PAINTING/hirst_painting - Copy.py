
import turtle as t
from turtle import Turtle , Screen
import random
screen = Screen()
mike_turtle = Turtle()
t.colormode(255)
# import colorgram

# painting_colors = []s

# colors = colorgram.extract('D:\D\PROJECT PORTFOLIO\Intermediate\HIRST PAINTING\image.jpg',30)

# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     color_rgb = (r,g,b)
#     painting_colors.append(color_rgb)




#pen up always
mike_turtle.penup()

#hide turtle
mike_turtle.hideturtle()

#Forward 10 times with dots and color change
def forward_ten_times():
    for _ in range(0,10):
        color = random.choice(color_list)
        mike_turtle.dot(18,color) 
        mike_turtle.forward(50)
# print(painting_colors)
color_list = [(245, 243, 238), (246, 242, 244), (202, 164, 110), (240, 245, 241), (236, 239, 243), (149, 75, 50),
                (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73),
                  (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158),
                    (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129),
                      (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)] 

#speed
mike_turtle.speed("fastest")

#set position and run
mike_turtle.setheading(215)
print(mike_turtle.position())
mike_turtle.forward(250)
mike_turtle.setheading(0)
for _ in range(0,10):
    forward_ten_times()
    mike_turtle.setheading(90)
    mike_turtle.forward(50)
    mike_turtle.setheading(180)
    mike_turtle.forward(500)
    mike_turtle.setheading(0)
    

screen.exitonclick()

