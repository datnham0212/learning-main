#1 IRL examples include: Name, Age and Gender
"""
person1 = {'Name': 'John', 'Age': 36, 'Gender': 'Male'}
person2 = {'Name': 'Jane', 'Age': 25, 'Gender': 'Female'}
person3 = {'Name': 'Jack', 'Age': 42, 'Gender': 'Male'}

people = [person1, person2, person3]

print(people)
"""

#2

d = {'b':200, 'a':100, 'c':1}
"""
print(d['a']) #100
print(d.get('e', None)) #None
print(len(d)) #3
print(d.keys()) #dict_keys(['b', 'a', 'c'])
print(d.values()) #dict_values([200, 100, 1])
print(d.pop('b')) #200
print(d) #{'a' : 100, 'c' : 1}
"""

#3
d['b'] = -200
print(d)

d['e'] = 500
print(d)

# d.pop('b')
del d['b']
print(d)

