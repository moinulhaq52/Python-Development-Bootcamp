from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class Cars:
    def __init__(self):
        self.all_cars = []
        self.speed = STARTING_MOVE_DISTANCE

    def car(self):
        random_car = random.randint(1,6)

        if random_car == 1:
            car = Turtle("square")
            car.penup()
            car.shapesize(1.1,2.2)
            car.color(random.choice(COLORS))
            y_random = random.randint(-250,250)
            car.goto(x=300 , y=y_random)
            self.all_cars.append(car)

      
    def move(self):
        for cars in self.all_cars:
            cars.setheading(180)
            cars.forward(self.speed)
        
    
