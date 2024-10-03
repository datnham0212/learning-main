import Fraction as f

f1 = f.Fraction()

f1.input()
print(f1)

f1.swap()
print(f1)

f2 = f.Fraction(3, 4)

f1.add(f2)
print(f1)

f3 = f1 - f2
print(f3)