# final_jep_view.py
#
# Clue view for the stack window
from PyQt6.QtWidgets import QVBoxLayout, QWidget, QLabel
from PyQt6.QtCore import Qt


class FinalJepView(QWidget):
    def __init__(self, state):
        super().__init__()
        self.game_state = state
        self.showing_cat = True
        self.initUI()

    def initUI(self):
        self.layout = QVBoxLayout()
        cat_font = self.game_state.get_font("swiss911", 54)
        clue_font = self.game_state.get_font("korina", 48)
        round = self.game_state.get_round_data()

        self.c_label = QLabel(round.categories[0].title)
        self.c_label.setFont(cat_font)
        self.c_label.setStyleSheet("color: white;")
        self.c_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.c_label.setWordWrap(True)

        self.q_label = QLabel(round.categories[0].clues[0].question)
        self.q_label.setFont(clue_font)
        self.q_label.setStyleSheet("color: white;")
        self.q_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.q_label.setWordWrap(True)

        self.a_label = QLabel(round.categories[0].clues[0].answer)
        self.a_label.setFont(clue_font)
        self.a_label.setStyleSheet("color: white;")
        self.a_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.a_label.setWordWrap(True)

        self.layout.addWidget(self.c_label)
        self.layout.addWidget(self.q_label)
        self.layout.addWidget(self.a_label)
        self.setLayout(self.layout)
        self.setStyleSheet("background-color:#060CE9;")
        self.show_category()
        self.show()

    def show_category(self):
        self.c_label.show()
        self.q_label.hide()
        self.a_label.hide()
        pass

    def show_clue(self):
        self.c_label.hide()
        self.q_label.show()
        self.a_label.hide()
        pass

    def show_answer(self):
        self.c_label.hide()
        self.q_label.show()
        self.a_label.show()
        pass

    def update(self):
        round = self.game_state.get_round_data()
        self.c_label.setText(round.categories[0].title)
        self.q_label.setText(round.categories[0].clues[0].question)
        self.a_label.setText(round.categories[0].clues[0].answer)


class WinnerView(QWidget):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.winner = self.controller.get_winner()
        self.initUI()

    def initUI(self):
        self.layout = QVBoxLayout()
        winner_font = self.controller.get_font("korina", 56)

        self.winner_label = QLabel(
                f"{self.winner.name} is the winner with ${self.winner.score}!")
        self.winner_label.setFont(winner_font)
        self.winner_label.setStyleSheet("color: white;")
        self.winner_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.winner_label.setWordWrap(True)

        self.layout.addWidget(self.winner_label)
        self.setLayout(self.layout)
        self.setStyleSheet("background-color:#060CE9;")
        self.show()

    def update(self):
        self.winner_label.setText(
                f"{self.winner.name} is the winner with ${self.winner.score}!")
