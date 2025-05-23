from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []

for question in question_data :
    
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_ques = Question(question_text, question_answer)
    question_bank.append(new_ques)
    
quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()
    

print("You've finished this quiz ")
print(f"Your final score is {quiz.score} / {len(question_bank)} ")