#2 Write a program that prints out your name, address and dob
#3 Observe and assess the output

def info():

    # name = 'Burr' 

    name = input('Name: ')
    address = input('Address: ')
    dob = int(input('Date of birth: '))

    # name = 'Burr' 
    # #Whichever is the last variable assigned to, will be the last one printed out
    return f"Your name is {name}, your address is {address}, born in {dob}"

if __name__ == '__main__':
    print(info())



