class Fraction:
    def __init__(self, top=0, bottom=1):
        self.num = top
        self.den = bottom

    def input(self):
        self.num, self.den = map(int, input("Enter a fraction: ").split("/"))
        
        if self.den == 0:
            raise ValueError("Denominator cannot be zero")
        
        

    @staticmethod
    def gcd(n, d):
        while d != 0:
            n, d = d, n % d
        return abs(n)
    
    def simplify(self):
        gcd = self.gcd(self.num, self.den)
        self.num //= gcd
        self.den //= gcd
    
    def swap(self):
        if self.num == 0:
            return self        
        self.num, self.den = self.den, self.num 

    def __add__(self, other):
        new_num = self.num * other.den + self.den * other.num
        new_den = self.den * other.den
        return Fraction(new_num, new_den)
    
    def __sub__(self, other):
        new_num = self.num * other.den - self.den * other.num
        new_den = self.den * other.den
        return Fraction(new_num, new_den)
    
    def __mul__(self, other):
        new_num = self.num * other.num
        new_den = self.den * other.den
        return Fraction(new_num, new_den)
    
    def __truediv__(self, other):
        new_num = self.num * other.den
        new_den = self.den * other.num
        return Fraction(new_num, new_den)
    
    def add(self, other):
        self.num = self.num * other.den + self.den * other.num
        self.den = self.den * other.den
        return self
    
    def sub(self, other):
        self.num = self.num * other.den - self.den * other.num
        self.den = self.den * other.den
        return self
    
    def mul(self, other):
        self.num = self.num * other.num
        self.den = self.den * other.den
        return self
    
    def div(self, other):
        self.num = self.num * other.den
        self.den = self.den * other.num
        return self

    def __str__(self):
        self.simplify()
        if self.den == 1:
            return f"{self.num}"
        return f"{self.num}/{self.den}"