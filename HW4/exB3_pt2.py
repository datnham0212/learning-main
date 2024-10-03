import random

first = set()
second = set()

for i in range(random.randint(10, 2000)):
    first.add(random.randint(10, 2000))

for j in range(random.randint(10, 2000)):
    second.add(random.randint(10, 2000))

print(first)
print(second)