def b_lst(lst):
    return set(lst)

lst = [1, 2, 3, 1, 2, 5, 6, 7, 8]

print(b_lst(lst))


def a_lst(lst):
    temp = []
    visited = []

    for n in lst:
        if n not in visited:
            visited.append(n)
            temp.append(n)
    return temp

print(a_lst(lst))