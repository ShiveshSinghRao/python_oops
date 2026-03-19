class Animal:
    def speak(self)->str:
        return "Hehehehehe!"

class Dog(Animal):
    def speak(self)->str:
        return "Woof"


class Cat(Animal):
    def speak(self)->str:
        return "Meow"
    

class Robot(Animal):
    def speak(self)->str:
        return "Hello World!"
    

def make_it_speak(thing):
    print(thing.speak())


list_of_obj = [Dog(), Cat(), Robot()]

for entry in list_of_obj:
    make_it_speak(entry)



"""
Same method name, different behavior in child class.
Python decides at runtime → dynamic binding

"""