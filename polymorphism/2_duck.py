
class Dog:
    def speak(self)->str:
        return "Woof"
    


class Cat:
    def speak(self)->str:
        return "Meow"
    

class Robot:
    def speak(self)->str:
        return "Hello World!"


def make_it_speak(thing):
    print(thing.speak())


list_of_obj = [Dog(), Cat(), Robot()]

for entry in list_of_obj:
    make_it_speak(entry)


"""
In Python, polymorphism is primarily achieved using duck typing — if it behaves like a duck, it's a duck

No inheritance needed!

"""