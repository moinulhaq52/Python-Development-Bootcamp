from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

# Question = Question()

question_bank = []
for value in question_data:
    question_text = value["text"]
    question_answer = value["answer"]
    new_question = Question(question_text , question_answer)
    question_bank.append(new_question)

# print(question_bank)
Quiz = QuizBrain(question_bank)

while Quiz.still_has_question():
    Quiz.next_question()


print("You completed the Quiz...")
print(f"Your Final Score was {Quiz.score}/{Quiz.question_number}")