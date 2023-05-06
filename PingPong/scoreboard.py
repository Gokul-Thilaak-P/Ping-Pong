from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self, player_plane, player_name):
        super().__init__()
        self.player_name = player_name
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(100.0*player_plane, 200.0)
        self.write(self.score, align= "center", font=("arial",75 ,"normal"))

    def refresh(self):
        self.clear()
        self.score += 1
        self.write(self.score, align="center", font=("arial", 75, "normal"))

    def result(self):
        if self.score == 10:
            self.home()
            self.write(f"GAME OVER\n      {self.player_name} wins", align="center", font=("arial", 25, "normal"))