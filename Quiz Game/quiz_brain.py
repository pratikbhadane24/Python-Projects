class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def check_answer(self, user_ans, correct_ans):
        if user_ans == correct_ans:
            self.score += 1
            print("You got it right!")
        else:
            print("That's Wrong!")
        print(f"The correct answer was {correct_ans}")
        print(f"Your current score is {self.score}/{self.question_number}\n")
        print("-----------------------------------------------------------------------------------------\n")

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_ans = input(f"Q.{self.question_number}: {current_question.text} (True/False)?: ").capitalize()
        self.check_answer(user_ans=user_ans, correct_ans=current_question.answer)