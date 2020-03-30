# jep.py
#
# The main Jep program
import sys
import time
from PyQt5.QtGui import QPixmap 
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from controller import Controller

def main():
    print("Welcome to Jep!")

    # Initialize GUI
    jep = QApplication([])
    # splash = QLabel()
    # splash.setPixmap(QPixmap('resources/jeopardy-logo.jpeg'))
    # splash.show()
    # time.sleep(3)
    # splash.close()
    
    # Initialize game data
    controller = Controller()

    # Run game until finish
    sys.exit(jep.exec_())

if __name__ == "__main__":
    main()
