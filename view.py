# view.py
#
# The root view window that is parent to all other widgets

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

from board import Board
from player_view import PlayerBarWidget

class View(QMainWindow):
    def __init__(self, model):
        super().__init__()
        self.model = model
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Jep with the Bois')
        self.central_widget = QWidget(self)
        self.layout = QVBoxLayout()
        self.main_content = Board(self, self.central_widget, self.model)
        self.player_bar = PlayerBarWidget(self, self.central_widget, self.model)
        self.layout.addWidget(self.main_content, 80)
        self.layout.addWidget(self.player_bar, 20)
        self.central_widget.setStyleSheet("background-color: black;")
        self.central_widget.setLayout(self.layout)
        self.setCentralWidget(self.central_widget)
        self.central_widget.show()
        self.showFullScreen()
        self.show()

    def update(self):
        new_round = self.model.check_next_round()
        self.main_content.update(new_round)
        self.player_bar.update()

    def keyPressEvent(self, event):
        s = event.text()
        if s.isdigit():
            if 1 <= int(s) <= len(self.model.players):
                self.model.curr_player = int(s)-1
        elif s == 'k':
            self.model.correct_answer()
            self.update()
        elif s == 'j':
            self.model.incorrect_answer()
            self.update()
        elif s == '!':
            self.model.reset_score()
            self.update()
        elif s == 'q':
            self.model.exit_game()
