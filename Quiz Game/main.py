from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

print("Welcome to the Quiz Game!!")
print("-----------------------------------------------------------------------------------------\n")

question_bank = []

for que in question_data:
    que_text = que["text"]
    que_answer = que["answer"]
    new_que = Question(q_text=que_text, q_answer=que_answer)
    question_bank.append(new_que)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()


print(f"You've Completed the Quiz\nYour final score was {quiz.score}/{quiz.question_number}")
print("-----------------------------------------------------------------------------------------")
