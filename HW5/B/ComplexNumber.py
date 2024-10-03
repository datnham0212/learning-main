import math
class ComplexNumber:
    # Formula: z = a + b*i

    def __init__(self, a=0, b=0):
        self.a = a
        self.b = b

    def input(self):
        self.a, self.b = list(map(int, input().split()))
        # self.b = float(input())

    def add(self, another):
        self.a = self.a + another.a
        self.b = self.b + another.b
        return self

    def sub(self, another):
        self.a = self.a - another.a
        self.b = self.b - another.b
        return self

    def mul(self, another):
        self.a = self.a * another.a
        self.b = self.b * another.b
        return self

    def div(self, another):
        self.a = self.a / another.a
        self.b = self.b / another.b
        return self
    
    def __add__(self, another):
        return ComplexNumber(self.a + another.a, self.b + another.b)

    def __sub__(self, another):
        return ComplexNumber(self.a - another.a, self.b - another.b)

    def __mul__(self, another):
        return ComplexNumber(self.a * another.a, self.b * another.b)

    def __truediv__(self, another):
        return ComplexNumber(self.a / another.a, self.b / another.b)

    def compare(self, another):
        if self == another:
            print(f"{self} is equal to {another}")
        elif self < another:
            print(f"{self} is less than {another}")
        else:
            print(f"{self} is greater than {another}")

    def magnitude(self):
        return math.sqrt(pow(self.a,2) + pow(self.b,2))

    def __eq__(self, another):
        return (self.magnitude() == another.magnitude())

    def __lt__(self, another):
        return (self.magnitude() < another.magnitude())

    def __gt__(self, another):
        return (self.magnitude() > another.magnitude())

    def __str__(self):
        result = f"z = {self.a}+{self.b}i" if self.b > 0 else f"z = {self.a}{self.b}i" if self.b < 0 else f"z = {self.a}"
        return result