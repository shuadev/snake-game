from turtle import Turtle
import random

LIGHT_PINK = '#f7aab2'


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.shapesize(0.5, 0.5)
        self.color(LIGHT_PINK)
        self.speed('fastest')
        self.new_food()
        # self.food.dot(10, LIGHT_PINK)

    def new_food(self):
        self.new_x = random.randint(-280,280)
        self.new_y = random.randint(-280,280)
        self.goto(self.new_x, self.new_y)


    # def random_colour(self):
    #     self.colours = ""
