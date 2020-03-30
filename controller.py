# controller.py
#
# Controller component between model and view
from game import Game
from board import Board
from PyQt5.QtCore import Qt

CLUE_MULT = 200

class Controller:
    def __init__(self):
        self.model = Game(self)
        self.view = Board(self)
        self.curr_player = 1
        self.curr_clue_indices = (1, 1)
        self.curr_clue_value = CLUE_MULT * self.model.round
        self.curr_clue_value = self.curr_clue_indices[0] * self.base_clue_value

    def show_clue(self, i, j):
        print("Showing clue: ({}, {})".format(i, j))
        self.curr_clue_indices = (i, j)
        self.curr_clue_value = self.curr_clue_indices[0] * self.base_clue_value
        self.view.cluev.populate_clue(self.model.clues[i][j].question,
                                      self.model.clues[i][j].answer)
        self.view.show_clue()

    def clear_cell(self, row, col):
        self.model.clues[i][j].answered = True
        self.update_view()

    def correct_answer(self):
        self.model.adjust_score(player, self.curr_clue_value)
        self.model.set_last_player(player)

    def incorrect_answer(self):
        self.model.adjust_score(player, points * -1)
