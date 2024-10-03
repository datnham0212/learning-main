"""
#a
def question_a(L):
    temp = []
    for part in L:
        each = part.split(",")
        
        for i in each:
            temp.append(i)

    return temp[0::3], temp[2::3]

#b
def question_b(a_dict):
    b = [int(i) for i in a_dict.values()]
    return sum(b)

#c
def question_c(a_dict):
    temp = max([int(i) for i in a_dict.values()])
    return [key for key, value in a_dict.items() if int(value) == temp]
    

if __name__ == '__main__':
    L = ["IT,20,600", "AP_Physics,18,200", "Calculus,19,100", "Organic_Chemistry,19,150"]
    courses, attendants = question_a(L)
    a_dict = {courses[i]:attendants[i] for i in range(len(courses))}
    print(a_dict)
    print(question_b(a_dict))
    print(question_c(a_dict))
"""

L = ["IT,20,600", "AP_Physics,18,200", "Calculus,19,100", "Organic_Chemistry,19,150"]
dict_temp = dict()
for temp in L:
    courses = temp.split(',')[0]
    attendants = temp.split(',')[2]
    dict_temp[courses] = attendants

print(dict_temp)

print(sum([int(i) for i in dict_temp.values()]))

max_val = max([int(i) for i in dict_temp.values()])

def question_c(dict_temp, max_val):
    return [key for key, value in dict_temp.items() if int(value) == max_val]

print(question_c(dict_temp, max_val))