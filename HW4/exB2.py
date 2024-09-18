lst = [12,24,35,70,88,120,155]

target = [1, 2, 3, 6]

new_lst = [value for index, value in enumerate(lst, start = 1) if index not in target]
    
print(new_lst)