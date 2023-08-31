from turtle import Screen
from paddles import Paddle
from ball import Ball
from scoreboard import Scoreboard
from wall import Wall
import time

window = Screen()
window.bgcolor("black")
window.setup(width = 800, height = 600)
window.title("Pong")
window.tracer(0) # block the animation

# Create the objects
right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))
ball = Ball()
score = Scoreboard("Player 1", "Player 2")
wall = Wall()

# paddles movement
window.listen()
window.onkeypress(key = "Up", fun = right_paddle.paddle_up)
window.onkeypress(key = "Down", fun = right_paddle.paddle_down)

window.onkeypress(key = "w", fun = left_paddle.paddle_up)
window.onkeypress(key = "s", fun = left_paddle.paddle_down)

is_game_on = True
speed = 0.08 # ball's speed

while is_game_on:
    window.update() # refresh the screen
    time.sleep(speed)
    ball.move()

    if ball.ycor() > 260 or ball.ycor() < -250:
        # if the ball hits the wall
        ball.step_y *= -1

    if ball.distance(right_paddle) < 50 and ball.xcor() > 320 or ball.distance(left_paddle) < 50 and ball.xcor() < -320:
        # if the ball hits the paddle
        ball.step_x *= -1
        if speed > 0.02:
            speed -= 0.005

    if ball.xcor() < -380:
        # if the ball goes out from the left side
        ball.ball_goes_out()
        score.right_plus("Player 1", "Player 2")
        speed = 0.08

    if ball.xcor() > 380:
        # if the ball goes out from the right side
        ball.ball_goes_out()
        score.left_plus("Player 1", "Player 2")
        speed = 0.08


    if score.l_score == 3 or score.r_score == 3:
        # if left player's or right player's score is equals to 3
        is_game_on = False

        wall.clean_window()
        window.update()

        if score.l_score > score.r_score:
            score.game_over("Player 1")

        else:
            score.game_over("Player 2")


# Press 'ESC' to exit at the end of the game
window.onkey(key = "Escape", fun = window.bye)
window.mainloop()