from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self, l_player, r_player):
        super().__init__()

        self.color("white")
        self.hideturtle()
        self.penup()

        self.l_score = 0
        self.r_score = 0

        self.refresh_score(l_player, r_player)


    def refresh_score(self, l_player, r_player):
        # Write player names and scores
        self.clear()

        self.goto(-290, 240)
        self.write(f"{l_player}", align = "center", font = ("Courier", 24, "normal") )

        self.goto(290, 240)
        self.write(f"{r_player}", align = "center", font = ("Courier", 24, "normal"))

        self.goto(-100, 170)
        self.write(f"{self.l_score}", align = "center", font = ("Courier", 80, "normal"))

        self.goto(100, 170)
        self.write(f"{self.r_score}", align = "center", font = ("Courier", 80, "normal"))        


    def right_plus(self, l_player, r_player):
        # increase the right player's score by 1
        self.r_score += 1
        self.refresh_score(l_player, r_player)


    def left_plus(self, l_player, r_player):
        # increase the left player's score by 1
        self.l_score += 1
        self.refresh_score(l_player, r_player)


    def game_over(self, winner):
        self.goto(0, 30)
        self.write("Game Over", align = "center", font = ("Courier", 40, "normal"))

        self.goto(0, -30)
        self.write(f"{winner} is the Winner", align = "center", font = ("Courier", 30, "normal"))

        self.goto(0, -100)
        self.write("Press 'ESC' to Exit", align = "center", font = ("Courier", 30, "normal"))