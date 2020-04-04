# jep.py
#
# The main Jep program
import sys

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

from game import Game
from view import View

def main():
    print("Welcome to Jep!")

    # Initialize GUI
    jep = QApplication([])
    
    # Initialize game data
    game = Game()
    view = View(game)

    # Run game until finish
    sys.exit(jep.exec_())

if __name__ == "__main__":
    main()
