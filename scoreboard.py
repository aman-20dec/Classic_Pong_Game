from turtle import Turtle, goto

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()

        self.draw_median()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.draw_score()


    def draw_median(self):
        self.goto(0, 250)
        self.seth(270)
        self.pensize(width=5)
        while self.ycor() > -250:
            self.forward(20)
            if self.isdown():
                self.penup()
            else:
                self.pendown()
        self.penup()
        self.seth(0)
        
    def l_scored(self):
        self.l_score+=1
        self.draw_score()

    def r_scored(self):
        self.r_score+=1
        self.draw_score()

    def draw_score(self):
        self.clear()
        self.goto(-100, 240)
        self.write(self.l_score, align="center", font=("Arial", 50, "normal" ))
        self.forward(200)
        self.write(self.r_score, align="center", font=("Arial", 50, "normal" ))

