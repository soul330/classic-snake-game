from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "bold")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("pink")
        self.penup()
        self.goto(0, 260)
        self.hideturtle()
        self.update_point()

    def update_point(self):
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)


    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def up_score(self):
        self.score += 1
        self.clear()
        self.update_point()
