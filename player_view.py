# player_view.py
#
# The widget for viewing the player
from functools import partial
from PyQt6.QtWidgets import (
        QHBoxLayout,
        QLabel,
        QLineEdit,
        QPushButton,
        QVBoxLayout,
        QWidget,
    )
from PyQt6.QtCore import Qt


# TODO: Hook those buttons up to handlers to adjust score
# TODO: Add a wager mode UI to the player currently wagering and the amount
# TODO: Adjust the score handlers to use the wager amount in DD situations

class PlayerBarWidget(QWidget):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.initUI()

    def initUI(self):
        self.layout = QHBoxLayout()
        self.player_widgets = []
        players = self.controller.get_players()
        for i, player in enumerate(players):
            pw = PlayerWidget(player)
            pw.name_label.editingFinished.connect(
                        partial(self.update_name, i))
            self.player_widgets.append(pw)
            self.layout.addWidget(pw)
        self.setLayout(self.layout)
        self.show()

    def update_name(self, player):
        self.model.update_player_name(
                player, self.player_widgets[player].name_label.text())

    def update(self):
        for widget in self.player_widgets:
            # widget.update(self.model.players[i].score)
            widget.update(0)
            if widget.last:
                widget.setStyleSheet("background-color:#068CE9")
            else:
                widget.setStyleSheet("background-color:#060CE9")


class PlayerWidget(QWidget):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.initUI()

    def initUI(self):
        self.layout = QVBoxLayout()

        self.subtract_button = QPushButton("-")
        self.score_label = QLabel(f"${self.score}")
        self.add_button = QPushButton("+")
        score_font = self.score_label.font()
        score_font.setPointSize(32)
        self.score_label.setFont(score_font)
        self.score_label.setAlignment(Qt.AlignmentFlags.AlignCenter)
        self.score_label.setStyleSheet("color: white;")

        self.name_label = QLineEdit()
        name_font = self.name_label.font()
        name_font.setPointSize(32)
        self.name_label.setFont(name_font)
        self.name_label.setText(self.player.name)
        self.name_label.setAlignment(Qt.AlignmentFlags.AlignCenter)
        self.name_label.setStyleSheet("color: white;")

        self.layout.addWidget(self.score_label)
        self.layout.addWidget(self.name_label)
        self.setStyleSheet("background-color:#060CE9;")
        self.setLayout(self.layout)
        self.show()

    def update(self, score):
        self.score = score
        if score < 0:
            self.score_label.setText(f"${self.player.score}")
            self.score_label.setStyleSheet("color: red;")
        else:
            self.score_label.setText(f"-${abs(self.player.score)}")
            self.score_label.setStyleSheet("color: white;")
