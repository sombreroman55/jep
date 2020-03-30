# clue_view.py
#
# Clue view for the stack window
from PyQt5.QtWidgets import (QWidget, QGridLayout, QPushButton, QLabel,
        QVBoxLayout, QSizePolicy)
from PyQt5.QtCore import Qt

class ClueView(QWidget):
    def __init__(self, parent, controller):
        super().__init__()
        self.parent = parent
        self.controller = controller
        self.layout = QVBoxLayout()
        self.q_label = QLabel()
        self.a_label = QLabel()
        self.layout.addWidget(self.q_label)
        self.layout.addWidget(self.a_label)
        self.setLayout(self.layout)
        self.show()

    def populate_clue(self, question, answer):
        self.a_label.hide()
        self.q_label.setText(question)
        self.a_label.setText("A: " + answer)
        self.q_label.show()

    def show_answer(self):
        self.a_label.show()

    def keyPressEvent(self, event):
        print("Clue key press!")
        s = event.text()
        if s == ' ':
            self.show_answer()
        elif event.key() == Qt.Key_Escape:
            self.parent.show_categories()
        elif s.isdigit():
            print(int(s))
            if 1 <= int(s) <= len(self.controller.model.players):
                self.controller.curr_player = int(s)
                print(self.controller.curr_player)
        elif s == 'g':
            self.controller.
            pass # Correct answer
        elif s == 'b':
            pass # Incorrect answer
