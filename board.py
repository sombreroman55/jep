# view.py
#
# The view for Jep board
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

from category_view import CategoryView
from clue_view import ClueView

class Board(QStackedWidget):
    def __init__(self, root, parent, model):
        super().__init__()
        self.root = root
        self.parent = parent
        self.model = model 
        self.CAT_IND = 0
        self.CLUE_IND = 1
        self.FJ_IND = 2
        self.WINNER_IND = 3

        self.initUI()

    def initUI(self):
        print("init Board UI")
        self.category_view = CategoryView(self.root, self, self.model)
        self.clue_view = ClueView(self.root, self, self.model)
        self.final_jep_view = FinalJepView(self.root, self, self.model)
        self.winner_view = WinnerView(self.root, self, self.model)
        self.addWidget(self.category_view)
        self.addWidget(self.clue_view)
        self.addWidget(self.final_jep_view)
        self.addWidget(self.winner_view)
        self.setStyleSheet("background-color: black;")
        self.show_categories()
        self.show()

    def show_categories(self):
        self.curr_index = self.CAT_IND
        self.setCurrentIndex(self.curr_index)

    def show_clue(self, i, j):
        self.model.curr_clue_row = i
        self.model.curr_clue_col = j
        self.model.curr_clue_value = \
                (self.model.curr_clue_row+1) * self.model.base_clue_value
        self.clue_view.populate_clue(self.model.clues[i][j].question,
                                     self.model.clues[i][j].answer)
        self.curr_index = self.CLUE_IND
        self.setCurrentIndex(self.curr_index)

    def show_final_jep(self):
        self.curr_index = self.FJ_IND
        self.setCurrentIndex(self.curr_index)

    def show_winner(self):
        self.curr_index = self.WINNER_IND
        self.setCurrentIndex(self.curr_index)

    def update(self):
        self.category_view.update()
        self.clue_view.update()

    def keyPressEvent(self, event):
        s = event.text()
        if s.isdigit():
            if 1 <= int(s) <= len(self.model.players):
                self.model.curr_player = int(s)-1
                print(self.model.curr_player)
        elif s == 'k':
            self.model.correct_answer()
            self.root.update()
        elif s == 'j':
            self.model.incorrect_answer()
            self.root.update()
        elif s == 'q':
            QCoreApplication.quit()
