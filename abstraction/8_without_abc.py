class A:
    def pay(self, amount):
        pass


class B(A):
    def pay(self, amount):
        pass


class C(A):
    pass


# obj = B()

# obj.b(100)
# AttributeError: 'B' object has no attribute 'b'

obj = C()
obj.pay(100)
# prints nothing fails silently as
# the pay method is not implemented in class C,
#  but it is defined in class A.
#  Since class C inherits from class A,
#  it has access to the pay method,
# but since it is not implemented in class C, it does nothing when called.
