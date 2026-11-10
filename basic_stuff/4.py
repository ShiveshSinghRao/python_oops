
"""
Why you need self when you can assign things directly? like this :
"""


class Car:
    brand = None
    model = None
# What you write:
A = Car()
A.brand ="Boss"
print(A.brand)

B= Car()
B.brand="yo"
print(B.brand)

# Imagine you want to add some Business logic whenever someone changes a car's brand.
# for this you need self

class Car2:
    def set_brand(self, brand):
        if not brand:
            print("Brand cannot be empty")
            return
        if brand=="AAA":
            print("branch cannot be AAA")
            return

        self.brand = brand

A = Car2()
A.set_brand("AAA")
A.set_brand("CCC")
print(A.brand)
B= Car2()
B.set_brand("BBB")
print(B.brand)


"""
WHy do I need init when I can simply use a method to set the attribute brand?
"""
class Car3:
    def set_brand(self, brand):
        if not brand or brand == "AAA":
            print("Invalid brand")
            return
        self.brand = brand

# Step 1: Create the object
my_car = Car3() 

# ---------------------------------------------------------
# DANGER ZONE: The object exists, but it's incomplete!
# 'my_car.brand' doesn't even exist yet because 
# set_brand() hasn't been called.
# ---------------------------------------------------------

# Step 2: Initialize it (developer might forget this step)
my_car.set_brand("Toyota")



"""
Why __init__ is Superior
    __init__ solves this by forcing a strict rule:
    - An object cannot be born unless it has its required data.

You can still include all your validation logic inside __init__

"""
class Car4:
    def __init__(self, brand):
        if not brand:
            raise ValueError("Brand cannot be empty")
        if brand == "AAA":
            raise ValueError("Brand cannot be AAA")
            
        self.brand = brand

# This works perfectly:
my_car = Car4("Toyota")

# This raises an error immediately upon creation, preventing a broken object from existing:
bad_car = Car4("AAAB")


class Car5:
    def __init__(self,brand, model):
        self.brand = brand
        self.model = model


# What you write:
my_car = Car5("Toyota", "Corolla")
print(my_car.brand, my_car.model)

# What Python actually executes behind the scenes:
my_car2 = Car5.__new__(Car5)       # 1. Allocate raw memory for the object
Car5.__init__(my_car2, "Toyota2", "Corolla22") # 2. Pass that raw object as 'self'

print(my_car2.model, my_car2.brand)

"""
self is simply a reference to the exact object that
is currently being created or operated on
"""