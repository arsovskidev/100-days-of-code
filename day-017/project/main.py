import data
import question_model
import quiz_brain

question_bank = []

for question in data.question_data:
    q = question_model.Question(question["question"], question["correct_answer"])
    question_bank.append(q)

quiz = quiz_brain.QuizBrain(question_bank)


while quiz.still_has_questions():
    quiz.next_question()

print(
    f"You completed the quiz, your final score is: {quiz.score}/{quiz.total_questions}"
)
