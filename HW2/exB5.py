import exB1
def nth_prime(n):
    lst = []
    count = 0
    num = 2
    while True:

        if count == n:
            break

        if exB1.isPrime(num):
            lst.append(num)
            count += 1
        num += 1
        
    return lst

if __name__ == "__main__":
    n = 10
    print(nth_prime(n))
    
    