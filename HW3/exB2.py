def bin_to_dec(input):
    str_input = str(input)    
    return int(sum(pow(2, len(str_input)-i) * int(str_input[i]) for i in range(len(str_input)))/2)


if __name__ == '__main__':
    s = '000,111,101'
    temp = s.split(',')
    
    for i in range(len(temp)):
        print(bin_to_dec(temp[i]), end=' ')