"""
STRATEGY PATTERN
"""

class PaymentStrategy:
    def pay(self, amount):
        pass

class UPI(PaymentStrategy):
    def pay(self, amount):
        print("Paid via UPI")

class Card(PaymentStrategy):
    def pay(self, amount):
        print("Paid via Card")

class Checkout:
    def __init__(self, strategy):
        self.strategy = strategy

    def pay(self, amount):
        self.strategy.pay(amount)


c = Checkout(UPI())  # changed behaviour at runtime
c.pay(100)

c.strategy = Card()   # changed behavior
c.pay(100)