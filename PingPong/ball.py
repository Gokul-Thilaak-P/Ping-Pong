from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.y_facing = 1
        self.x_facing = 1
        self.move_speed = 0.1
        self.shape("circle")
        self.color("white")
        self.penup()

    def move(self):
        self.goto(self.xcor() + (10 * self.x_facing), self.ycor() + (10 * self.y_facing))

    def out_of_bound(self):
        self.x_facing *= -1
        if self.xcor() > 0:
            self.y_facing = -1
        else:
            self.y_facing = 1
        self.move_speed = 0.1
        self.home()
