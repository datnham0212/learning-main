from shape import Shape

class Square(Shape):
    def __init__(self, length):
        super().__init__()
        self.length = length
    
    def getarea(self):
        return self.length ** 2

# OR: 

# import shape

# class Square(shape.Shape):
#     (rest of the code)