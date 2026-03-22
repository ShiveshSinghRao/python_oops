class BankAccount:
    def __init__(self):
        self._balance = 1000

    def get_balance(self):
        return self._balance

    def set_balance(self, value):
        if value < 0:
            raise ValueError("Invalid")
        self._balance = value


acc = BankAccount()
print(acc.get_balance())
acc.set_balance(500)
print(acc.get_balance())