class Survey:

    def __init__(self,name):
        self.name=name
        self.question_list=[]
        self.is_closed=False
        self.description=None
        self.ans_index=0

    def get_name():
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
                   self.is_closed=True

    def is_closed(self):
        return self.is_closed
