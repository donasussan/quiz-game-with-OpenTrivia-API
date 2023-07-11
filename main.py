import requests
from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from ui import QuizInterface


question_bank = []
for question in question_data:
    question_text = question['question']
    question_answer = question['correct_answer']
    new_question = Question(text=question_text,answer=question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

#while quiz.if_more_questions_present():
  #  quiz.next_question()

#print("You have completed the Quiz")
#print(f"Your final score is:{quiz.score}/12")
quiz_ui = QuizInterface(quiz)