from volunteer import Volunteer
from collector import Collector
from question import Question

class Controller:

    def __init__(self):
        self.volunteers = dict()
        self.collectors = {"+18587749238": Collector("+18587749238", "Henry")}

    def parser(self, phone, input):
        phone = str(phone)
        input = input.strip()
        print input
        if phone in self.volunteers:
            return self.volunteer_parser(self.volunteers[phone],input)
        elif phone in self.collectors:
            return self.collector_parser(self.collectors[phone],input)
        else:
            return "invalid input"


    def volunteer_parser(self, volunteer, input):
        return volunteer.process_response(input)


    def collector_parser(self, collector, input):

        temp_input = input.split()
        keyword = temp_input[0]
        print keyword

        if keyword == "EDQ":
            collector.end_survey()
            return "Survey completion finished."
        elif keyword == "EDC":
            collector.end_choice()
            return "Enter new question or send EDQ to end survery creation."
        elif keyword == "CREATE":
            if len(temp_input) > 1:
                collector.create_Survey(' '.join(temp_input[1:]))
                return "Survey creation started. Enter first question:\n"
        elif keyword == "CTL":
            if len(temp_input) > 1:
                numbers = temp_input[1:]
                for number in numbers:
                    if number not in self.volunteers:
                        volunteer = Volunteer(number)
                        self.volunteers[number] = volunteer
                collector.add_contact_list(' '.join(numbers))
                return "Contact group generated."
        elif keyword == "CHECK":
            if len(temp_input) > 1:
                data = ''.join(temp_input).split(',')
                if len(data) > 1:
                    survey_function = data[1]
                    survey_name = data[2]
                    response_list = []
                    for v in self.volunteers:
                        response_list += [v.get_survey(survey_name).get_question_list()]
                    dictionary = {}
                    for response in response_list:
                        for question in response:
                            if str(question.ans) in dictionary:
                                if question.get_type() is "str":
                                    dictionary[str(question.ans)] += [1]
                                elif question.get_type() is "num":
                                    dictionary[str(question.ans)] += [question.ans]
                    for k in dictionary:
                        if survey_function is "AVG":
                            dictionary[k] = sum(dictionary[k])/len(dictionary[k])
                        else:
                            dictionary[k] = sum(dictionary[k])
                    return str(dictionary)

        elif keyword == "SEND":
            if len(temp_input) > 2:
                for number in collector.send(temp_input[2:]):
                    if number in self.volunteers:
                        self.volunteers[number].add_survey(collector.get_survey(temp_input[1]))
                return "Survery sent"
        else:
            if collector.process_response(input) == 1:
                return "Enter answer type: "
            else:
                return "Enter answer choice text: "
