# category_view.py
#
# Category view for the stack window
from functools import partial
from PyQt6.QtWidgets import (
        QWidget,
        QLabel,
        QPushButton,
        QGridLayout,
        QSizePolicy
    )
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont
import game


class BoardView(QWidget):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.initUI()

    def initUI(self):
        self.layout = QGridLayout()
        font = self.controller.get_font("swiss911", 54)
        round = self.controller.get_round_data()
        self.category_labels = [None] * len(round.categories)
        for i, category in enumerate(round.categories):
            p = (0, i)
            cat_label = QLabel(category.title)
            cat_label.setSizePolicy(QSizePolicy.Policy.Expanding,
                                    QSizePolicy.Policy.Expanding)
            cat_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
            cat_label.setWordWrap(True)
            cat_label.setFont(font)
            cat_label.setStyleSheet("color: white;")
            self.layout.addWidget(cat_label, *p)
            self.category_labels[i] = cat_label
        font.setLetterSpacing(QFont.SpacingType.AbsoluteSpacing, 4)
        font.setPointSize(72)
        font.setBold(True)
        self.button_widgets = [[None
                                for j in range(len(round.categories[i].clues))]
                               for i in range(len(round.categories))]
        for i, category in enumerate(round.categories):
            for j, clue in enumerate(category.clues):
                p = (j+1, i)
                button = QPushButton(f"${clue.value}")
                button.setFont(font)
                button.setStyleSheet("color: #FFCC00;")
                # button.clicked.connect(
                        # partial(self.parent.show_clue, i, j))
                button.setSizePolicy(QSizePolicy.Policy.Expanding,
                                     QSizePolicy.Policy.Expanding)
                self.layout.addWidget(button, *p)
                self.button_widgets[i][j] = button
        self.setStyleSheet("background-color:#060CE9;")
        self.setLayout(self.layout)
        self.show()

    def update(self):
        round = self.controller.get_round_data()
        for i, category in enumerate(round.categories):
            self.category_labels[i].setText(category.title)
        for i, category in enumerate(round.categories):
            for j, clue in enumerate(category.clues):
                if clue.answered:
                    self.button_widgets[i][j].setEnabled(False)
                    self.button_widgets[i][j].setStyleSheet(
                            "background-color: #808080;")
                else:
                    self.button_widgets[i][j].setText(f"${clue.value}")
                    self.button_widgets[i][j].setEnabled(True)
                    self.button_widgets[i][j].setStyleSheet(
                            "background-color: #060CE9; color: #FFCC00")
