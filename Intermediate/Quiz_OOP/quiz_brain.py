class QuizBrain:
    
    def __init__(self,question_list):
        self.question_number = 0
        self.score = 0
        self.question_list = question_list


    def check_aswer(self):
        pass
            
    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        ans = input(f"Q:{self.question_number}: {current_question.question}: (True/False)")
        self.check_aswer(ans , current_question.answer)

    def still_has_question(self):
        return self.question_number < len(self.question_list)
    
    def check_aswer(self,ans,correct_ans):
        self.ans = ans
        self.correct_ans = correct_ans
        if self.ans.lower() == correct_ans.lower():
            self.score += 1
            print("You clear this question")
            print(f"Score is {self.score}")
        else:
            print("You lose")
            print(f"Score is {self.score}")
            print(f"The Correct answer is {correct_ans}")
            False
    