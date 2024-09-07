#Calculate total charges for customer's video rentals, knowing that old movies are $2.00, new movies are $3.00

def total_charges(old, new):
    return "%.2f" % (old * 2 + new * 3)

if __name__ == '__main__':
    print("Quantity of: ")
    old = int(input("Old movies: "))
    new = int(input("New movies: "))

    print(f"Total charges: ${total_charges(old, new)}")