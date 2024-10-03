class Circle:
    def __init__(self, radius=1):
        self.radius = radius

    def findarea(self):
        return  3.14 * self.radius ** 2

    def findperimeter(self):
        return 2 * 3.14 * self.radius
