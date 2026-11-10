class A:
    pass

obj = A()
obj2 = A()

print( obj==obj2) # false
print(obj is obj2) # false


"""
This introduces our first important distinction:
- A class defines the structure and behavior.
- An object is an actual instance of that class.
- An instance can maintain its own state.

But how does an object get its state?

That's where __init__ enters the picture.

"""