# view.py
#
# The view for Jep board

from PyQt6.QtWidgets import QLabel, QStackedWidget
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap

from category_view import CategoryView
from clue_view import ClueView
from final_jep_view import FinalJepView, WinnerView


class Board(QStackedWidget):
    def __init__(self, root, parent, game_state):
        super().__init__()
        self.root = root
        self.parent = parent
        self.game_state = game_state
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
        self.category_view = CategoryView(self.root, self, self.game_state)
        self.clue_view = ClueView(self.root, self, self.game_state)
        self.final_jep_view = FinalJepView(self.root, self, self.game_state)
        self.winner_view = WinnerView(self.root, self, self.game_state)

        self.sj_card = self.init_image_card("resources/img/jeopardy.jpg")
        self.dj_card = self.init_image_card("resources/img/double-jeopardy.jpg")
        self.dd_card = self.init_image_card("resources/img/daily-double.jpg")
        self.fd_card = self.init_image_card("resources/img/final-jeopardy.jpg")

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

    def init_image_card(self, image_path):
        image_card = QLabel(self)
        image_card.setPixmap(QPixmap("resources/img/jeopardy.jpg"))
        image_card.setAlignment(Qt.AlignmentFlag.AlignCenter)
        image_card.setScaledContents(True)
        image_card.resize(self.width(), self.height())
        return image_card

    def show_categories(self):
        self.curr_index = self.CAT_IND
        self.setCurrentIndex(self.curr_index)

    def show_clue(self, i, j):
        self.game_state.curr_clue_row = i
        self.game_state.curr_clue_col = j
        self.game_state.curr_clue_value = \
            (self.game_state.curr_clue_row+1) * self.game_state.base_clue_value
        self.clue_view.populate_clue(self.game_state.clues[i][j].question,
                                     self.game_state.clues[i][j].answer)
        if self.game_state.clues[i][j].daily_double:
            self.game_state.play_sound('daily_double')
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
            if self.game_state.round == 1:
                self.show_card(self.SJ_CARD)
            elif self.game_state.round == 2:
                self.show_card(self.DJ_CARD)
            elif self.game_state.round == 3:
                self.show_card(self.FJ_CARD)
        self.category_view.update()
        self.clue_view.update()
        self.final_jep_view.update()
        self.winner_view.update()

    def keyPressEvent(self, event):
        s = event.text()
        if not self.game_state.wager_mode:
            if s.isdigit():
                if 1 <= int(s) <= len(self.game_state.players):
                    self.game_state.curr_player = int(s)-1
            elif s == 'k':
                self.game_state.correct_answer()
                self.root.update()
            elif s == 'j':
                self.game_state.incorrect_answer()
                self.root.update()
            elif s == 'n':
                if self.curr_index == self.SJ_CARD or self.curr_index == self.DJ_CARD:
                    self.show_categories()
                elif self.curr_index == self.DD_CARD:
                    self.curr_index = self.CLUE_IND
                elif self.curr_index == self.FJ_CARD:
                    self.show_final_jep()
                    self.game_state.play_sound('final_jep')
                self.setCurrentIndex(self.curr_index)
            elif s == 'q':
                self.game_state.exit_game()
            elif s == 'w':
                self.game_state.wager_mode = True
            elif s == '!':
                self.game_state.reset_score()
                self.root.update()
        else:
            if s.isdigit():
                self.game_state.update_wager(int(s))
            elif s == 'k':
                self.game_state.correct_wager()
                self.root.update()
            elif s == 'j':
                self.game_state.incorrect_wager()
                self.root.update()
            elif s == 'n':
                if self.curr_index == self.SJ_CARD or self.curr_index == self.DJ_CARD:
                    self.show_categories()
                elif self.curr_index == self.DD_CARD:
                    self.curr_index = self.CLUE_IND
                elif self.curr_index == self.FJ_CARD:
                    self.show_final_jep()
                    self.game_state.play_sound('final_jep')
                self.setCurrentIndex(self.curr_index)
            elif s == 'q':
                self.game_state.exit_game()
            elif s == 'c':
                self.game_state.reset_wager()
            elif s == 'w':
                self.game_state.wager_mode = False
