import math

n = int(input('Enter a number: '))

num_len = math.floor(math.log10(n)) + 1

for i in range(num_len):
    temp = n // pow(10, num_len - i - 1)
    print(temp)
    n = n % pow(10, num_len - i - 1)
