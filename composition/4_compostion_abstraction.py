from abc import ABC, abstractmethod

class Engine(ABC):
    @abstractmethod
    def start(self):
        pass

class PetrolEngine(Engine):
    def start(self):
        print("Petrol engine")

class ElectricEngine(Engine):
    def start(self):
        print("Electric engine")

class Car:
    def __init__(self, engine: Engine):
        self.engine = engine

    def start(self):
        self.engine.start()


car1 = Car(PetrolEngine())
car2 = Car(ElectricEngine())

car1.start()
car2.start()

"""
COMPOSITION + ABSTRACTION (REAL DESIGN)
"""