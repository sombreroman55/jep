# player_view.py
#
# The widget for viewing the player
from PyQt6.QtWidgets import (
        QHBoxLayout,
        QLabel,
        QLineEdit,
        QPushButton,
        QVBoxLayout,
        QWidget,
    )
from PyQt6.QtCore import Qt


class PlayerBarWidget(QWidget):
    def __init__(self, root, state):
        super().__init__()
        self.root = root
        self.game_state = state
        self.initUI()

    def initUI(self):
        self.layout = QHBoxLayout()
        self.player_widgets = []
        players = self.game_state.get_players()
        for i, player in enumerate(players):
            pw = PlayerWidget(self, player, i, self.game_state)
            pw.name_label.editingFinished.connect(lambda: self.update_name(i))
            self.player_widgets.append(pw)
            self.layout.addWidget(pw)
        self.setLayout(self.layout)
        self.show()

    def set_clue_value(self, value):
        for p in self.player_widgets:
            p.set_clue_value(value)

    def player_wager(self):
        players = self.game_state.get_players()
        for i, p in enumerate(players):
            if p.last:
                self.player_widgets[i].player_wager()

    def all_wager(self):
        for p in self.player_widgets:
            p.player_wager()

    def update_root(self):
        self.root.update()

    def update_name(self, player):
        self.game_state.update_player_name(
                player, self.player_widgets[player].name_label.text())

    def update(self):
        players = self.game_state.get_players()
        for i, player in enumerate(players):
            self.player_widgets[i].update(player)


class PlayerWidget(QWidget):
    def __init__(self, parent, player, idx, state):
        super().__init__()
        self.parent = parent
        self.game_state = state
        self.index = idx
        self.initUI(player)

    def initUI(self, player):
        self.layout = QVBoxLayout()

        self.adjust_bar = QWidget()
        self.adjust_layout = QHBoxLayout()
        self.subtract_button = QPushButton("-")
        self.value_label = QLineEdit("")
        value_font = self.value_label.font()
        value_font.setPointSize(24)
        self.value_label.setFont(value_font)
        self.value_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.value_label.setStyleSheet("color: white;")
        self.add_button = QPushButton("+")
        self.adjust_layout.addWidget(self.subtract_button, 15)
        self.adjust_layout.addWidget(self.value_label, 70)
        self.adjust_layout.addWidget(self.add_button, 15)
        self.adjust_bar.setLayout(self.adjust_layout)
        self.subtract_button.clicked.connect(
                lambda: self.incorrect_answer())

        self.add_button.clicked.connect(
                lambda: self.correct_answer())

        self.score_label = QLabel(f"${player.score}")
        score_font = self.score_label.font()
        score_font.setPointSize(32)
        self.score_label.setFont(score_font)
        self.score_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.score_label.setStyleSheet("color: white;")

        self.name_label = QLineEdit()
        name_font = self.name_label.font()
        name_font.setPointSize(32)
        self.name_label.setFont(name_font)
        self.name_label.setText(player.name)
        self.name_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.name_label.setStyleSheet("color: white;")

        self.layout.addWidget(self.adjust_bar)
        self.layout.addWidget(self.score_label)
        self.layout.addWidget(self.name_label)
        self.setStyleSheet("background-color:#060CE9;")
        self.setLayout(self.layout)
        self.show()

    def correct_answer(self):
        self.game_state.correct_answer(
                self.index, int(self.value_label.text()))
        self.parent.update_root()

    def incorrect_answer(self):
        self.game_state.incorrect_answer(
                self.index, int(self.value_label.text()))
        self.parent.update_root()

    def player_wager(self):
        self.value_label.setText(str(""))
        self.value_label.setEnabled(True)

    def set_clue_value(self, value):
        self.value_label.setText(str(value))
        self.value_label.setEnabled(False)

    def update(self, player):
        if player.last:
            self.setStyleSheet("background-color:#068CE9")
        else:
            self.setStyleSheet("background-color:#060CE9")

        if player.score >= 0:
            self.score_label.setText(f"${player.score}")
            self.score_label.setStyleSheet("color: white;")
        else:
            self.score_label.setText(f"-${abs(player.score)}")
            self.score_label.setStyleSheet("color: red;")
