import html
class QuizBrain:
    def __init__(self, q_list):
        self.current_question = None
        self.question_no = 0
        self.question_list = q_list
        self.score = 0

    def if_more_questions_present(self):
        return self.question_no < len(self.question_list)

    def next_question(self):
        self.current_question = self.question_list[self.question_no]
        self.question_no = self.question_no+1
        q_format_text = html.unescape(self.current_question.text)
        return f"Q.{self.question_no}: {q_format_text}"
        #user_ans = input(f"Q.{self.question_no}: {q_format_text} Type (True or False): ")
        #self.check_answer(user_ans, self.current_question.answer)

    def check_answer(self,user_ans):
        correct_ans = self.current_question.answer
        if user_ans == correct_ans:
            #print("You got it correct!")
            self.score = self.score +1
            return True
            #print( "Your score is",self.score, f"/{self.question_no}")
        else:
           # print("That's wrong!")
          #  print(f"The correct answer is: {correct_ans}")
          #  print("Your score is", self.score, f"/{self.question_no}")
            return False









