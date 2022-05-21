from turtle import Screen
from snakey import Snakey
import time
from food import Food
from scoreboard import Scoreboard

# Windows setup
window_screen = Screen()
window_screen.setup(width=600, height=600)
window_screen.bgcolor("black")
window_screen.title("Welcome to Snake In The Grass Game!")
window_screen.tracer(0)

snakey = Snakey()
food = Food()
scoreboard = Scoreboard()

window_screen.listen()
window_screen.onkey(snakey.up, "Up")
window_screen.onkey(snakey.down, "Down")
window_screen.onkey(snakey.left, "Left")
window_screen.onkey(snakey.right, "Right")


game_is_on = True
while game_is_on:
    window_screen.update()
    time.sleep(0.1)
    snakey.move()

    # Inspect collision with food.
    if snakey.head.distance(food) < 15:
        food.refresh()
        snakey.expand()
        scoreboard.up_score()

    # Inspect collision with wall.
    if snakey.head.xcor() > 280 or snakey.head.xcor() < -280 or snakey.head.ycor() > 280 or snakey.head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()

    # Inspect collision with snake tail. #SIMPLIFIED VERSION
    for snakey_part in snakey.snake_parts[1:]:
        if snakey.head.distance(snakey_part) < 10:
            game_is_on = False
            scoreboard.game_over()

    # Inspect collision with snake tail. # UN-SIMPLIFIED VERSION
    # for snakey_part in snakey.snake_parts:
    #     if snakey_part == snakey.head:
    #         pass
    #     elif snakey.head.distance(snakey_part) < 10:
    #         game_is_on = False
    #         scoreboard.game_over()
    # If the head snake collide with any part in the tail, GAME OVER! trigger game_over

    # for par in snake_parts:
    #     par.forward(20)


# snakey_2 = Turtle(shape="square")
# snakey_2.color("white")
# snakey_2.goto(-20, 0)
#
# snakey_3 = Turtle(shape="square")
# snakey_3.color("white")
# snakey_3.goto(-40, 0)

window_screen.exitonclick()
