import math

def bin_to_dec(input):
    str_input = str(input)    
    return int(sum(pow(2, len(str_input)-i) * int(str_input[i]) for i in range(len(str_input)))/2)

def dec_to_bin(input):
    binary = ''
    while input > 0:
        binary += '0' if input % 2 == 0 else '1'
        input //= 2
    return (binary[::-1])

def hex_to_dec(input):
    pass

def octal_to_bin(input):
    pass

if __name__ == '__main__':
    first = 10011
    second = 47
    print(bin_to_dec(first))
    print(dec_to_bin(second))