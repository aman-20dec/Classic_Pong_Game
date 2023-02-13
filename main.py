from pickle import TRUE
from turtle import Turtle, Screen
from ball import Ball
from paddles import Paddle
from scoreboard import Scoreboard

import time


screen = Screen()

screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")

screen.tracer(0)

left_paddle = Paddle("left")
right_paddle = Paddle("right")
ball = Ball()
scorecard = Scoreboard()

screen.listen()
screen.onkey(left_paddle.move_up, "a")
screen.onkey(right_paddle.move_up, "k")
screen.onkey(left_paddle.move_down, "z")
screen.onkey(right_paddle.move_down, "m")

game_continue = True
ball_speed = .1


while game_continue:
    time.sleep(ball_speed)
    screen.update()
    ball.move()

    if (right_paddle.distance(ball) < 50 and ball.xcor() > 335) or (left_paddle.distance(ball) < 50 and ball.xcor() < -340): 
        # game_continue = False
        ball.paddle_deflect()
        ball_speed *= .9
    
    if ball.xcor() < -370:
         ball.game_reset()
         scorecard.r_scored()
         ball_speed = .1


    if ball.xcor() > 360:
        ball.game_reset()
        scorecard.l_scored()
        ball_speed = .1

    if scorecard.l_score >=5 or scorecard.r_score >=5:
        game_continue = False

screen.exitonclick()