# view.py
#
# The root view window that is parent to all other widgets

from PyQt6.QtWidgets import QWidget, QMainWindow, QVBoxLayout
from main_area_view import MainArea
from player_view import PlayerBarWidget


class View(QMainWindow):
    def __init__(self, state):
        super().__init__()
        self.game_state = state
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Jep with the Bois')
        self.root_widget = QWidget(self)
        self.layout = QVBoxLayout()
        self.main_area = MainArea(self, self.game_state)
        self.player_bar = PlayerBarWidget(self.game_state)
        self.layout.addWidget(self.main_area, 80)
        self.layout.addWidget(self.player_bar, 20)
        self.root_widget.setStyleSheet("background-color: black;")
        self.root_widget.setLayout(self.layout)
        self.setCentralWidget(self.root_widget)
        self.root_widget.show()
        self.showFullScreen()

    def update(self):
        # new_round = self.model.check_next_round()
        is_next_round = self.game_state.check_next_round()
        self.main_area.update(is_next_round)
        self.player_bar.update()
