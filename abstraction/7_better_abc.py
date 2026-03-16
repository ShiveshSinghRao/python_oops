from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def speak(self, msg: str):
        pass

    def livesIN(self, msg: str | None = "default location"):
        print(f"Animals live on {msg}")

    def eats(self, msg: str):
        print(f"Animals eat {msg}")


class Dog(Animal):
    def speak(self, msg: str):
        print(f"Dog says: {msg}")

    def livesIN(self, msg):
        print(f"Dog lives in {msg}")


class Cat(Animal):
    def speak(self, msg: str):
        print(f"Cat says: {msg}")

    def eats(self, msg):
        print(f"Cat eats {msg}")


def animal_sound(animal: Animal, msg: str):
    animal.speak(msg)


def animal_lives_in(animal: Animal, msg: str):
    animal.livesIN(msg)


if __name__ == "__main__":
    dog = Dog()
    cat = Cat()

    dog.speak("Woof!")
    dog.livesIN("house")

    cat.speak("Meow!")
    cat.eats("fish")

    animal_sound(dog, "Woof!")
    animal_sound(cat, "Meow!")
