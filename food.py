from turtle import Turtle
import random
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5) # changes the shape of the turtle 
        self.color("red")
        self.speed("fastest")
        # rand_x = random.randint(-295, 295)
        # rand_y = random.randint(-295, 295)
        # self.goto(rand_x, rand_y)
        self.refresh() #generates food at a random place
    

    def refresh(self):
        rand_x = random.randint(-285, 285)
        rand_y = random.randint(-285, 285)
        self.goto(rand_x, rand_y)