from Employee import Employee

class Fresher(Employee):
    def __init__(self, grad_date, grad_rank, edu):
        super().__init__()
        self.grad_date = grad_date
        self.grad_rank = grad_rank
        self.edu = edu

    def showInfo(self):
        super().showInfo()
        print("grad_date: ", self.grad_date)
        print("grad_rank: ", self.grad_rank)
        print("edu: ", self.edu)