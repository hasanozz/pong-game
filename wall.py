from turtle import Turtle


class Wall():

    def __init__(self):
        self.wall_parts = []
        self.wall_positions = []
        self.x = -400
        self.y = 290


        for i in range(95):
            # Create wall positions
            if i < 40:
                self.wall_positions.append((self.x, self.y))
                self.x += 20
            
            elif i == 40:
                self.x = 0
                self.y -= 50
                self.wall_positions.append((self.x, self.y))
            
            elif i < 54:
                self.wall_positions.append((self.x, self.y))
                self.y -= 40

            elif i == 54:
                self.x = -400
                # self.y -= 10
                self.wall_positions.append((self.x, self.y))

            else:
                self.wall_positions.append((self.x, self.y))
                self.x += 20

            # Create Wall objects
            self.new_part = Turtle("square")
            self.wall_parts.append(self.new_part)
            self.wall_parts[i].color("white")
            self.wall_parts[i].penup()
            self.wall_parts[i].goto(self.wall_positions[i])

    def clean_window(self):
        # clear screen at the end of the game
        for i in range(95):
            self.wall_parts[i].color("black")