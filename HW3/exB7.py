def exB7(s):
    new_s = s.split(' ')
    set_s = set(new_s)
    
    return {word: new_s.count(word) for word in set_s}

s = 'hello world hi world goodbye world hi'
print(exB7(s))