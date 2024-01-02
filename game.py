# game.py
#
# Game state data and functions for Jep

from dataclasses import dataclass
import sys
import json
import random
import subprocess
from threading import Timer
from PyQt5.QtCore import QCoreApplication


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


class Jep:
    def __init__(self):
        self.load_clues()
        self.players = [Player() for _ in range(3)]
        self.round = 1
        self.curr_player = 0
        self.curr_clue_row = 0
        self.curr_clue_col = 0
        self.wager_mode = False
        self.base_clue_value = 200 * self.round
        self.curr_clue_value = self.curr_clue_row * self.base_clue_value
        self.initialize_clues(self.round)
        self.assign_daily_double()
        self.answer_timer = None
        self.sounds = {
                'daily_double': "resources/sounds/daily-double.mp3",
                'final_jep': "resources/sounds/final-jep.mp3",
                'jeopardy_theme': "resources/sounds/jeopardy-theme.mp3",
                'times_up': "resources/sounds/times-up.mp3"
                      }

    def play(self):
        # TODO: Initialize UI and own it
        pass

    def load_clues(self):
        with open('clues.json') as cluefile:
            self.clues = json.load(cluefile)
            print(self.clues)
            sys.exit(1)

    def create_UI(self):
        # TODO: Create UI elements
        pass

    def update_state(self):
        # TODO: Update game state and UI elements
        pass

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
                self.base_clue_value = 200 * self.round
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

    def correct_answer(self, player, value):
        self.players[player].score += value
        self.set_last_player()
        self.clear_timer()

    def incorrect_answer(self, player, value):
        self.players[player].score -= value
        self.reset_timer()

    def reset_wager(self, player):
        self.players[self.curr_player].wager = 0

    def update_wager(self, digit):
        self.players[self.curr_player].wager *= 10
        self.players[self.curr_player].wager += digit

    def reset_score(self, player):
        self.players[player].score = 0

    def reset_timer(self):
        self.clear_timer()
        self.answer_timer = Timer(20, self.play_sound, args=['times_up'])
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
            rand_i = random.randint(2, 4)
            rand_j = random.randint(0, 5)
            if (rand_j != used_col and
               not self.clues[rand_i][rand_j].daily_double):
                self.clues[rand_i][rand_j].daily_double = True
                used_col = rand_j
                assigned += 1

    def exit_game(self):
        self.clear_timer()
        QCoreApplication.quit()
