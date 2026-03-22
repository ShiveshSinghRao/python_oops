class BankAccount:
    def __init__(self):
        self.__balance = 100  # this is private 
    
    def get_balance(self):
        return self.__balance
    
    def deposit(self, amt):
        if amt>0:
            self.__balance += amt


acc = BankAccount()
print(acc.get_balance())
acc.deposit(500)

print(acc.__balance) # this is throw error
print(acc._BankAccount__balance)  # this will still work which is obj_className__variableName