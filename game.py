# game.py
#
# Game state data and functions for Jep

import json
import random
from threading import Timer
from fonts import FontManager
from PyQt6.QtMultimedia import QSoundEffect


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
    name: str = ""
    score: int = 0


class GameState:
    def __init__(self):
        self.fonts = FontManager()
        self.players = [Player() for _ in range(3)]
        self.curr_round = 0
        self.curr_player = 0
        self.wager_mode = False
        self.answer_timer = None
        self.load_clues()
        self.assign_daily_double()
        self.sounds = {
                'daily_double': "resources/sounds/daily-double.mp3",
                'final_jep': "resources/sounds/final-jep.mp3",
                'jeopardy_theme': "resources/sounds/jeopardy-theme.mp3",
                'times_up': "resources/sounds/times-up.mp3"
                }

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
        QSoundEffect.play(self.sounds[sound])

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
        return Player()

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
        self.clear_timer()

    def get_players(self):
        return self.players

    def update_player_name(self, player, name):
        self.players[player].name = name

    def set_last_player(self):
        for player in self.players:
            if player == self.players[self.curr_player]:
                player.last = True
            else:
                player.last = False

    def correct_answer(self, player, value):
        self.players[player].score += value
        self.set_last_player()
        self.clear_timer()

    def incorrect_answer(self, player, value):
        self.players[player].score -= value
        self.reset_timer()

    def reset_wager(self, player):
        self.players[self.curr_player].wager = 0

    def update_wager(self, digit):
        self.players[self.curr_player].wager *= 10
        self.players[self.curr_player].wager += digit

    def reset_score(self, player):
        self.players[player].score = 0

    def reset_timer(self):
        self.clear_timer()
        self.answer_timer = Timer(30, self.play_sound, args=['times_up'])
        self.answer_timer.daemon = True
        self.answer_timer.start()

    def clear_timer(self):
        if self.answer_timer:
            self.answer_timer.cancel()
        self.answer_timer = None

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
