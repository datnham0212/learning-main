#Given a radius of a sphere, calculate the diameter, circumference, surface area and volume

def diameter(r):
    return 2*r

def circumference(r):
    return 2*3.14*r

def volume(r):
    return (4/3)*3.13*r**3

def surface_area(r):
    return 4*3.14*r**2

def info(r):
    print(f"Diameter: {diameter(r):.2f} (m)")
    print(f"Circumference: {circumference(r):.2f} (m)")
    print(f"Volume: {volume(r):.2f} (m³)")
    print(f"Surface Area: {surface_area(r):.2f} (m²)")


if __name__ == '__main__':
    r = float(input("Enter the radius of the sphere: "))
    info(r)
