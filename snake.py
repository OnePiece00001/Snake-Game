from turtle import Turtle
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
class Snake:
    
    def __init__(self):
        self.segments = []
        self.create_snake()
        # self.move()
    
    def create_snake(self):
        for i in range(3):
            pen = Turtle("square")
            pen.up()
            # pen.shapesize(stretch_len=0.5, stretch_wid=0.5)
            pen.color("white")
            pen.goto(-20*i, 0)
            self.segments.append(pen)
    
    def move(self):
        for i in range(len(self.segments)-1,0,-1):
            x=self.segments[i-1].xcor()
            y=self.segments[i-1].ycor()
            self.segments[i].goto(x,y)
        # turt[0].right(90)
        self.segments[0].fd(20)
    
    def add_tail(self):
        pen = Turtle("square")
        # pen.shapesize(stretch_len=0.5, stretch_wid=0.5)
        pen.up()
        pen.color("white")
        val = len(self.segments)
        x = self.segments[val-1].xcor()
        y = self.segments[val-1].ycor()
        pen.goto(x, y)
        self.segments.append(pen)

    def up(self):
        if(self.segments[0].heading() != DOWN):
            self.segments[0].setheading(UP)
            
    def down(self):
        if(self.segments[0].heading() != UP):
            self.segments[0].setheading(DOWN)
        
    def left(self):
        if(self.segments[0].heading() != RIGHT):
            self.segments[0].setheading(LEFT)
        
    def right(self):
        if(self.segments[0].heading() != LEFT):
            self.segments[0].setheading(RIGHT)
        