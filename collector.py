from survey import Survey
from question import Question

class Collector:
    def __init__(self,phone,name):
        self.phone=phone
        self.name=name
        self.survey_list={}
        self.contact_list={}
        self.state=0;
        self.cur=None
        self.cur_question=None


    def create_Survey(self,name):
        self.cur=Survey(name)
        if self.cur is None:
            return -1
        return 1

    def add_question(self,question):
        if self.cur is not None:
            self.add_question(question)

    def process_response(self,input):
        if self.cur_question is None:
            self.cur_question=Question()
            self.cur_question.add_description(input)
            return 1
        elif self.cur_question.get_type() is None:
            self.cur_question.set_type(input)
            return 2
        else:
            self.cur_question.add_choice(input)
            return 2


    def add_contact_list(self,phone_list):
        tmp=phone_list.split(",")
        name=str(tmp[0]).lower()
        for i in range(1,len(tmp)):
            self.contact_list[name].append(str(tmp[i]))

    def get_contact_list(self,name):
        return self.contact_list[name]

    def end_choice(self):
        self.cur.add_question(self.cur_question)
        self.cur_question=None

    def end_survey(self):
        self.survey_list[self.cur.get_name()]=self.cur
        self.cur=None

    def get_survey(self,name):
        return self.survey_list[name]
