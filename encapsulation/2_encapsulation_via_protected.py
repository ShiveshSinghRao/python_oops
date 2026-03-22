class BankAccount:
    def __init__(self):
        self._balance = 100  # this is protected 
    
    def get_balance(self):
        return self._balance
    
    def deposit(self, amt):
        if amt>0:
            self._balance += amt


acc = BankAccount()
print(acc.get_balance())
acc.deposit(500)

print(acc._balance)  # this will still work