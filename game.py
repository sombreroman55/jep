# game.py
#
# Model of the Jep game

Player = namedtuple("Player", ["name", "score"])

class Game:
    def __init__(self):
        self.players = list()
        self.round = 1
