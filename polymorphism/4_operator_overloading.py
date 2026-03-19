print(1 + 2)          # 3
print("Hi " + "Bro")  # Hi Bro

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

p1 = Point(1, 2)
p2 = Point(3, 4)

p3 = p1 + p2
print(p3.x, p3.y)  # output : 4 6

print(len("hello"))   # string
print(len([1,2,3]))   # list


"""
Same function → works on different types

Python supports polymorphism mainly via duck typing and method overriding. 
It does not support traditional compile-time overloading like Java, 
but we can achieve similar behavior using default arguments, *args, or 
singledispatch
"""