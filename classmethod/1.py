class A:
    @classmethod
    def foo(cls):
        print(cls)


A.foo()  # what python does is foo(A)

# if you try this 
a = A()
a.foo() # ptyhon still does foo(A)

# its alwsys class never instance