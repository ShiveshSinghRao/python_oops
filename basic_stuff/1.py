class Car:
    brand= None
    model = None


A= Car
obj = Car()

A.brand= "aaaaa"
Car.brand="bbbb"

print(A.brand)
print(Car.brand)