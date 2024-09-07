
def twp(hw,trh,toh):
    return hw* (trh + toh*1.5)

if __name__ == '__main__':
    hw = int(input("Hourly wage: "))
    trh = int(input("Total regular hours: "))
    toh = int(input("Total overtime hours: "))    

    print(twp(hw,trh,toh))