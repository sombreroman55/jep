# game.py
#
# Model of the Jep game

from dataclasses import dataclass
import random
import subprocess
from threading import Timer

from PyQt5.QtCore import QCoreApplication

import game_data as gd

CLUE_MULT = 200
ANSWER_TIME = 20

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
    wager: int = 0
    last: bool = False

class Game:
    def __init__(self):
        self.players = [Player() for _ in range(3)]
        self.round = 1
        self.winning_player = 0
        self.curr_player = 0
        self.curr_clue_row = 0
        self.curr_clue_col = 0
        self.wager_mode = False
        self.base_clue_value = CLUE_MULT * self.round
        self.curr_clue_value = self.curr_clue_row * self.base_clue_value
        self.data = gd.GameData()
        self.get_round_data(self.round)
        self.assign_daily_double()
        self.answer_timer = None
        self.sounds = {
                'daily_double'   : "resources/sounds/daily-double.mp3",
                'final_jep'      : "resources/sounds/final-jep.mp3",
                'jeopardy_theme' : "resources/sounds/jeopardy-theme.mp3",
                'times_up'       : "resources/sounds/times-up.mp3"
                      }

    def get_round_data(self, r):
        self.categories = self.data.get_cats_for_round(r)
        qdata = self.data.get_questions_for_round(r)
        adata = self.data.get_answers_for_round(r)
        if self.round < 3:
            self.clues = [[Clue(qdata[i][j], adata[i][j]) \
                    for j in range(6)] for i in range(5)]
        else:
            self.clues = [[Clue(qdata[i][j], adata[i][j]) \
                    for j in range(1)] for i in range(1)]

    def check_next_round(self):
        clear = [[x.answered for x in row] for row in self.clues]
        if all(all(row) for row in clear):
            self.round += 1
            if self.round >= 4:
                return
            self.get_round_data(self.round)
            if self.round < 3:
                self.base_clue_value = CLUE_MULT * self.round
                self.assign_daily_double()
            return True
        return False

    def mark_answered(self):
        self.clues[self.curr_clue_row][self.curr_clue_col].answered = True
        self.clear_timer()

    def update_player_name(self, player, name):
        self.players[player].name = name

    def set_last_player(self):
        for player in self.players:
            if player == self.players[self.curr_player]:
                player.last = True
            else:
                player.last = False


    def correct_answer(self):
        self.players[self.curr_player].score += self.curr_clue_value
        self.set_last_player()
        if self.players[self.curr_player].score > self.players[self.winning_player].score:
            self.winning_player = self.curr_player
        self.reset_timer()

    def incorrect_answer(self):
        self.players[self.curr_player].score += self.curr_clue_value * -1
        self.reset_timer()

    def reset_wager(self):
        self.players[self.curr_player].wager = 0

    def update_wager(self, digit):
        self.players[self.curr_player].wager *= 10
        self.players[self.curr_player].wager += digit

    def correct_wager(self):
        self.players[self.curr_player].score += self.players[self.curr_player].wager
        self.set_last_player()
        self.reset_timer()

    def incorrect_wager(self):
        self.players[self.curr_player].score += self.players[self.curr_player].wager * -1
        self.reset_timer()

    def reset_score(self):
        self.players[self.curr_player].score = 0

    def reset_timer(self):
        if self.answer_timer:
            self.answer_timer.cancel()
        self.answer_timer = None
        self.answer_timer = Timer(ANSWER_TIME, self.play_sound, args=['times_up'])
        self.answer_timer.daemon = True
        self.answer_timer.start()

    def clear_timer(self):
        if self.answer_timer:
            self.answer_timer.cancel()
        self.answer_timer = None

    def play_sound(self, sound):
        self.sound_process = subprocess.Popen(["mpv", self.sounds[sound]])

    def assign_daily_double(self):
        assigned = 0
        used_col = -1
        while assigned < self.round:
            rand_i = random.randint(2,4)
            rand_j = random.randint(0,5)
            if (rand_j != used_col and
                not self.clues[rand_i][rand_j].daily_double):
                self.clues[rand_i][rand_j].daily_double = True
                used_col = rand_j
                assigned += 1

    def exit_game(self):
        self.clear_timer()
        QCoreApplication.quit()
