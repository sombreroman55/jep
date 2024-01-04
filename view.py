# view.py
#
# The root view window that is parent to all other widgets

from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget, QMainWindow, QVBoxLayout
from main_area_view import MainArea
from player_view import PlayerBarWidget


class View(QMainWindow):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Jep with the Bois')
        self.root_widget = QWidget(self)
        self.layout = QVBoxLayout()
        self.main_area = MainArea(self, self.controller)
        self.player_bar = PlayerBarWidget(self.controller)
        self.layout.addWidget(self.main_area, 80)
        self.layout.addWidget(self.player_bar, 20)
        self.root_widget.setStyleSheet("background-color: black;")
        self.root_widget.setLayout(self.layout)
        self.setCentralWidget(self.root_widget)
        self.root_widget.show()
        self.showFullScreen()
        self.show()

    def update(self):
        new_round = self.model.check_next_round()
        self.main_area.update(new_round)
        self.player_bar.update()

    def keyPressEvent(self, event):
        s = event.key()
        if s == Qt.Key.Key_Q.value:
            self.controller.handle_exit_game()
