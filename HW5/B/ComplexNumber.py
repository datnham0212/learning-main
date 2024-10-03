import math
class ComplexNumber:
    # Formula: z = a + b*i
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def input(self):
        self.a = float(input())
        self.b = float(input())

    def add(self, another):
        return (self.a + another.a, self.b + another.b)

    def sub(self, another):
        return (self.a - another.a, self.b - another.b)

    def mul(self, another):
        return (self.a * another.a, self.b * another.b)

    def div(self, another):
        return (self.a / another.a, self.b / another.b)
    

    def __add__(self, another):
        return (self.a + another.a, self.b + another.b)

    def __sub__(self, another):
        return (self.a - another.a, self.b - another.b)

    def __mul__(self, another):
        return (self.a * another.a, self.b * another.b)

    def __truediv__(self, another):
        return (self.a / another.a, self.b / another.b)

    def compare(self):
        pass

    def magnitude(self):
        return math.sqrt(sum(pow(self.a,2),pow(self.b,2)))

    def __eq__(self):
        pass

    def __lt__(self):
        pass

    def __gt__(self):
        pass

    def __str__(self):
        result = f"z = {self.a}+{self.b}i" if self.b > 0 else f"z = {self.a}{self.b}i" if self.b < 0 else f"z = {self.a}"
        return result