from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.width(20)
        self.penup()
        self.x_move = 10
        self.y_move = 10

    def move(self):
        
        x_cor = self.xcor() + self.x_move
        y_cor = self.ycor() + self.y_move
        self.goto(x_cor, y_cor)
        if y_cor > 295 or y_cor < -295:
            self.y_move *= -1

    def paddle_deflect(self):      
        
        self.x_move *= -1
    
    def game_reset(self):
        self.goto(0,0)
        self.paddle_deflect()