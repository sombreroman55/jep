# category_view.py
#
# Category view for the stack window
from functools import partial
from PyQt5.QtWidgets import (QWidget, QGridLayout, QPushButton, QLabel,
        QSizePolicy)
from PyQt5.QtCore import Qt
import controller

class CategoryView(QWidget):
    def __init__(self, parent, controller):
        super().__init__()
        self.controller = controller
        self.parent = parent
        self.create_board()
        self.show()

    def create_board(self):
        self.setWindowTitle('Jep!')
        grid = QGridLayout()
        self.setLayout(grid)
        for i in range(len(self.controller.model.categories)):
            p = (0, i)
            cat_label = QLabel(self.controller.model.categories[i])
            cat_label.setSizePolicy(QSizePolicy.Expanding, 
                                    QSizePolicy.Expanding)
            grid.addWidget(cat_label, *p)
        for i in range(len(self.controller.model.clues)):
            for j in range(len(self.controller.model.clues[i])):
                p = (i+1, j)
                button = QPushButton("${}".format(  
                                                (i+1) 
                                              * controller.CLUE_MULT
                                              * self.controller.model.round))
                button.clicked.connect(
                        partial(self.controller.show_clue, i, j))
                button.setSizePolicy(QSizePolicy.Expanding, 
                                     QSizePolicy.Expanding)
                grid.addWidget(button, *p)

    def keyPressEvent(self, event):
        pass

