class Engine:
    def start(self):
        print("engine started")
    

class Car:
    def start(self):
        obj = Engine()    # this is hardcoded
        obj.start()



"""
whats wrong here?
- car is creating Engine itself
- you cannot change engine esaily
- everyting is tightly couple


thumb rule : 
if your class A say IS-A class B then inheritance
if your class A has-A class B then composition

here a car has a engine so compostion 
"""
