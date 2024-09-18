lst = [1, 2, 3, 1, 2, 5, 6, 7, 8]

b_lst = set(lst)

print(b_lst)

a_lst = []
visited = []

for n in lst:
    if n not in visited:
        visited.append(n)
        a_lst.append(n)

print(a_lst)