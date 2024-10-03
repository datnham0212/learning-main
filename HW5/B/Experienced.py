from Employee import Employee

class Experienced(Employee):
    def __init__(self, exp, spec):
        super().__init__()
        self.exp = exp
        self.spec = spec
    
    def showInfo(self):
        super().showInfo()
        print("exp: ", self.exp)
        print("spec: ", self.spec)