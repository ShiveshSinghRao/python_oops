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

    @abstractmethod
    def sound(self):
        pass


class Dog(Animal):
    def send(self, msg: str):
        print(f"Dog says: {msg}")


if __name__ == "__main__":
    dog = Dog()
    dog.communicate("Woof!")


# TypeError: Can't instantiate abstract class Dog with abstract method sound
