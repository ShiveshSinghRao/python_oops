

class ElectricEngine():
    def start(self):
        print("eletric engine started")

class Engine:
    def start(self):
        print("engine started")
    

class Car:
    def __init__(self, engine):  # this is compostion
        self.engine = engine
    def start(self):
        self.engine.start()



car = Car(Engine())
car.start()

car_2 = Car(ElectricEngine())
car_2.start()

"""
- car does not create engine
- engine is given from outside
- car jsut uses it 


THIS IS COMPOSITION

- same car
- differnt engine
- no code change

 “Give object what it needs instead of letting it create it”
"""

