from turtle import Turtle

class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0,270)
        self.write(f"Score = {self.score}" , align = 'center', font = ("Courier",12,"normal"))
        self.hideturtle()
        
    def inc_score(self):
        self.clear()
        self.score += 1
        self.write(f"Score = {self.score}" , align = 'center', font = ("Courier",12,"normal"))
        
    def game_over(self):
        self.clear()
        self.goto(0,0)
        self.write("GAME OVER", align= 'center', font = ("Courier",24,"bold"))
        self.goto(0,-20)
        self.write(f"You Scored {self.score}", align= 'center', font = ("Courier",12,"normal"))
        
    def booster(self):
        self.clear()
        self.color('blue')
        
    def reset(self):
        self.color('white')
        
        
        