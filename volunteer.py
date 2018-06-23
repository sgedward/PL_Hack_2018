import copy 
from send import send
from survey import Survey
from question import Question

class Background:
    def __init__(self, name, location, *extra_info):
        self.name = name
        self.location = location
        self.extra_info = extra_info

    def __str__(self):
        return " ".join([self.name, self.location, " ".join(self.extra_info)])

class Volunteer:
    
    def __init__(self, phone):
        self.phone = phone
        self.request_background()
        self.survey_list = []
        self.background = None

    def request_background(self):
        send("Please provide some background info seperated by spaces (Name, Location, etc.): ", self.phone)
        pass

    def add_survey(self, survey):
        send("You have a new survey:\n" + survey.get_name() + "\n" + survey.get_description() + "\n" \
        + self.survey_list[-1].get_next_question().get_description() + "\n" \ 
        + self.survey_list[-1].get_next_question().get_choice_string(), self.phone)
        if not self.is_busy():
            self.survey_list.append(copy.deepcopy(survey))
        

    def is_busy(self):
        return len(self.survey_list) > 0 and not self.survey_list[-1].isClosed()

    def get_survey_reduced(self, name):
        for survey in self.survey_list:
            if survey.get_name() is name and survey.isClosed():
                return survey

    def add_answer(self, resp):
        if self.is_busy():
            self.survey_list[-1].add_ans(resp)

    def process_response(self, resp):
        if not self.background:
            resp = resp.split()
            if len(resp) > 1:
                self.background = Background(resp[0], resp[1], resp[2:])
                return "Background received!"
        else:
            if self.is_busy():
                self.add_answer(resp)
                return "Answer received!\nNext question:\n" + self.survey_list[-1].get_next_question().get_description() + "\n" + self.survey_list[-1].get_next_question().get_choice_string()

    def __str__(self):
        return " ".join(["Phone:", self.phone, str(self.background), "Surveys:", self.survey_list])


    
    


        