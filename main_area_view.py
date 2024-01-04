# view.py
#
# The view for Jep board

from PyQt6.QtWidgets import QLabel, QStackedWidget
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap

from board_view import BoardView
from clue_view import ClueView
from final_jep_view import FinalJepView, WinnerView


class MainArea(QStackedWidget):
    def __init__(self, root, controller):
        super().__init__()
        self.root = root
        self.controller = controller
        self.curr_view = "jeopardy-card"
        self.stack_idx = {
            "board": 0,
            "clue": 1,
            "final-jep": 2,
            "winner": 3,
            "jeopardy-card": 4,
            "oouble-jeopardy-card": 5,
            "daily-double-card": 6,
            "final-jeopardy-card": 7
        }
        self.initUI()

    def initUI(self):
        self.board_view = BoardView(self.controller)
        self.clue_view = ClueView(self.controller)
        self.final_jep_view = FinalJepView(self.controller)
        self.winner_view = WinnerView(self.controller)
        card_images = ["resources/img/jeopardy.jpg",
                       "resources/img/double-jeopardy.png",
                       "resources/img/daily-double.png",
                       "resources/img/final-jeopardy.jpg"]

        self.addWidget(self.board_view)
        self.addWidget(self.clue_view)
        self.addWidget(self.final_jep_view)
        self.addWidget(self.winner_view)
        for img in card_images:
            widget = self.init_image_card(img)
            self.addWidget(widget)

        self.setStyleSheet("background-color: black;")
        self.show_board()
        self.show()

    def init_image_card(self, image_path):
        image_card = QLabel(self)
        image_card.setPixmap(QPixmap("resources/img/jeopardy.jpg"))
        image_card.setAlignment(Qt.AlignmentFlag.AlignCenter)
        image_card.setScaledContents(True)
        image_card.resize(self.width(), self.height())
        return image_card

    def show_board(self):
        self.curr_view = "board"
        self.setCurrentIndex(self.stack_idx[self.curr_view])

    def show_clue(self, category, clue):
        clue = self.controller.get_clue_data(category, clue)
        self.clue_view.set_clue(clue)
        if clue.daily_double:
            # self.game_state.play_sound('daily_double')
            self.curr_view = "daily-double-card"
            self.setCurrentIndex(self.stack_idx[self.curr_view])
        else:
            self.curr_view = "clue"
            self.setCurrentIndex(self.stack_idx[self.curr_view])

    def show_final_jep(self):
        self.curr_view = "final-jep"
        self.setCurrentIndex(self.stack_idx[self.curr_view])

    def show_winner(self):
        self.curr_view = "winner"
        self.setCurrentIndex(self.stack_idx[self.curr_view])

    def update(self, new_round):
        if new_round:
            if self.game_state.round == 1:
                self.show_card(self.SJ_CARD)
            elif self.game_state.round == 2:
                self.show_card(self.DJ_CARD)
            elif self.game_state.round == 3:
                self.show_card(self.FJ_CARD)
        self.board_view.update()
        self.clue_view.update()
        self.final_jep_view.update()
        self.winner_view.update()

    def keyPressEvent(self, event):
        s = event.text()
        if s == 'n':
            if (self.curr_view == "jeopardy-card" or
                    self.curr_view == "double-jeopardy-card"):
                self.show_board()
            elif self.curr_view == "double-jeopardy-card":
                self.curr_view = "clue"
            elif self.curr_view == "final-jeopardy-card":
                self.show_final_jep()
                self.game_state.play_sound('final_jep')
            self.setCurrentIndex(self.stack_idx[self.curr_view])
        elif s == 'q':
            self.game_state.exit_game()
        else:
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
                elif s == 'c':
                    self.game_state.reset_wager()
                elif s == 'w':
                    self.game_state.wager_mode = False
