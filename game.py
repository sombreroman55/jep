# game.py
#
# Game state data and functions for Jep

import json
import random
from PyQt6.QtCore import QUrl
from PyQt6.QtMultimedia import QSoundEffect
from PyQt6.QtGui import QFont, QFontDatabase


class FontManager:
    def __init__(self):
        self.fonts = {
            "swiss911": "./resources/fonts/swiss-911.ttf",
            "korina": "./resources/fonts/korina-bold.ttf"
        }
        self.font_ids = {}

        for k, v in self.fonts.items():
            font_id = QFontDatabase.addApplicationFont(v)
            self.font_ids[k] = font_id

    def get_custom_font(self, font, point_size):
        font = QFontDatabase.applicationFontFamilies(self.font_ids[font])[0]
        return QFont(font, point_size)


class SoundManager:
    def __init__(self):
        self.sounds = {
                'daily_double': "resources/sounds/daily-double.wav",
                'final_jep': "resources/sounds/final-jep.wav",
                'jeopardy_theme': "resources/sounds/jeopardy-theme.wav",
                'opening': "resources/sounds/opening.wav"
                }
        self.sound = None

    def play_sound(self, sound):
        self.sound = QSoundEffect()
        self.sound.setSource(QUrl.fromLocalFile(self.sounds[sound]))
        self.sound.setLoopCount(1)
        self.sound.play()


class Clue:
    def __init__(self, q, a, val, media):
        self.question = q
        self.answer = a
        self.value = val
        self.media = media
        self.answered = False
        self.daily_double = False

    def mark_answered(self):
        self.answered = True

    def set_daily_double(self):
        self.daily_double = True


class Category:
    def __init__(self, title, clues):
        self.title = title
        self.clues = clues


class Round:
    def __init__(self, categories):
        self.categories = categories


class GameData:
    def __init__(self, rounds):
        self.rounds = rounds


class Player:
    def __init__(self):
        self.name = ""
        self.score = 0
        self.last = False


class GameState:
    def __init__(self):
        self.fonts = FontManager()
        self.sounds = SoundManager()
        self.players = [Player() for _ in range(4)]
        self.players[0].last = True
        self.curr_round = 0
        self.curr_player = 0
        self.wager_mode = False
        self.answer_timer = None
        self.load_clues()
        self.assign_daily_double()

    def load_clues(self):
        with open('clues.json') as cluefile:
            clues = json.load(cluefile)
        rounds = []
        for round in clues["rounds"]:
            categories = []
            for cat in round["categories"]:
                title = cat["title"]
                clues = []
                for clue in cat["clues"]:
                    q = clue["q"]
                    a = clue["a"]
                    val = clue["value"]
                    media = clue["media"]
                    c = Clue(q, a, val, media)
                    clues.append(c)
                c = Category(title, clues)
                categories.append(c)
            r = Round(categories)
            rounds.append(r)
        self.game_data = GameData(rounds)

    def play_sound(self, sound):
        self.sounds.play_sound(sound)

    def get_font(self, font, point_size):
        return self.fonts.get_custom_font(font, point_size)

    def get_round_data(self):
        return self.game_data.rounds[self.curr_round]

    def get_clue_data(self, category, clue):
        return (self.game_data
                .rounds[self.curr_round]
                .categories[category]
                .clues[clue])

    def get_winner(self):
        winner = max(range(len(self.players)),
                     key=lambda i: self.players[i].score)
        return self.players[winner]

    def check_next_round(self):
        if all(all(clue.answered for clue in category.clues) for category in
               self.game_data.rounds[self.curr_round].categories):
            self.curr_round += 1
            if self.curr_round >= 3:
                return False
            if self.curr_round < 2:
                self.assign_daily_double()
            return True
        return False

    def mark_answered(self, category, clue):
        self.game_data\
            .rounds[self.curr_round]\
            .categories[category]\
            .clues[clue].mark_answered()

    def get_players(self):
        return self.players

    def update_player_name(self, player, name):
        self.players[player].name = name

    def set_last_player(self, player):
        for i, p in enumerate(self.players):
            if player == i:
                p.last = True
            else:
                p.last = False

    def correct_answer(self, player, value):
        self.players[player].score += value
        self.set_last_player(player)

    def incorrect_answer(self, player, value):
        self.players[player].score -= value

    def assign_daily_double(self):
        assigned = 0
        used_col = -1
        while assigned < self.curr_round+1:
            rand_i = random.randint(0, 5)
            rand_j = random.randint(2, 4)
            if (rand_i != used_col and
               not self.game_data.rounds[self.curr_round].
                    categories[rand_i].clues[rand_j].daily_double):
                self.game_data\
                    .rounds[self.curr_round]\
                    .categories[rand_i]\
                    .clues[rand_j].set_daily_double()
                used_col = rand_j
                assigned += 1
