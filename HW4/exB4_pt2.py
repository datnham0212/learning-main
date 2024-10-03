def func(d):
    return set(val for val in d.values())

if __name__ == '__main__':
    d = {}
    n = int(input())

for i in range(n):
    key = i
    value = input()
    d[key] = value

print(func(d))
