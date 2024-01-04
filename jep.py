# jep.py
#
# The C in the MVC

import subprocess
from game import GameState
from view import View
from threading import Timer
from PyQt6.QtWidgets import QApplication


class Jep:
    def __init__(self):
        self.round = 1
        self.curr_player = 0
        self.curr_clue_row = 0
        self.curr_clue_col = 0
        self.wager_mode = False
        self.base_clue_value = 200 * self.round
        self.curr_clue_value = self.curr_clue_row * self.base_clue_value
        self.answer_timer = None
        self.sounds = {
                'daily_double': "resources/sounds/daily-double.mp3",
                'final_jep': "resources/sounds/final-jep.mp3",
                'jeopardy_theme': "resources/sounds/jeopardy-theme.mp3",
                'times_up': "resources/sounds/times-up.mp3"
                }

    def play(self):
        self.model = GameState()
        self.view = View(self)

    def update_state(self):
        # TODO: Update game state and UI elements
        pass

    def get_clue_data(self, category, clue):
        return self.model.get_clue_data(category, clue)

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

    def exit_game(self):
        self.clear_timer()
        QApplication.quit()
