# Given a range of number, find all of the even numbers

import exB1

# def find_even_num(min, max):
    # even_num_list = []
    # for i in range(min, max+1):
    #     if i % 2 == 0:
    #         even_num_list.append(i)
    # return even_num_list

def find(min ,max):
    square_list = [i for i in range(min, max+1) if exB1.isSquareNumber(i)]
    palindrome_list = [i for i in range(min, max+1) if exB1.isPalindrome(i)]
    prime_list = [i for i in range(min, max+1) if exB1.isPrime(i)]
    perfect_list = [i for i in range(min, max+1) if exB1.isPerfect(i)]

    print('Square numbers: ', square_list)
    print('Palindrome numbers: ', palindrome_list)
    print('Prime numbers: ', prime_list)
    print('Perfect numbers: ', perfect_list)

if __name__ == '__main__':
    min = int(input('Starting number: '))
    max = int(input('Closing number: '))
    # print(find_even_num(min, max))

    find(min, max)