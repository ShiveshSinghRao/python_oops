class Car:
    brand = None
    model = None 

# A = Car and A = Car()  both are different things
# first is a ALISA to the Class ( its a reference to the class ) second one is the object


A = Car
print(A)          # Output: <class '__main__.Car'>

# 2. A is now an instance (object) of the Car class
A = Car()
print(A)          # Output: <__main__.Car object at 0x...>
print(type(A))    # Output: <class '__main__.Car'>


