from turtle import Turtle, position, setheading
X_LEFT_POS = -370
X_RIGHT_POS = 360
Y_POS = 5

class Paddle(Turtle):
    def __init__(self, side):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=4, stretch_len=1)
        
        if side == "left":
            self.setposition(X_LEFT_POS,Y_POS)
        else:
            self.setposition(X_RIGHT_POS,Y_POS)

    def move_up(self):
        position = list(self.pos())
        position[1] += 30
        if position[1] < 270:
            self.goto(position)

    def move_down(self):
        position = list(self.pos())
        position[1] -= 30
        if position[1] > -265:
            self.goto(position)