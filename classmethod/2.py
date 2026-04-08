class Car:
    count = 0

    def __init__(self):
        Car.count += 1

    @classmethod
    def total_cars(cls):
        return cls.count


c1 = Car()
c2 = Car()

print(Car.total_cars())  # Expected: 2