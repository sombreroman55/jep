# player_view.py
#
# The widget for viewing the player
from functools import partial
from PyQt6.QtWidgets import QWidget, QHBoxLayout, QLabel, QVBoxLayout
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QLineEdit, QPushButton


class PlayerBarWidget(QWidget):
    def __init__(self, root, parent, model):
        super().__init__()
        self.root = root
        self.parent = parent
        self.model = model
        self.initUI()

    def initUI(self):
        self.layout = QHBoxLayout()
        self.player_widgets = list()
        for i in range(len(self.model.players)):
            player = self.model.players[i]
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
        for i in range(len(self.player_widgets)):
            self.player_widgets[i].update(self.model.players[i].score)
            if self.model.players[i].last:
                self.player_widgets[i].setStyleSheet("background-color:#068CE9")
            else:
                self.player_widgets[i].setStyleSheet("background-color:#060CE9")


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
        self.score_label.setText(f"${self.player.score}")
        if score < 0:
            self.score_label.setStyleSheet("color: red;")
        else:
            self.score_label.setStyleSheet("color: white;")
