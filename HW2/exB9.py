def power(a, n):
    if n == 0:
        return 1
    elif n % 2 == 0:
        half = power(a, n // 2)
        return half * half
    else:
        half = power(a, (n - 1) // 2)
        return a * half * half

# Sử dụng hàm
a = int(input("a: "))
n = int(input("n: "))
result = power(a, n)
print(f"{a}^{n} = {result}")
