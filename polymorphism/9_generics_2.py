from typing import Generic, TypeVar

T = TypeVar('T')

class Payment:
    def pay(self):
        pass

class UPI(Payment):
    def pay(self):
        print("UPI payment")

class Card(Payment):
    def pay(self):
        print("Card payment")


class PaymentProcessor(Generic[T]):
    def process(self, method: T):
        method.pay()


processor = PaymentProcessor[Payment]()
processor.process(UPI())
processor.process(Card())


"""
Combines:

- Subtype polymorphism 

- Generics 

"""