def find(min ,max):
    for i in range(min, max + 1):
        if i % 7 == 0 and i % 9 == 0:
            print("First number to be divisible by both 7 and 9:",i)
            break

if __name__ == '__main__':
    min = int(input('Starting number: '))
    max = int(input('Closing number: '))
    find(min, max)