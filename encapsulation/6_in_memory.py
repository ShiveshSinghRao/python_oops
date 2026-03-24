class Square:
    def __init__(self, side):
        self.side = side  # The only real variable

    @property
    def area(self):
        # This isn't stored in memory, it's computed!
        return self.side ** 2

shape = Square(5)
print(shape.area) # 25