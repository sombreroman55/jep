# game.py
#
# Model of the Jep game

from dataclasses import dataclass
import random

import game_data as gd

CLUE_MULT = 200

class Clue:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer
        self.daily_double = False
        self.answered = False

@dataclass
class Player:
    name: str = ""
    score: int = 0
    last: bool = False

class Game:
    def __init__(self):
        self.players = [Player() for i in range(4)]
        self.round = 1
        self.curr_player = 1
        self.curr_clue_row = 0
        self.curr_clue_col = 0
        self.base_clue_value = CLUE_MULT * self.round
        self.curr_clue_value = self.curr_clue_row * self.base_clue_value
        self.data = gd.GameData()
        self.get_round_data(self.round)
        self.assign_daily_double()

    def get_round_data(self, r):
        self.categories = self.data.get_cats_for_round(r)
        qdata = self.data.get_questions_for_round(r)
        adata = self.data.get_answers_for_round(r)
        if self.round < 3:
            self.clues = [[Clue(qdata[i][j], adata[i][j]) \
                    for j in range(6)] for i in range(5)]
        else:
            self.clues = Clue(qdata, adata)

    def check_next_round(self):
        clear = [[x.answered for x in row] for row in clues]
        if all(all(row) for row in clear):
            self.round += 1
            self.get_round_data(self.round)
            if self.round < 3:
                self.assign_daily_double()

    def set_wager(self, score):
        self.curr_clue_value = score
        print(self.curr_clue_value)

    def mark_answered(self):
        self.clues[self.curr_clue_row][self.curr_clue_col].answered = True

    def update_player_name(self, player, name):
        self.players[player].name = name

    def correct_answer(self):
        self.players[self.curr_player].score += self.curr_clue_value
        self.players[self.curr_player].last = True

    def incorrect_answer(self):
        self.players[self.curr_player].score += self.curr_clue_value * -1

    def assign_daily_double(self):
        assigned = 0
        while assigned < self.round:
            rand_i = random.randint(2,4)
            rand_j = random.randint(0,5)
            if not self.clues[rand_i][rand_j].daily_double:
                self.clues[rand_i][rand_j].daily_double = True
                assigned += 1
