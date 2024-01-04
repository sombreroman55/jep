# clue_view.py
#
# Clue view for the stack window
from PyQt6.QtWidgets import QLabel, QVBoxLayout, QWidget
from PyQt6.QtCore import Qt


class ClueView(QWidget):
    def __init__(self, parent, state):
        super().__init__()
        self.parent = parent
        self.game_state = state
        self.category = -1
        self.clue_num = -1
        self.clue = None
        self.showing_answer = False
        self.initUI()

    def initUI(self):
        self.layout = QVBoxLayout()
        font = self.game_state.get_font("korina", 48)

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

    def set_clue(self, category, clue_num, clue_data):
        self.category = category
        self.clue_num = clue_num
        self.clue = clue_data
        self.a_label.hide()
        self.q_label.setText(self.clue.question)
        self.a_label.setText("A: " + self.clue.answer)
        self.q_label.show()

    def show_answer(self):
        self.q_label.show()
        self.a_label.show()

    def update(self):
        pass  # Nothing to update in clue view

    def mousePressEvent(self, event):
        if not self.showing_answer:
            self.show_answer()
            self.showing_answer = True
        else:
            self.showing_answer = False
            self.game_state.mark_answered(self.category, self.clue_num)
            self.parent.show_board()
        self.parent.update_root()
