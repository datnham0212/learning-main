a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

new_list_b = [x for x in b if x in a]

# print(new_list_b)

new_list_a = []

for j in range(len(b)):
    for i in range(len(a)):
        if b[j] == a[i]:
            new_list_a.append(b[j])

new_list_a = set(new_list_a)
print(new_list_a)



