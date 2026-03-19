def check_2(num: int , str: str):
    print(f"hello bunny: {num} and str is {str}")

def check_2(num:int):
    print(f"hello bunny with only num:{num}")

class A:
    def check(num: int , str: str):
        print(f"hello num: {num} and str is {str}")
    
    def check(num:int):
        print(f"hello num:{num}")



obj = A()
obj.check(1)
# check_2(1)
# check_2(1,"bob")


"""

In Python, function overloading does NOT exist (at least not like Java/C++).

So what happens?

The second check_2 function overrides the first one

Python only keeps the latest definition

So effectively, Python sees only this:
```
        def check_2(num:int):
            print(f"hello bunny with only num:{num}")
```
- Python does not support method/function overloading by default

- Latest function definition overwrites previous ones
"""