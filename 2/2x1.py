def count_characters(w):
    count = 0
    for i in w:
        count += 1
    return count
        

def ex1():
    s = input('Enter a string: ')
    sum = 0

    l = s.split(' ')

    for i in l:
        # for j in i:      #Alternative method
        #     count += 1
        sum += count_characters(i)
    
    print('Number of characters: ', sum)

if __name__ == '__main__':
    ex1()