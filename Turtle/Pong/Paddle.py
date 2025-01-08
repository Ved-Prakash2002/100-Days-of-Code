from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, x_cor, y_cor):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color("white")
        self.penup()
        self.speed("fastest")
        self.goto(x_cor, y_cor)

    def up(self):
        if self.ycor() < 250:  # (screen.window_height() / 2 - rectangle_height / 2)
            self.sety(self.ycor() + 20)

    def down(self):
        if self.ycor() > -250:  # (-screen.window_height() / 2 + rectangle_height / 2)
            self.sety(self.ycor() - 20)
