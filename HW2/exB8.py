import math

n = int(input('Enter a number: '))
sum = 0
num_len = math.floor(math.log10(n)) + 1

clone_of_n = n

for i in range(num_len):
    temp = clone_of_n // pow(10, num_len - i - 1)
    sum += temp
    clone_of_n = clone_of_n % pow(10, num_len - i - 1)

print(f"There are {num_len} digits in {n}")
print(f"Sum of digits of {n} is {sum}")