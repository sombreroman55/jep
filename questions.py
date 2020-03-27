# questions.py
# Contains the questions for the Jep rounds

class Question:
    def __init__(self, answer, difficulty):
        self.answer = answer
        self.difficulty = difficulty
        self.daily_double = False
        self.answered = False

class Category:
    def __init__(self, topic, questions):
        self.topic = topic
        self.questions = questions
