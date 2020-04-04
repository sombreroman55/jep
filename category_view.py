# category_view.py
#
# Category view for the stack window
from functools import partial

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

import game

class CategoryView(QWidget):
    def __init__(self, root, parent, model):
        super().__init__()
        self.root = root
        self.parent = parent
        self.model = model
        self.initUI()

    def initUI(self):
        print("init CategoryView UI")
        self.layout = QGridLayout()
        font_db = QFontDatabase()
        _id = font_db.addApplicationFont("./resources/fonts/swiss-911.ttf")
        font = QFont("Swiss911 UCm BT", 54)
        for i in range(len(self.model.categories)):
            p = (0, i)
            cat_label = QLabel(self.model.categories[i])
            cat_label.setSizePolicy(QSizePolicy.Expanding, 
                                    QSizePolicy.Expanding)
            cat_label.setAlignment(Qt.AlignCenter)
            cat_label.setWordWrap(True)
            cat_label.setFont(font)
            cat_label.setStyleSheet("color: white;")
            self.layout.addWidget(cat_label, *p)
        font.setLetterSpacing(QFont.AbsoluteSpacing, 4)
        font.setPointSize(72)
        font.setBold(True)
        self.button_widgets = [[None 
                                for j in range(len(self.model.clues[i]))]
                                for i in range(len(self.model.clues))]
        for i in range(len(self.model.clues)):
            for j in range(len(self.model.clues[i])):
                p = (i+1, j)
                button = QPushButton(
                    "${}".format((i+1) * game.CLUE_MULT * self.model.round))
                button.setFont(font)
                button.setStyleSheet("color: #FFCC00;")
                button.clicked.connect(
                        partial(self.parent.show_clue, i, j))
                button.setSizePolicy(QSizePolicy.Expanding, 
                                     QSizePolicy.Expanding)
                self.layout.addWidget(button, *p)
                self.button_widgets[i][j] = button
        self.setStyleSheet("background-color:#060CE9;")
        self.setLayout(self.layout)
        self.show()

    def update(self):
        for i in range(len(self.model.clues)):
            for j in range(len(self.model.clues[i])):
                if self.model.clues[i][j].answered:
                    self.button_widgets[i][j].setEnabled(False)
                    self.button_widgets[i][j].setStyleSheet(
                            "background-color: #808080;")

    def keyPressEvent(self, event):
        s = event.text()
        if s.isdigit():
            if 1 <= int(s) <= len(self.model.players):
                self.model.curr_player = int(s)-1
                print(self.model.curr_player)
        elif s == 'k':
            self.model.correct_answer()
            self.root.update()
        elif s == 'j':
            self.model.incorrect_answer()
            self.root.update()
        elif s == 'q':
            QCoreApplication.quit()
