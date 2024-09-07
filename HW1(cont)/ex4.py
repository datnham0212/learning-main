def momentum(m,v):
    return m*v

def kinetic_energy(m,v):
    return 0.5*m*v**2

if __name__ == '__main__':
    m = float(input("Enter mass: "))
    v = float(input("Enter velocity: "))
    print(momentum(m,v))
    print(kinetic_energy(m,v))