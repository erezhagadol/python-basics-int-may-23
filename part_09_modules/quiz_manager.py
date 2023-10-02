import random
from quiz_questions import*

user_score = 0 #keeps track of questions

def get_random_question():
    question, answer = random.choice(list(game_questions.items()))
    return question, answer