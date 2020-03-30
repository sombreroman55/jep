# view.py
#
# The view for Jep board
from PyQt5.QtWidgets import (QWidget, QGridLayout, QPushButton, QLabel,
        QStackedWidget, QSizePolicy)
from PyQt5.QtCore import Qt
from category_view import CategoryView
from clue_view import ClueView

CAT_IND = 0
CLUE_IND = 1
FJ_CAT_IND = 2
FJ_CLUE_IND = 3

class Board(QStackedWidget):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.categoryv = CategoryView(self, self.controller)
        self.cluev = ClueView(self, self.controller)
        self.addWidget(self.categoryv)
        self.addWidget(self.cluev)
        self.curr_index = CAT_IND
        self.setCurrentIndex(self.curr_index)
        self.show()

    def show_categories(self):
        self.curr_index = CAT_IND
        self.setCurrentIndex(self.curr_index)

    def show_clue(self):
        self.curr_index = CLUE_IND
        self.setCurrentIndex(self.curr_index)

    def keyPressEvent(self, event):
        pass
