# final_jep_view.py
#
# Clue view for the stack window
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class FinalJepView(QWidget):
    def __init__(self, root, parent, model):
        super().__init__()
        self.root = root
        self.parent = parent
        self.model = model
        self.showing_cat = True
        self.initUI()

    def initUI(self):
        print("init FinalJep UI")
        self.layout = QVBoxLayout()
        font_db = QFontDatabase()
        _id = font_db.addApplicationFont("./resources/fonts/swiss-911.ttf")
        cat_font = QFont("Swiss911 UCm BT", 54)
        font_db.addApplicationFont("./resources/fonts/korina-bold.ttf")
        clue_font = QFont("Korinna", 48)

        self.c_label.setFont(cat_font)
        self.c_label = QLabel(self.model.categories)
        self.c_label.setAlignment(Qt.AlignCenter)
        self.c_label.setWordWrap(True)

        self.q_label.setFont(clue_font)
        self.q_label = QLabel(self.model.clues.question)
        self.q_label.setAlignment(Qt.AlignCenter)
        self.q_label.setWordWrap(True)

        self.a_label.setFont(clue_font)
        self.a_label = QLabel(self.model.clues.answer)
        self.a_label.setAlignment(Qt.AlignCenter)
        self.a_label.setWordWrap(True)

        self.layout.addWidget(self.c_label)
        self.layout.addWidget(self.q_label)
        self.layout.addWidget(self.a_label)
        self.setLayout(self.layout)
        self.setStyleSheet("background-color:#060CE9;")
        self.show_category()
        self.show()

    def show_category(self):
        self.c_label.show()
        self.q_label.hide()
        self.a_label.hide()
        pass

    def show_clue(self):
        self.c_label.hide()
        self.q_label.show()
        self.a_label.hide()
        pass

    def show_answer(self):
        self.c_label.hide()
        self.q_label.show()
        self.a_label.show()
        pass

    def keyPressEvent(self, event):
        s = event.text()
        if s == ' ':
            if self.showing_cat:
                self.show_clue()
                self.showing_cat = False
            else:
                self.show_answer()
        elif event.key() == Qt.Key_Escape:
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


class WinnerView(QWidget):
    def __init__(self, root, parent, model):
        super().__init__()
        self.root = root
        self.parent = parent
        self.model = model
        self.initUI()

    def initUI(self):
        print("init Winner UI")
        self.layout = QVBoxLayout()
        font_db = QFontDatabase()
        font_db.addApplicationFont("./resources/fonts/korina-bold.ttf")
        winner_font = QFont("Korinna", 56)

        self.winner_label.setFont(cat_font)
        self.winner_label = QLabel("{} is the winner with ${}!".format(
                                    self.model.winner_name, 
                                    self.model.winner_score))
        self.winner_label.setAlignment(Qt.AlignCenter)
        self.winner_label.setWordWrap(True)

        self.layout.addWidget(self.winner_label)
        self.setLayout(self.layout)
        self.show()
