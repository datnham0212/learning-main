#List all of the prime numbers that are less than user's input

import exB1

def prime_list(n):
    primes = []
    for i in range(2, n):
        if exB1.isPrime(i):
            primes.append(i)
    return primes

if __name__ == '__main__':
    n = int(input("Enter a number: "))
    print(prime_list(n))