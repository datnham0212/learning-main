#Check if a number is prime, palindrome, perfect square, or none of these
def isPrime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def isPalindrome(n):
    return True if str(n) == str(n)[::-1] else False

def isPerfect(n):
    if n < 0:
        return False
    sum = 0

    for i in range(1, n):
        if n % i == 0:
            sum += i
    return True if sum == n else False

def isSquareNumber(n):
    if n < 0:
        return False
    for i in range(n):
        if i * i == n:
            return True
    return False

def indentify(n):
    num_type = []
    if isPrime(n):
        num_type.append("prime")

    if isPalindrome(n):
        num_type.append("palindrome")
    
    if isSquareNumber(n):
        num_type.append("square")

    if isPerfect(n):
        num_type.append("perfect")

    return num_type

if __name__ == '__main__':
    n = int(input("Enter a number: "))
    print(indentify(n))