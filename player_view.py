# player_view.py
#
# The widget for viewing the player
from functools import partial

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

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
            pw = PlayerWidget(player.name, player.score)
            pw.name_label.editingFinished.connect(
                        partial(self.update_name, i))
            self.player_widgets.append(pw)
            self.layout.addWidget(pw)
        self.setLayout(self.layout)
        self.show()

    def update_name(self, player):
        self.model.update_player_name(player, self.player_widgets[player].name_label.text())

    def update(self):
        for i in range(len(self.player_widgets)):
            self.player_widgets[i].update(self.model.players[i].score)
            if self.model.players[i].last:
                self.player_widgets[i].setStyleSheet("background-color:#068CE9")
            else:
                self.player_widgets[i].setStyleSheet("background-color:#060CE9")

    def keyPressEvent(self, event):
        s = event.text()
        if s.isdigit():
            if 1 <= int(s) <= len(self.controller.model.players):
                self.model.curr_player = int(s)-1
        elif s == 'k':
            self.model.correct_answer()
            self.root.update()
        elif s == 'j':
            self.model.incorrect_answer()
            self.root.update()
        elif s == '!':
            self.model.reset_score()
            self.root.update()
        elif s == 'q':
            QCoreApplication.quit()



class PlayerWidget(QWidget):
    def __init__(self, name, score):
        super().__init__()
        self.name = name
        self.score = score
        self.initUI()

    def initUI(self):
        self.layout = QVBoxLayout()

        self.score_label = QLabel("${}".format(self.score))
        score_font = self.score_label.font()
        score_font.setPointSize(32)
        self.score_label.setFont(score_font)
        self.score_label.setAlignment(Qt.AlignCenter)
        self.score_label.setStyleSheet("color: white;")

        self.name_label = QLineEdit()
        name_font = self.name_label.font()
        name_font.setPointSize(32)
        self.name_label.setFont(name_font)
        self.name_label.setText(self.name)
        self.name_label.setAlignment(Qt.AlignCenter)
        self.name_label.setStyleSheet("color: white;")

        self.layout.addWidget(self.score_label)
        self.layout.addWidget(self.name_label)
        self.setStyleSheet("background-color:#060CE9;")
        self.setLayout(self.layout)
        self.show()

    def update(self, score):
        self.score = score
        if score < 0:
            self.score_label.setStyleSheet("color: red;")
            self.score_label.setText("-${}".format(self.score * -1))
        else:
            self.score_label.setStyleSheet("color: white;")
            self.score_label.setText("${}".format(self.score))
