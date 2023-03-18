# view.py
#
# The view for Jep board
from PyQt5.QtWidgets import QLabel, QStackedWidget
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap

from category_view import CategoryView
from clue_view import ClueView
from final_jep_view import FinalJepView, WinnerView

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
        self.SJ_CARD = 4
        self.DJ_CARD = 5
        self.DD_CARD = 6
        self.FJ_CARD = 7

        self.initUI()

    def initUI(self):
        self.category_view = CategoryView(self.root, self, self.model)
        self.clue_view = ClueView(self.root, self, self.model)
        self.final_jep_view = FinalJepView(self.root, self, self.model)
        self.winner_view = WinnerView(self.root, self, self.model)

        self.sj_card = QLabel(self)
        self.sj_card.setPixmap(QPixmap("resources/img/jeopardy.jpg"))
        self.sj_card.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.sj_card.setScaledContents(True)
        self.sj_card.resize(self.width(), self.height())
        self.sj_card.show()

        self.dj_card = QLabel(self)
        self.dj_card.setPixmap(QPixmap("resources/img/double-jeopardy.png"))
        self.dj_card.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.dj_card.setScaledContents(True)
        self.dj_card.resize(self.width(), self.height())
        self.dj_card.show()

        self.dd_card = QLabel(self)
        self.dd_card.setPixmap(QPixmap("resources/img/daily-double.png"))
        self.dd_card.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.dd_card.setScaledContents(True)
        self.dd_card.resize(self.width(), self.height())
        self.dd_card.show()

        self.fj_card = QLabel(self)
        self.fj_card.setPixmap(QPixmap("resources/img/final-jeopardy.jpg"))
        self.fj_card.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.fj_card.setScaledContents(True)
        self.fj_card.resize(self.width(), self.height())
        self.fj_card.show()

        self.addWidget(self.category_view)
        self.addWidget(self.clue_view)
        self.addWidget(self.final_jep_view)
        self.addWidget(self.winner_view)
        self.addWidget(self.sj_card)
        self.addWidget(self.dj_card)
        self.addWidget(self.dd_card)
        self.addWidget(self.fj_card)

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
        if self.model.clues[i][j].daily_double:
            self.model.play_sound('daily_double')
            self.show_card(self.DD_CARD)
        else:
            self.curr_index = self.CLUE_IND
            self.setCurrentIndex(self.curr_index)

    def show_final_jep(self):
        self.curr_index = self.FJ_IND
        self.setCurrentIndex(self.curr_index)

    def show_winner(self):
        self.curr_index = self.WINNER_IND
        self.setCurrentIndex(self.curr_index)

    def show_card(self, ind):
        if ind == self.SJ_CARD:
            self.curr_index = self.SJ_CARD
        elif ind == self.DJ_CARD:
            self.curr_index = self.DJ_CARD
        elif ind == self.DD_CARD:
            self.curr_index = self.DD_CARD
        elif ind == self.FJ_CARD:
            self.curr_index = self.FJ_CARD
        self.setCurrentIndex(self.curr_index)

    def update(self, new_round):
        if new_round:
            if self.model.round == 1:
                self.show_card(self.SJ_CARD)
            elif self.model.round == 2:
                self.show_card(self.DJ_CARD)
            elif self.model.round == 3:
                self.show_card(self.FJ_CARD)
        self.category_view.update()
        self.clue_view.update()
        self.final_jep_view.update()
        self.winner_view.update()

    def keyPressEvent(self, event):
        s = event.text()
        if not self.model.wager_mode:
            if s.isdigit():
                if 1 <= int(s) <= len(self.model.players):
                    self.model.curr_player = int(s)-1
            elif s == 'k':
                self.model.correct_answer()
                self.root.update()
            elif s == 'j':
                self.model.incorrect_answer()
                self.root.update()
            elif s == 'n':
                if self.curr_index == self.SJ_CARD or self.curr_index == self.DJ_CARD:
                    self.show_categories()
                elif self.curr_index == self.DD_CARD:
                    self.curr_index = self.CLUE_IND
                elif self.curr_index == self.FJ_CARD:
                    self.show_final_jep()
                    self.model.play_sound('final_jep')
                self.setCurrentIndex(self.curr_index)
            elif s == 'q':
                self.model.exit_game()
            elif s == 'w':
                self.model.wager_mode = True
            elif s == '!':
                self.model.reset_score()
                self.root.update()
        else:
            if s.isdigit():
                self.model.update_wager(int(s))
            elif s == 'k':
                self.model.correct_wager()
                self.root.update()
            elif s == 'j':
                self.model.incorrect_wager()
                self.root.update()
            elif s == 'n':
                if self.curr_index == self.SJ_CARD or self.curr_index == self.DJ_CARD:
                    self.show_categories()
                elif self.curr_index == self.DD_CARD:
                    self.curr_index = self.CLUE_IND
                elif self.curr_index == self.FJ_CARD:
                    self.show_final_jep()
                    self.model.play_sound('final_jep')
                self.setCurrentIndex(self.curr_index)
            elif s == 'q':
                self.model.exit_game()
            elif s == 'c':
                self.model.reset_wager()
            elif s == 'w':
                self.model.wager_mode = False
