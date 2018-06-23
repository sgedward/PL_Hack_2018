from question import Question

class Survey:

    def __init__(self,name):
        self.name=name
        self.question_list=[]
        self.closed=False
        self.description=None
        self.ans_index=0

    def get_name(self):
        return self.name

    def add_description(self,description):
        self.description=str(description)

    def add_question(self,question):
        self.question_list.append(question)

    def add_ans(self,ans):
        if self.ans_index < len(self.question_list):
            if self.question_list[self.ans_index].set_ans(ans):
                    self.ans_index+=1
            if self.ans_index == len(self.question_list):
                   self.closed=True

    def is_closed(self):
        return self.closed

    def get_next_question(self):
        return self.question_list[self.ans_index]
    
    def get_question_list(self):
        return self.question_list
