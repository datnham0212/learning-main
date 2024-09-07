def ex2(s):
    length = 0

    l = s.split(' ')

    for i in l:
        length += 1
    
    print('Number of characters: ', length)

if __name__ == '__main__':
    string = input()
    ex2(string)