class QuizBrain:
    def __init__(self, question_list):
        self.score = 0
        self.question_number = 0
        self.question_list = question_list
        self.total_questions = len(self.question_list)

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(
            f"Q.{self.question_number}: {current_question.text} (True/False)?: "
        )
        if self.check_answer(user_answer, current_question.answer):
            self.score += 1
            print("You got it right!")
        else:
            print("That's wrong.")

        print(f"The correct answer was: {current_question.answer}.")
        print(f"Your current score is: {self.score}/{self.total_questions}")

    def still_has_questions(self):
        return self.question_number != self.total_questions

    def check_answer(self, user_answer, correct_answer):
        return user_answer.lower() == correct_answer.lower()
