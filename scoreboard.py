from turtle import Turtle

FONT = ("Courier", 24, "normal")
START_X_COORD = -200
START_Y_COORD = 260


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.color('black')
        self.penup()
        self.hideturtle()
        self.goto(START_X_COORD, START_Y_COORD)
        self.update_text()

    def update_text(self):
        self.clear()
        self.write(arg=f"LEVEL : {self.level}", move=False, align='center', font=FONT)

    def end_game_text(self):
        self.goto(0, 0)
        self.write(arg=f"GAME OVER", move=False, align='center', font=FONT)

    def increase_level(self):
        self.level += 1
        self.update_text()
