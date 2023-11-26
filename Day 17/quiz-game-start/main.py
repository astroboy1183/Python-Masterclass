#TODO : Make this a more complex program / Project.

from question_model import *
from data import *
from quiz_brain import *


question_bank = []

for q in range(len(question_data)):
    question_bank.append(Question(question_data[q]["text"],question_data[q]["answer"]))


quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print(f"You have completed the quiz.\n Your final score is {quiz.score}/{len(question_bank)}")