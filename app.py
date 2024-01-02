# jep.py
#
# The main Jep program
import sys

from PyQt6.QtWidgets import QApplication
from game import Jep


def main():
    print("Welcome to Jep!")
    app = QApplication([])

    jep = Jep()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
