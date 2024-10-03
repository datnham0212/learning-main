class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def findarea(self):
        return self.width * self.height

    def findperimeter(self):
        return 2 * (self.width + self.height)

