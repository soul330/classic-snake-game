from turtle import Turtle
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snakey:

    def __init__(self):
        self.snake_parts = []
        self.create_snakey()
        self.head = self.snake_parts[0]

    def create_snakey(self):
        for position in STARTING_POSITIONS:
            self.add_snakey_part(position)

    def add_snakey_part(self, position):
        snake_part = Turtle(shape="square")
        snake_part.color("green")
        snake_part.penup()
        snake_part.goto(position)
        self.snake_parts.append(snake_part)

    def expand(self):
        self.add_snakey_part(self.snake_parts[-1].position())

    def move(self):
        for part_num in range(len(self.snake_parts) - 1, 0, -1):
            new_x = self.snake_parts[part_num - 1].xcor()
            new_y = self.snake_parts[part_num - 1].ycor()
            self.snake_parts[part_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
