class BankAccount:
    def __init___(self):
        self._balance = 1000
    
    @property
    def balance(self):           # getter
        return self._balance
    
    @balance.setter              # setter
    def balance(self, value):
        if value < 0:
            raise ValueError("invalid balance")
        self._balance = value

acc = BankAccount()
acc.balance =500
print(acc.balance)


# self._balance  this is internal
# self.balance    this is property 