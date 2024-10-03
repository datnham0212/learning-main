class Shape:
    def __init__(self, name='square', color='white'):
        self.color = color
        self.name = name

    def findarea(self):
        pass

    def findperimeter(self):
        pass

    def __str__(self):
        return f'{self.name} has {self.color} color'