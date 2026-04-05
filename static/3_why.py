def add_tax(price):
    return price * 1.18

class Invoice:
    calculate_tax = add_tax



# way 1 call via class

obj = Invoice.calculate_tax(100)
print(obj)


# this works fine

# way 2 call via object ( instance )

obj = Invoice()
print(obj.calculate_tax(100))

# bound method added self so we will get 
# Type error postional arugment takes 1 but 2 are given