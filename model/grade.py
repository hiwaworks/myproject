
import datetime
class Grade:
    def __init__(self,course,term,score):
        self.cours=self.cours
        self.term=term
        self.score=score
        self.date=datetime.datetime.now()


    def to_dict(self):
        return{
            "course":self.cours,
            "term":self.term,
            "score":self.score,
            "date":self.date
        }
