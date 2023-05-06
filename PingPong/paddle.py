from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, player_plane):
        super().__init__()
        self.player_plane = player_plane
        self.shape("square")
        self.color("white")
        self.shapesize(5.0, 1.0)
        self.penup()
        self.goto(self.player_plane * 350.0, 0.0)

    def up(self):
        if self.ycor() < 230:
            self.goto(self.xcor(), self.ycor() + 20)

    def down(self):
        if self.ycor() > -230:
            self.goto(self.xcor(), self.ycor() - 20)