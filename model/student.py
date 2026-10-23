from model.grade import Grade


class Student:
    def __init__(self,student_id,fullname):
       self.student_id=student_id
       self.fullname=fullname
       self.grade=list[Grade]=[]
    def add_grade(self,grade):
        if grade is not None:
            self.grade.append(grade)
            