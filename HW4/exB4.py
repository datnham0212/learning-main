lst = [1,1,1,1,2,2,2,2,3,3,4,5,5]

# lst_set = set(lst)

# count = {i: lst.count(i) for i in lst_set}

# print(count)


lst = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 4, 5, 5]
visited = []
result = []

for n in lst:
    if n not in visited:
        visited.append(n)
        count = lst.count(n)
        result.append(count)  

print(result)


    
    