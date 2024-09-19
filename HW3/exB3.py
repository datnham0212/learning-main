def occurence(s):
    count = 0
    for i in range(len(s)):
        if s[i].isalpha():
            count += 1 
    
    return count

if __name__ == '__main__':
    print(occurence(input()))