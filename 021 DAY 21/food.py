from turtle import Turtle
import random

COLORS = ["red" ,"blue", "green", "yellow" ,"orange"]

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.shapesize(0.5,0.5)
        self.color(random.choice(COLORS))
        self.speed('fastest')
        self.refresh()
        
    def refresh(self):
        self.color(random.choice(COLORS))
        ran_x = random.randint(-270,270)
        ran_y = random.randint(-270,270)
        self.goto(ran_x,ran_y)
        
    