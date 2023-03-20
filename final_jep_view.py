# final_jep_view.py
#
# Clue view for the stack window
from PyQt6.QtWidgets import QVBoxLayout, QWidget, QLabel
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont, QFontDatabase


class FinalJepView(QWidget):
    def __init__(self, root, parent, model):
        super().__init__()
        self.root = root
        self.parent = parent
        self.model = model
        self.showing_cat = True
        self.initUI()

    def initUI(self):
        self.layout = QVBoxLayout()
        font_db = QFontDatabase()
        _id = font_db.addApplicationFont("./resources/fonts/swiss-911.ttf")
        cat_font = QFont("Swiss911 UCm BT", 54)
        font_db.addApplicationFont("./resources/fonts/korina-bold.ttf")
        clue_font = QFont("Korinna", 48)

        self.c_label = QLabel(self.model.categories[0])
        self.c_label.setFont(cat_font)
        self.c_label.setStyleSheet("color: white;")
        self.c_label.setAlignment(Qt.AlignCenter)
        self.c_label.setWordWrap(True)

        self.q_label = QLabel(self.model.clues[0][0].question)
        self.q_label.setFont(clue_font)
        self.q_label.setStyleSheet("color: white;")
        self.q_label.setAlignment(Qt.AlignCenter)
        self.q_label.setWordWrap(True)

        self.a_label = QLabel(self.model.clues[0][0].answer)
        self.a_label.setFont(clue_font)
        self.a_label.setStyleSheet("color: white;")
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

    def update(self):
        self.c_label.setText(self.model.categories[0])
        self.q_label.setText(self.model.clues[0][0].question)
        self.a_label.setText(self.model.clues[0][0].answer)

    def keyPressEvent(self, event):
        s = event.text()
        if not self.model.wager_mode:
            if s == ' ':
                if self.showing_cat:
                    self.show_clue()
                    self.showing_cat = False
                else:
                    self.show_answer()
            elif event.key() == Qt.Key_Escape:
                self.root.update()
                self.parent.show_winner()
            elif s.isdigit():
                if 1 <= int(s) <= len(self.model.players):
                    self.model.curr_player = int(s)-1
            elif s == 's':
                self.model.play_sound('jeopardy_theme')
            elif s == 'q':
                self.model.exit_game()
            elif s == '!':
                self.model.reset_score()
                self.root.update()
            elif s == 'w':
                self.model.wager_mode = True
        else:
            if s.isdigit():
                self.model.update_wager(int(s))
            elif s == 'k':
                self.model.correct_wager()
                self.root.update()
            elif s == 'j':
                self.model.incorrect_wager()
                self.root.update()
            elif s == 'c':
                self.model.reset_wager()
            elif s == 'w':
                self.model.wager_mode = False


class WinnerView(QWidget):
    def __init__(self, root, parent, model):
        super().__init__()
        self.root = root
        self.parent = parent
        self.model = model
        self.initUI()

    def initUI(self):
        self.layout = QVBoxLayout()
        font_db = QFontDatabase()
        font_db.addApplicationFont("./resources/fonts/korina-bold.ttf")
        winner_font = QFont("Korinna", 56)

        self.winner_label = QLabel("{} is the winner with ${}!".format(
                                  self.model.players[self.model.winning_player].name,
                                  self.model.players[self.model.winning_player].score))
        self.winner_label.setFont(winner_font)
        self.winner_label.setStyleSheet("color: white;")
        self.winner_label.setAlignment(Qt.AlignCenter)
        self.winner_label.setWordWrap(True)

        self.layout.addWidget(self.winner_label)
        self.setLayout(self.layout)
        self.setStyleSheet("background-color:#060CE9;")
        self.show()

    def update(self):
        self.winner_label.setText("{} is the winner with ${}!".format(
                                  self.model.players[self.model.winning_player].name,
                                  self.model.players[self.model.winning_player].score))

    def keyPressEvent(self, event):
        s = event.text()
        if s == 'q':
            self.model.exit_game()
