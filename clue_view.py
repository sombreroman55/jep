# clue_view.py
#
# Clue view for the stack window
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class ClueView(QWidget):
    def __init__(self, root, parent, model):
        super().__init__()
        self.root = root
        self.parent = parent
        self.model = model
        self.initUI()

    def initUI(self):
        print("init ClueView UI")
        self.layout = QVBoxLayout()
        font_db = QFontDatabase()
        _id = font_db.addApplicationFont("./resources/fonts/korina-bold.ttf")
        font = QFont("Korinna", 48)
        self.q_label = QLabel()
        self.a_label = QLabel()
        self.q_label.setFont(font)
        self.q_label.setStyleSheet("color: white;")
        self.a_label.setFont(font)
        self.a_label.setStyleSheet("color: white;")
        self.q_label.setAlignment(Qt.AlignCenter)
        self.a_label.setAlignment(Qt.AlignCenter)
        self.q_label.setWordWrap(True)
        self.a_label.setWordWrap(True)
        self.layout.addWidget(self.q_label)
        self.layout.addWidget(self.a_label)
        self.setLayout(self.layout)
        self.setStyleSheet("background-color:#060CE9;")
        self.show()

    def populate_clue(self, question, answer):
        self.a_label.hide()
        self.q_label.setText(question)
        self.a_label.setText("A: " + answer)
        self.q_label.show()

    def show_answer(self):
        self.q_label.show()
        self.a_label.show()

    def update(self):
        pass  # Nothing to update in clue view

    def keyPressEvent(self, event):
        s = event.text()
        if s == ' ':
            self.show_answer()
        elif event.key() == Qt.Key_Escape:
            self.model.mark_answered()
            self.root.update()
            self.parent.show_categories()
        elif s.isdigit():
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
