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
        print("init PlayerBar UI")
        self.layout = QHBoxLayout()
        self.player_widgets = list()
        for player in self.model.players:
            pw = PlayerWidget(player.name, player.score)
            pw.name_le.editingFinished.connect(
                    lambda(player.name = pw.name_le.text()))
            self.player_widgets.append(pw)
            self.layout.addWidget(pw)
        self.setLayout(self.layout)
        self.show()

    def update(self):
        for i in range(len(self.player_widgets)):
            self.player_widgets[i].update(self.model.players[i].score)

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
        elif s == 'q':
            QCoreApplication.quit()



class PlayerWidget(QWidget):
    def __init__(self, player):
        super().__init__()
        self.player = player
        self.initUI()

    def initUI(self):
        print("init Player UI")
        self.layout = QVBoxLayout()

        self.score_label = QLabel("${}".format(self.player.score))
        score_font = self.score_label.font()
        score_font.setPointSize(32)
        self.score_label.setFont(score_font)
        self.score_label.setAlignment(Qt.AlignCenter)
        self.score_label.setStyleSheet("color:#FFFFFF;")

        self.name_le = QLineEdit()
        name_font = self.name_le.font()
        name_font.setPointSize(32)
        self.name_le.setFont(name_font)
        self.name_le.setText(self.player.name)
        self.name_le.setAlignment(Qt.AlignCenter)
        self.name_le.setStyleSheet("color:#FFFFFF;")

        self.layout.addWidget(self.score_label)
        self.layout.addWidget(self.name_le)
        self.setStyleSheet("background-color:#060CE9;")
        self.setLayout(self.layout)
        self.show()

    def update(self, score):
        self.score = score
        if score < 0:
            self.score_label.setStyleSheet("color:#FF0000;")
            self.score_label.setText("-${}".format(self.score * -1))
        else:
            self.score_label.setStyleSheet("color:#FFFFFF;")
            self.score_label.setText("${}".format(self.score))

    def keyPressEvent(self, event):
        s = event.text()
        if s.isdigit():
            if 1 <= int(s) <= len(self.model.players):
                self.model.curr_player = int(s)-1
        elif s == 'k':
            self.model.correct_answer()
            self.root.update()
        elif s == 'j':
            self.model.incorrect_answer()
            self.root.update()
        elif s == 'q':
            QCoreApplication.quit()
