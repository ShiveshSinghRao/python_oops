

# this code will throw an error guess what is that error

class Factory:
    a= 12 # attribute

    def hello(SOME): # method
        print("Hello world")

    print("check class logic")


#Factory().hello()
A= Factory()
A.hello()


#self is missing 
"""
Python translates A.hello() into:
Factory.hello(A) # Passing 'A' into hello()
but hello is not taking any params so you get :
 - takes 0 positional arguments but 1 was given
"""

class Car:
    def __init__(YO, brand):
        YO.brand = brand
        return "Car created!"  # ❌ TypeError: __init__() should return None, not 'str'

"""
self Is Just a Variable Name (Not a Reserved Keyword)
"""


"""
Where do instance attributes like self.brand actually go?
"""

class Car2:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    def bossHello():
        pass
my_car = Car2("Tesla", "Model 3")

# Inspecting the internal dictionary of the instance
print(my_car.__dict__)
# Output: {'brand': 'Tesla', 'model': 'Model 3'}
Obj= Car2("A","BBBBBB")
print(Car2.__dict__)