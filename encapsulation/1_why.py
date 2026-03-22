class BankAccount:
    def __init__(self):
        self.balance = 100


acc = BankAccount()
print(acc.balance)
acc.balance= -400
print(acc.balance)


"""
Anyone can change data and break logic

"""