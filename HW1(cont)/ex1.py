#Calculate surface area of a cube

def calc(n):
    return 6*n**2


if __name__ == '__main__':
    print(f" { calc(int(input('Given a length: '))) } m²")