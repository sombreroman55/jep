# questions.py
# Contains the questions for the Jep rounds

class Clue:
    def __init__(self, question, answer, difficulty):
        self.question = question
        self.answer = answer
        self.difficulty = difficulty
        self.daily_double = False
        self.answered = False

class Category:
    def __init__(self, topic, clues):
        self.topic = topic
        self.clues = clues
