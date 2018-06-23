class Question:

    def __init__(self):
        self.description=None
        self.type=None
        self.choice=[]
        self.ans=None

    def add_description(self,description):
        self.description=description

    def add_choice(self,choice):
        self.choice.append(choice)

    def get_choice(self):
        return self.choice

    def set_ans(self,ans):
      try:
          if self.type == "str":
             self.ans=str(ans)
          elif self.type == "num":
             self.ans=int(ans)
          return True
      except ValueError:
          return False

    def set_type(self,type):
        self.type=type

    def get_type(self,type):
        return self.type
