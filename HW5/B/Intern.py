from Employee import Employee

class Intern(Employee):
    def __init__(self, majors, semester, unv_name):
        super().__init__()
        self.majors = majors
        self.semester = semester
        self.unv_name = unv_name
    
    def showInfo(self):
        super().showInfo()
        print("majors: ", self.majors)
        print("semester: ", self.semester)
        print("unv_name: ", self.unv_name)
        