class QuizBrain:
    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def still_has_question(self):
        return self.question_number < len(self.question_list)

    def nextQuestion(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_ans = input(f"{self.question_number}: {current_question.text} (True/False) :")
        self.check_ans(user_ans, current_question.ans)

    def check_ans(self, user_ans, crct_ans):
        if user_ans.lower() == crct_ans.lower():
            self.score += 1
            print("You got right answer")

        else:
            print('your ans is wrong')
            print(f'correct answer {crct_ans}')
        print(f'your score {self.score}/{len(self.question_list)}')
