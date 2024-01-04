# jep.py
#
# The main Jep program
import sys

from PyQt6.QtWidgets import QApplication
from game import GameState
from view import View


def main():
    print("Welcome to Jep!")
    app = QApplication(sys.argv)
    game_state = GameState()
    view = View(game_state)
    view.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
