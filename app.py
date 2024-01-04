# jep.py
#
# The main Jep program
import sys

from PyQt6.QtWidgets import QApplication
from jep import Jep


def main():
    print("Welcome to Jep!")
    app = QApplication(sys.argv)
    jep = Jep()
    jep.play()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
