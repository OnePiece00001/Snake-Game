from turtle import Turtle
ALLIGN = "center"
FONT = ("Arial", 20, "normal")
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.count = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.write(f"Score = {self.count}", align = ALLIGN, font = FONT)

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align = ALLIGN, font = FONT)
        
    
    def foodcount(self):
        self.count += 1
        self.clear() #clear the written text
        self.update_score()
        