# jep.py
#
# The main Jep program
import sys
from PyQt6.QtWidgets import QApplication
from game import Game


def main():
    print("Welcome to Jep!")

    # Initialize GUI
    jep = QApplication(sys.argv)

    # Initialize game data
    game = Game(jep)
    game.play()


if __name__ == "__main__":
    main()
