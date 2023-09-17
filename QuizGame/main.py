from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
question_bank=[]
for question in question_data:
    var = question['text']
    ans= question['answer']
    q=Question(var,ans)
    question_bank.append(q)
quiz=QuizBrain(question_bank)
while quiz.still_has_question():
    quiz.nextQuestion()
