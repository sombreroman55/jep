# game.py
#
# Model of the Jep game

from dataclasses import dataclass
import random
import game_data as gd

class Clue:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer
        self.daily_double = False
        self.answered = False

@dataclass
class Player:
    name: str
    score: int = 0
    last: bool = False

class Game:
    def __init__(self, controller,):
        self.controller = controller
        self.players = list()
        self.round = 1
        self.data = gd.GameData()
        self.get_round_data(self.round)
        self.assign_daily_double()

    def get_round_data(self, r):
        self.categories = self.data.get_cats_for_round(r)
        qdata = self.data.get_questions_for_round(r)
        adata = self.data.get_answers_for_round(r)
        self.clues = [[Clue(qdata[i][j], adata[i][j]) \
                for j in range(6)] for i in range(5)]

    def check_next_round(self):
        clear = [[x.answered for x in row] for row in clues]
        if all(all(row) for row in clear):
            self.round += 1
            self.get_round_data(self.round)
            if self.round < 3:
                self.assign_daily_double()


    def add_player(self, name):
        player = Player(name)
        self.players.append(player)

    def adjust_score(self, player, amount):
        self.players[player].score += amount

    def set_last_player(self, player):
        self.players[player].last = True

    def assign_daily_double(self):
        assigned = 0
        while assigned < 2:
            rand_i = random.randint(2,4)
            rand_j = random.randint(0,5)
            if not self.clues[rand_i][rand_j].daily_double:
                self.clues[rand_i][rand_j].daily_double = True
                assigned += 1
