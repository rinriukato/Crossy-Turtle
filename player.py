from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(STARTING_POSITION)
        self.color('black')
        self.shape('turtle')
        self.setheading(90)  # North

    def move(self):
        self.forward(MOVE_DISTANCE)

    def reset_pos(self):
        self.goto(STARTING_POSITION)

    def is_at_finish_line(self) -> bool:
        return self.ycor() >= FINISH_LINE_Y

    def set_dead(self):
        self.hideturtle()
