# jep.py
#
# The main Jep program
import sys
from PyQt5.QtWidgets import QApplication, QWidget
from board import Board

if __name__ == "__main__":
    print("Welcome to Jep!")

    # Initialize GUI
    jep = QApplication([])
    
    board = Board()
    sys.exit(jep.exec_())

    # Initialize game data

    # Run game until finish
