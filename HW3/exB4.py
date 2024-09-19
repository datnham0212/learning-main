def cap(s):
    words = s.split(' ')
    temp = ''
    for word in words:
        temp += word.capitalize()
        temp += ' '

    return temp

if __name__ == '__main__':
    print(cap(input()))