

from abc import ABC, abstractmethod

class Engine(ABC):
    @abstractmethod
    def start(self):
        pass

class PetrolEngine(Engine):  # PetrolENgine is a Engine
    def start(self):
        print("Petrol engine")


e = PetrolEngine()  
e.start()