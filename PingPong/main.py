from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.title("Ping-Pong")
screen.bgcolor("black")
screen.tracer(0)


paddle1 = Paddle(1)
paddle2 = Paddle(-1)
ball = Ball()
score1 = ScoreBoard(1, "P1")
score2 = ScoreBoard(-1, "P2")

screen.listen()
screen.onkey(paddle1.up, "Up")
screen.onkey(paddle1.down, "Down")
screen.onkey(paddle2.up, "w")
screen.onkey(paddle2.down, "s")
game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    if ball.ycor() >= 280 or ball.ycor() <= -280:
        ball.y_facing *= -1

    if (ball.distance(paddle1) < 50 or ball.distance(paddle2) < 50) \
            and (ball.xcor() >= 330 or ball.xcor() <= -330):
        ball.x_facing *= -1
        ball.move_speed *= 0.8

    if ball.xcor() >= 420:
        score2.refresh()
        ball.out_of_bound()

    if ball.xcor() <= -420:
        score1.refresh()
        ball.out_of_bound()

    if score1.score == 10 or score2.score == 10:
        game_is_on = False
        score1.result()
        score2.result()
        ball.color("black")

screen.exitonclick()
