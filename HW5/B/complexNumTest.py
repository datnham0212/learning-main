import ComplexNumber as cn

num1 = cn.ComplexNumber(3, -4)
num2 = cn.ComplexNumber()

num2.input()

print(num1)
print(num2)

print(num1.div(num2))
print(num1*num2)
print(num1==num2)
num1.compare(num2)