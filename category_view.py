# category_view.py
#
# Category view for the stack window
from functools import partial
from PyQt6.QtWidgets import QWidget, QLabel, QPushButton
from PyQt6.QtCore import Qt, QGridLayout
from PyQt6.QtGui import QFont, QFontDatabase
import game


class CategoryView(QWidget):
    def __init__(self, root, parent, model):
        super().__init__()
        self.root = root
        self.parent = parent
        self.model = model
        self.initUI()

    def initUI(self):
        self.layout = QGridLayout()
        font_db = QFontDatabase()
        _ = font_db.addApplicationFont("./resources/fonts/swiss-911.ttf")
        font = QFont("Swiss911 UCm BT", 54)
        self.category_labels = [None for i in range(len(self.model.categories))]
        for i in range(len(self.model.categories)):
            p = (0, i)
            cat_label = QLabel(self.model.categories[i])
            cat_label.setSizePolicy(Qt.QSizePolicy.Expanding,
                                    Qt.QSizePolicy.Expanding)
            cat_label.setAlignment(Qt.AlignCenter)
            cat_label.setWordWrap(True)
            cat_label.setFont(font)
            cat_label.setStyleSheet("color: white;")
            self.layout.addWidget(cat_label, *p)
            self.category_labels[i] = cat_label
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
                    f"${(i+1) * game.CLUE_MULT * self.model.round}")
                button.setFont(font)
                button.setStyleSheet("color: #FFCC00;")
                button.clicked.connect(
                        partial(self.parent.show_clue, i, j))
                button.setSizePolicy(Qt.QSizePolicy.Expanding,
                                     Qt.QSizePolicy.Expanding)
                self.layout.addWidget(button, *p)
                self.button_widgets[i][j] = button
        self.setStyleSheet("background-color:#060CE9;")
        self.setLayout(self.layout)
        self.show()

    def update(self):
        for i in range(len(self.model.categories)):
            self.category_labels[i].setText(self.model.categories[i])
        for i in range(len(self.model.clues)):
            for j in range(len(self.model.clues[i])):
                if self.model.clues[i][j].answered:
                    self.button_widgets[i][j].setEnabled(False)
                    self.button_widgets[i][j].setStyleSheet(
                            "background-color: #808080;")
                else:
                    self.button_widgets[i][j].setText(
                        "${}".format((i+1) * game.CLUE_MULT * self.model.round))
                    self.button_widgets[i][j].setEnabled(True)
                    self.button_widgets[i][j].setStyleSheet(
                            "background-color: #060CE9; color: #FFCC00")

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
        elif s == '!':
            self.model.reset_score()
            self.root.update()
        elif s == 'q':
            self.model.exit_game()
