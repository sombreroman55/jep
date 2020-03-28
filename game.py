# game.py
#
# Model of the Jep game

Player = namedtuple("Player", ["name", "score"])

@dataclass
class Player:
    name: str
    score: int = 0
    last: bool = False

class Game:
    def __init__(self):
        self.players = list()
        self.round = 1

    def add_player(self, name):
        player = Player(name)
        self.players.append(player)

    def adjust_score(self, player, amount):
        self.players[player].score += amount
