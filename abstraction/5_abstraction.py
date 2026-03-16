from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def send(self, msg: str):
        pass

    def receive(self, msg: str | None = "default message"):
        print(f"Animal received: {msg}")

    def communicate(self, msg: str):
        self.send(msg)
        self.receive(msg)

    def sound(self):
        pass


class Dog(Animal):
    def send(self, msg: str):
        print(f"Dog says: {msg}")


if __name__ == "__main__":
    dog = Dog()
    dog.communicate("Woof!")


# works perfectly fine as the Dog class inherits the receive and communicate methods from the Animal class,
#  and it provides its own implementation of the send method. 
# The sound method is not abstract, so it does not need to be implemented in the Dog class.
