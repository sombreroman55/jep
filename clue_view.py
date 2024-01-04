# clue_view.py
#
# Clue view for the stack window
from PyQt6.QtWidgets import QLabel, QVBoxLayout, QWidget
from PyQt6.QtCore import Qt


class ClueView(QWidget):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.clue = None
        self.initUI()

    def initUI(self):
        self.layout = QVBoxLayout()
        font = self.controller.get_font("korina", 48)

        self.q_label = QLabel()
        self.q_label.setFont(font)
        self.q_label.setStyleSheet("color: white;")
        self.q_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.q_label.setWordWrap(True)

        self.a_label = QLabel()
        self.a_label.setFont(font)
        self.a_label.setStyleSheet("color: white;")
        self.a_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.a_label.setWordWrap(True)

        self.layout.addWidget(self.q_label)
        self.layout.addWidget(self.a_label)
        self.setLayout(self.layout)
        self.setStyleSheet("background-color:#060CE9;")
        self.show()

    def set_clue(self, clue):
        self.clue = clue
        self.a_label.hide()
        self.q_label.setText(self.clue.question)
        self.a_label.setText("A: " + self.clue.answer)
        self.q_label.show()

    def show_answer(self):
        self.q_label.show()
        self.a_label.show()

    def update(self):
        pass  # Nothing to update in clue view
