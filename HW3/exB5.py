def count(s):
    cap = 0
    nocap = 0
    
    for char in s:
        if char.isalpha():
            if char.isupper():
                cap += 1
            else:
                nocap += 1
    
    return cap, nocap

if __name__ == '__main__':
    s = 'Hello, my name is Computer!'
    cap, nocap = count(s)

    print(cap)
    print(nocap)
