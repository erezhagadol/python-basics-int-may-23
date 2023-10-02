from quiz_manager import *
question, answer = get_random_question()
print("\nQuestion" , question)
user_answer = input("Your answer: ")

if user_answer == "quit":
    break
