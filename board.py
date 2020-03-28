# board.py
#
# Creates and displays the Jep board
from PyQt5.QtWidgets import (QWidget, QGridLayout, QPushButton)

class Board(QWidget):
    def __init__(self):
        super().__init__()
        self.create_board()

    def create_board(self):
        self.setWindowTitle('Jep!')
        grid = QGridLayout()
        self.setLayout(grid)
        self.clues = ['C1', 'C2', 'C3', 'C4', 'C5', 'C6',
                      'Q1', 'Q1', 'Q1', 'Q1', 'Q1', 'Q1',
                      'Q2', 'Q2', 'Q2', 'Q2', 'Q2', 'Q2',
                      'Q3', 'Q3', 'Q3', 'Q3', 'Q3', 'Q3',
                      'Q4', 'Q4', 'Q4', 'Q4', 'Q4', 'Q4',
                      'Q5', 'Q5', 'Q5', 'Q5', 'Q5', 'Q5']
        pos = [(i, j) for i in range (6) for j in range(6)]
        for p, c in zip(pos, self.clues):
            button = QPushButton(c)
            grid.addWidget(button, *p)

        self.show()
