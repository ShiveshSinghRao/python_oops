from abc import ABC , abstractmethod

class Animal(ABC):
    @abstractmethod
    def send(self, message: str):
        pass



class Dog(Animal):  
    def send(self, message: str):
        print(f"send {message} message from Dog")

class Cat(Animal):
    def send(self, message: str):
        print(f"send {message} message from cat")
   


if __name__ == "__main__":
    dog = Dog()
    cat = Cat()

    dog.send("hello")
    cat.send( "world")