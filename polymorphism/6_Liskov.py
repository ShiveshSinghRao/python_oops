class Animal:
    def speak(self):
        print("Some sound")

class Dog(Animal):
    def speak(self):
        print("Bark")

class Cat(Animal):
    def speak(self):
        print("Meow")


def make_sound(animal: Animal):
    animal.speak()


make_sound(Dog())  # Dog is a subtype of Animal
make_sound(Cat())



"""
This is Subtype Polymorphism

💡 Why it works?

    Because of:

    - Inheritance

    - Method overriding

    - Dynamic dispatch (runtime binding)

Interview Line

“Subtype polymorphism allows a child class object to be
 treated as a parent class reference, enabling flexible
   and extensible design.”

"""