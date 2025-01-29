from turtle import Turtle

LIGHT_PINK = '#f7aab2'
BG_COLOUR = '#48091a'
FONT = ('Major Mono Display', 16, 'bold')
GAME_OVER_FONT = ('Major Mono Display', 40, 'bold')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open('data.txt', mode='r') as data:
            self.highest_score = int(data.read())
        self.penup()
        self.hideturtle()
        self.color(LIGHT_PINK)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto((-285, 270))
        self.write(arg=f'SCORE: {self.score}', align='left', font=FONT)
        self.goto((260, 270))
        self.write(arg=f'HIGH SCORE: {self.highest_score}', align='right', font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def reset_score(self):
        if self.score > int(self.highest_score):
            self.highest_score = self.score
            with open('data.txt', mode='w') as file:
                file.write(str(self.highest_score))
        self.score = 0
        self.update_scoreboard()

    # def game_over(self):
        # self.goto(0, 0)
        # self.color(LIGHT_PINK)
        # self.write(align='center', arg='GAME OVER', font=GAME_OVER_FONT)

