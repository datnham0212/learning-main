def isPrime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


num = list(map(int, input().split(',')))
prime = []
for i in range(len(num)):
    if isPrime(num[i]):
        prime.append(num[i])

print(prime)