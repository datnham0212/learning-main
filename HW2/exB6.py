min = 99
max = 999

for i in range(min, max+1):
    if i % 7 == 0 and i % 5 != 0:
        print(i)